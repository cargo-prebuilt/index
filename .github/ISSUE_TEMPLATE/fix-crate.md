---
name: Fix Crate
about: A crate needs fixing
title: ''
labels: fix-crate
assignees: ''

---

**Crate name**

**Details**
<!-- Reason(s) the crate might be broken, or leave blank -->

**Broken on index:**
- [ ] Stable

**Targets Broken on**

Tier 1: Crates must build on these platforms
- [ ] x86_64-apple-darwin
- [ ] aarch64-apple-darwin
- [ ] x86_64-unknown-linux-gnu
- [ ] x86_64-unknown-linux-musl
- [ ] aarch64-unknown-linux-gnu
- [ ] aarch64-unknown-linux-musl

Tier 2: Crates optionally build for these platforms, but if one fails the entire build fails
- [ ] x86_64-pc-windows-msvc
- [ ] aarch64-pc-windows-msvc
- [ ] riscv64gc-unknown-linux-gnu
- [ ] riscv64gc-unknown-linux-musl
- [ ] s390x-unknown-linux-gnu
- [ ] powerpc64le-unknown-linux-gnu
- [ ] armv7-unknown-linux-gnueabihf
- [ ] armv7-unknown-linux-musleabihf

Tier 3: Crates optionally build for these platforms, but the build will still publish if any fail
- [ ] x86_64-unknown-freebsd
- [ ] x86_64-unknown-netbsd
- [ ] powerpc64-unknown-linux-gnu

**Testing Environment**
 - OS(s): [e.g. MacOS 13, Windows 11, Ubuntu 22.04]
 - Rust Version: [e.g. 1.67.0]
