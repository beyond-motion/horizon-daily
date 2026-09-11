---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 7 items, 2 important content pieces were selected

---

**Technology News**
1. [trynix.dev boots any Nix package in a browser via qemu-wasm](#item-tech-news-1) ⭐️ 7.0/10
2. [Shopify returns mobile apps to native Swift and Kotlin](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [trynix.dev boots any Nix package in a browser via qemu-wasm](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 7.0/10

Farid Zakaria has launched trynix.dev, which Simon Willison describes as Zakaria&\#x27;s self-called &quot;magnum opus&quot; of Nix work. The site runs a qemu-wasm-powered x86\_64 Linux virtual machine entirely in the browser through WebAssembly, and that VM can be booted with any Nix package from the past 13 years. Packages are URL addressable: navigating to https://trynix.dev/?pkg=python3%403.6.2 and clicking &quot;Load&quot; opens an interactive shell against a VM running Python 3.6.2 from 2017. Zakaria has built further tooling on top of it, including trynix-preview, a GitHub Action that comments a link on a pull request so the PR&\#x27;s build can be booted in the browser — &quot;No servers, just browsers.&quot;

rss · Simon Willison · Sep 10, 23:44

**「Background」** Nix is a package manager and build system whose nixpkgs collection has defined reproducible packages for well over a decade, and trynix.dev indexes that historical output so individual packages can be addressed by URL, such as python3@3.6.2, a Python release from 2017 \(tool-1-2\). The tooling rests on qemu-wasm, which compiles the QEMU emulator to WebAssembly so an x86\_64 Linux machine can boot inside a browser tab with no server involved, paired with a nixpkgs-multiverse index that tracks what the repository ever shipped \(tool-1-3\).

**「Impact」** Nix users and maintainers gain a serverless way to inspect and interact with arbitrary historical package versions directly from a URL, and the trynix-preview action extends that to reviewing a pull request by booting its actual build in the browser. The source does not state performance, resource, or browser-compatibility limits for running these VMs.

<details><summary>References</summary>
<ul>
<li><a href="https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser">Any Nix package, live in your browser | Farid Zakaria’s Blog</a></li>
<li><a href="https://trynix.dev/">trynix — boot anything nixpkgs ever shipped, in your browser</a></li>

</ul>
</details>

**Tags**: `#Nix`, `#WebAssembly`, `#qemu-wasm`, `#Browser-based VMs`, `#Reproducible environments`

---

<a id="item-tech-news-2"></a>
### [Shopify returns mobile apps to native Swift and Kotlin](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 7.0/10

Shopify is moving its mobile apps from React Native back to separate Swift and Kotlin native codebases, according to a Shopify Engineering post highlighted by Simon Willison. Shopify had switched to React Native in 2020 to avoid building the same features twice, let developers work across the stack, and spend less time on feature parity. In the new post, Shopify says native still means maintaining software on two platforms, but AI agents can now do enough implementation, translation, testing, and review work that this cost is no longer the deciding factor. Shopify maintains react-native-skia, flash-list, and restyle; the first two are finding new homes, while restyle, described as having a smaller user base, will be archived at the end of 2026. The post gives full credit to React Native as a great platform during the six years Shopify used it.

rss · Simon Willison · Sep 10, 21:11

**「Background」** React Native is a cross-platform framework that lets teams write one JavaScript-based codebase for both iOS and Android, which Shopify adopted in 2020 to avoid building each feature twice and to let developers work across the stack. Going &quot;native&quot; instead means maintaining separate Swift code for iOS and Kotlin code for Android, a duplication cost that historically drove companies toward cross-platform frameworks. Shopify&\#x27;s reversal rests on the claim that AI coding agents can now handle enough implementation, translation, testing, and review work to make that duplicated maintenance burden less decisive than it was in 2020 \(the company&\#x27;s own post is dated Sep 10, 2026\).

**「Impact」** Developers relying on Shopify&\#x27;s React Native libraries face the concrete change that restyle will be archived at the end of 2026, while the broader React Native ecosystem gets a notable example of an AI-driven reassessment of cross-platform versus native development.

<details><summary>References</summary>
<ul>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify ( 2026 ) - Shopify</a></li>
<li><a href="https://sesamedisk.com/shopify-switching-from-react-native-to/">Shopify Switching from React Native - Sesame Disk</a></li>

</ul>
</details>

**Tags**: `#React Native`, `#mobile development`, `#AI coding agents`, `#Shopify`, `#native apps`

---