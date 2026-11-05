---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> 从 7 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [Alpine Linux OpenSSH-server 密码认证绕过公告](#item-tech-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Alpine Linux OpenSSH-server 密码认证绕过公告](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) ⭐️ 8.0/10

Alpine Linux 发布了 OpenSSH-server 密码认证绕过漏洞的安全公告。社区分析指出，根因是 musl libc 的 crypt\(\) 在输入口令超过 256 字节时返回错误标记“\*”，而“\*”也正是无密码账户密码哈希字段的存储值，导致哈希比较误判为匹配并让登录成功。因此，本应不接受密码的 SSH 账户会接受 256 到 1024 字符的任意密码，攻击者只要能访问 SSH 端口即可在不知道密码的情况下登录。讨论认为该问题主要影响使用 musl 的 Alpine 系统，而非所有 OpenSSH 部署；公告建议在无法立即更新时设置 PasswordAuthentication no 并重启 sshd。

hackernews · pantalaimon · 11月5日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50379704)

**「背景」** musl libc 的 crypt\(\) 在以超过 256 字节的密钥调用时会返回字符串“\*”作为错误标记；而在 /etc/shadow 等密码字段中，“\*”又用于表示账户没有可用密码，二者直接比较就可能被误判为密码匹配。该问题据报自 2016 年起存在，影响采用 musl 的 Alpine Linux、OpenWRT、buildroot 等默认配置系统，并在 OpenSSH 10.6p2 中修复。Alpine 的公告强调需更新 openssh 并重启 sshd，仅升级软件包不会替换正在运行的守护进程。

**「影响」** 运行 sshd 的 Alpine Linux 管理员必须升级 openssh 并重启守护进程，仅升级软件包不会替换正在运行的实例；若暂时无法升级，应设置 PasswordAuthentication no 并重启 sshd，以关闭无需密码即可远程登录的路径。

**「社区讨论」** 社区讨论普遍将根因归结为 musl crypt\(\) 用“\*”同时表示错误和无密码账户的哨兵值，并质疑这一设计与 musl 对 POSIX 的强调不符；也有评论从语言设计角度主张用 Result 等显式错误类型避免此类哨兵值问题。另有用户担心容器化应用更新基础镜像缓慢，并有人质疑公告措辞是否夸大了影响范围，指出问题主要局限于 Alpine/musl 环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory : openssh - server password ... | Alpine Linux</a></li>
<li><a href="https://habr.com/ru/news/1104006/">Раскрыта уязвимость sshhole в OpenSSH на базе musl Linux ...</a></li>
<li><a href="https://www.linux.org.ru/news/security/18414937">Обход аутентификации сервера OpenSSH на системах musl</a></li>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory: openssh-server password authentication ...</a></li>
<li><a href="https://www.rescana.com/post/openssh-10-6p2-alpine-musl-password-auth-bypass-prepare-now">OpenSSH 10.6p2 Fixes Critical Password Bypass on Alpine and ...</a></li>

</ul>
</details>

**标签**: `#OpenSSH`, `#Alpine Linux`, `#musl libc`, `#security vulnerability`, `#authentication bypass`

---