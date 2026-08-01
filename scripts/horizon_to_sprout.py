#!/usr/bin/env python3
"""
Horizon 简报 → SproutForge 发芽衔接脚本

用法:
    python3 horizon_to_sprout.py                          # 默认取最新简报
    python3 horizon_to_sprout.py --file path/to/summary.md  # 指定简报
    python3 horizon_to_sprout.py --dry-run                 # 只解析不执行
    python3 horizon_to_sprout.py --threshold 8.0           # 只处理评分≥8.0的
    python3 horizon_to_sprout.py --tag-filter 'deepseek'   # 只处理含特定标签的

流程:
    Horizon 简报 (md) → 解析 items → 逐条调 content-router /fetch → 存入 SproutForge

前置条件:
    1. Horizon 已运行并产出简报 (uv run horizon --hours 24)
    2. content-router aApp 已安装
    3. sproutforge aApp 已安装
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# === 配置 ===
HORIZON_POSTS_DIR = Path.home() / 'Horizon' / 'docs' / '_posts'
SPROUTFORGE_AAPP_ID = 'sproutforge'
CONTENT_ROUTER_AAPP_ID = 'content-router'


def parse_horizon_summary(md_path: str) -> list[dict]:
    """解析 Horizon 简报 markdown，提取每条 item。

    Returns:
        [{title, url, score, tags, summary_snippet}, ...]
    """
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    items = []
    pattern = r'###\s+\[([^\]]+)\]\(([^)]+)\)\s+⭐️\s+([\d.]+)/10'
    matches = list(re.finditer(pattern, content))

    for match in matches:
        title = match.group(1)
        url = match.group(2)
        score = float(match.group(3))

        # 提取该 item 的标签
        rest = content[match.end():match.end() + 3000]
        tags_match = re.search(r'\*\*标签\*\*:\s*([^\n]+)', rest)
        tags = tags_match.group(1) if tags_match else ''

        # 提取摘要片段（第一段非空描述）
        # 跳过 source/platform 行，找正文段落
        lines = rest.split('\n')
        summary_lines = []
        for line in lines[1:]:  # skip title line
            line = line.strip()
            if not line:
                if summary_lines:
                    break
                continue
            if line.startswith('hackernews') or line.startswith('rss') or line.startswith('**「'):
                if line.startswith('**「'):
                    break
                continue
            summary_lines.append(line)
        summary_snippet = ' '.join(summary_lines)[:500]

        items.append({
            'title': title,
            'url': url,
            'score': score,
            'tags': tags,
            'summary': summary_snippet,
        })

    return items


from typing import Optional

def find_latest_summary() -> Optional[str]:
    """找到最新的中文简报文件。"""
    pattern = str(HORIZON_POSTS_DIR / '*-summary-zh.md')
    files = sorted(glob.glob(pattern))
    return files[-1] if files else None


def filter_items(items: list[dict], threshold: float = 0, tag_filter: str = '') -> list[dict]:
    """按评分和标签过滤 items。"""
    filtered = items
    if threshold > 0:
        filtered = [i for i in filtered if i['score'] >= threshold]
    if tag_filter:
        tag_lower = tag_filter.lower()
        filtered = [i for i in filtered if tag_lower in i['tags'].lower()]
    return filtered


def format_for_sproutforge(item: dict) -> str:
    """将 Horizon item 格式化为 SproutForge 可消化的内容。

    SproutForge 需要一段有足够信息密度的文本。
    我们把 Horizon 的摘要 + 标签组织成结构化文本。
    """
    parts = [
        f"# {item['title']}",
        f"",
        f"来源: {item['url']}",
        f"Horizon 评分: {item['score']}/10",
        f"标签: {item['tags']}",
        f"",
        f"## Horizon AI 摘要",
        f"",
        item['summary'],
    ]
    return '\n'.join(parts)


def main():
    parser = argparse.ArgumentParser(description='Horizon 简报 → SproutForge 发芽衔接')
    parser.add_argument('--file', type=str, help='指定简报文件路径')
    parser.add_argument('--dry-run', action='store_true', help='只解析不执行衔接')
    parser.add_argument('--threshold', type=float, default=0, help='评分阈值，默认全部')
    parser.add_argument('--tag-filter', type=str, default='', help='标签过滤关键词')
    parser.add_argument('--list-only', action='store_true', help='只列出 items 不衔接')
    args = parser.parse_args()

    # Step 1: 找到简报
    md_path = args.file or find_latest_summary()
    if not md_path or not os.path.exists(md_path):
        print('❌ 未找到 Horizon 简报文件')
        print(f'   搜索路径: {HORIZON_POSTS_DIR}')
        sys.exit(1)

    print(f'📄 简报文件: {md_path}')

    # Step 2: 解析 items
    items = parse_horizon_summary(md_path)
    if not items:
        print('❌ 未解析出任何 item')
        sys.exit(1)

    print(f'📋 解析出 {len(items)} 条 item')

    # Step 3: 过滤
    items = filter_items(items, args.threshold, args.tag_filter)
    if args.threshold > 0 or args.tag_filter:
        print(f'🔍 过滤后剩余 {len(items)} 条')

    # Step 4: 列出
    print()
    for i, item in enumerate(items):
        print(f"  {i+1}. [{item['score']}/10] {item['title']}")
        print(f"     {item['url']}")
        print(f"     标签: {item['tags'][:60]}")
    print()

    if args.list_only or args.dry_run:
        print('✅ dry-run / list-only 模式，不执行衔接')
        return

    # Step 5: 逐条衔接到 SproutForge（通过 content-router /fetch）
    print('---')
    print('🚀 开始衔接 SproutForge...\n')

    # 通过 aapp_call 衔接 — 这里需要通过 remio 的 aapp 机制调用
    # 脚本本身只负责解析和格式化，实际 aapp 调用由 agent 或 cron wrapper 完成
    for i, item in enumerate(items):
        content = format_for_sproutforge(item)
        print(f"--- Item {i+1}/{len(items)}: {item['title']} ---")
        print(f"  URL: {item['url']}")
        print(f"  Score: {item['score']}")
        print(f"  Content length: {len(content)} chars")
        print()

    # 输出 JSON 供 cron wrapper / agent 使用
    output = {
        'summary_file': md_path,
        'total_items': len(items),
        'items': items,
        'timestamp': datetime.now().isoformat(),
    }

    output_path = os.path.join(os.path.dirname(__file__), '.horizon_sprout_queue.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f'📦 队列已写入: {output_path}')
    print(f'   Agent 可读取此文件，逐条调 content-router /fetch → sproutforge /extract-prepare')


if __name__ == '__main__':
    main()
