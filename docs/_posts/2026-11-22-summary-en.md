---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 2 items, 1 important content pieces were selected

---

**Technology News**
1. [Muru: Dumpleton&\#x27;s AI-assisted Rust server for Python ASGI/WSGI](#item-tech-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Muru: Dumpleton&\#x27;s AI-assisted Rust server for Python ASGI/WSGI](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, creator of mod\_wsgi, has introduced Muru, an AI-assisted Rust server for running ASGI and WSGI Python applications in development and production. Over roughly three weeks beginning November 4, 2026, he published a detailed public development log covering worker design, an “import once, fork many” model, HTTPS in development, running WSGI and ASGI together, releases without restarts, canaries without a service mesh, container and Kubernetes behavior, worker-driven scaling, scale-to-zero, scheduled overlays, and a per-page toolbar with tracing. In a post titled “AI as a lifestyle choice,” Dumpleton said AI may do much of the surface work but that deciding what is not good enough remains his responsibility, aided by 20 years of experience with mod\_wsgi. The supplied material does not report adoption, benchmark results, or production-readiness evidence.

rss · Simon Willison · Nov 21, 23:56

**「Background」** WSGI and ASGI are Python interfaces for connecting web applications to servers; WSGI predates ASGI and handles synchronous applications, while ASGI adds asynchronous support. Dumpleton created mod\_wsgi 20 years ago and has been thinking about the ideal way to serve Python web applications in production since then. Muru is his new Rust-based effort to provide tooling for both ASGI and WSGI apps in development and production.

**Tags**: `#Python`, `#ASGI/WSGI`, `#Rust`, `#web servers`, `#open source`

---