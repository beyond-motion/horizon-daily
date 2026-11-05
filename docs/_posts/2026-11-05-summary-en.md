---
layout: default
title: "Horizon Summary: 2026-11-05 (EN)"
date: 2026-11-05
lang: en
---

> From 7 items, 1 important content pieces were selected

---

**Technology News**
1. [Alpine Linux advisory: OpenSSH password authentication bypass](#item-tech-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Alpine Linux advisory: OpenSSH password authentication bypass](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) ⭐️ 8.0/10

Alpine Linux published a security advisory for a password-authentication bypass in OpenSSH-server. Community analysis points to musl&\#x27;s crypt\(\) returning the sentinel string &quot;\*&quot; when the supplied key is longer than 256 bytes; because &quot;\*&quot; is also the stored password field for accounts with no password, the comparison can match and permit a login. The issue appears scoped to Alpine&\#x27;s musl-based OpenSSH environment rather than all OpenSSH deployments, and the supplied material does not specify affected version ranges or patch details. The advisory is significant for Alpine systems that accept SSH password logins.

hackernews · pantalaimon · Nov 5, 14:44 · [Discussion](https://news.ycombinator.com/item?id=50379704)

**「Background」** OpenSSH&\#x27;s sshd can authenticate users with passwords by comparing the supplied password against a hash stored in the password database. On systems using musl libc, the crypt\(\) function is reported to return the sentinel string &quot;\*&quot; when the supplied key exceeds 256 bytes; because &quot;\*&quot; is also used in password fields for accounts with no password, an overlong password can match those entries. The issue is reported to affect musl-based systems such as Alpine Linux, OpenWrt, and buildroot with default settings, to have existed since 2016, and to be fixed in OpenSSH 10.6p2.

**「Impact」** Alpine Linux hosts running the affected openssh-server daemon face a remote password-authentication bypass, so administrators must either upgrade and restart sshd or set PasswordAuthentication no and restart sshd; upgrading the package alone does not replace the running daemon.

**「Community discussion」** Commenters focused on musl&\#x27;s &quot;\*&quot; sentinel and error-handling design, with some questioning why the C library behaves this way and calling the pattern unsafe. One commenter argued the write-up makes the issue seem worse than it is, while another warned that containerized applications are often slow to update their base images.

<details><summary>References</summary>
<ul>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory : openssh - server password ... | Alpine Linux</a></li>
<li><a href="https://www.linux.org.ru/news/security/18414937">Обход аутентификации сервера OpenSSH на системах musl</a></li>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory: openssh-server password authentication ...</a></li>
<li><a href="https://cybersecuritynews.com/openssh-flaw-bypass-password-authentication/">OpenSSH Flaw Could Let Attackers Bypass Password ...</a></li>
<li><a href="https://www.rescana.com/post/openssh-10-6p2-alpine-musl-password-auth-bypass-prepare-now">OpenSSH 10.6p2 Fixes Critical Password Bypass on Alpine and ...</a></li>

</ul>
</details>

**Tags**: `#OpenSSH`, `#Alpine Linux`, `#musl libc`, `#security vulnerability`, `#authentication bypass`

---