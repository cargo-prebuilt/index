# cargo-prebuilt-index
Some crate.io binaries built for different platforms.

## Platforms Supported (Targets)

Native:
- x86_64-unknown-linux-gnu
- x86_64-apple-darwin
- x86_64-pc-windows-msvc
- aarch64-apple-darwin

Cross:
- x86_64-unknown-linux-musl
- aarch64-unknown-linux-gnu
- aarch64-unknown-linux-musl
- riscv64gc-unknown-linux-gnu
- powerpc64-unknown-linux-gnu
- powerpc64le-unknown-linux-gnu

## Binaries

- [bacon](https://github.com/Canop/bacon)
- [cargo-audit](https://github.com/rustsec/rustsec/tree/main/cargo-audit)
- [cargo-build-deps](https://github.com/nacardin/cargo-build-deps)
- [cargo-edit](https://github.com/killercup/cargo-edit)
- [cargo-generate](https://github.com/cargo-generate/cargo-generate)
- [cargo-outdated](https://github.com/kbknapp/cargo-outdated)
- [cargo-prebuilt](https://github.com/crow-rest/cargo-prebuilt)
- [cargo-wasi](https://github.com/bytecodealliance/cargo-wasi)
- [just](https://github.com/casey/just)
- [tauri-cli](https://github.com/tauri-apps/tauri)
- [trunk](https://github.com/thedodd/trunk)
- [wasm-pack](https://github.com/rustwasm/wasm-pack)
- [wasmtime-cli](https://github.com/bytecodealliance/wasmtime)

## "API"

- Index holds the latest version built. (https://github.com/crow-rest/cargo-prebuilt-index/releases/download/stable-index/CRATE)
- Builds are put under a prerelease named CRATE-VERSION.
- The binary is in TARGET.tar.gz and the hash is in TARGET.sha256.
