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

## API (Will Change)

- Index holds the latest version built. (https://github.com/crow-rest/cargo-prebuilt-index/releases/download/stable-index/CRATE)
- Builds are put under a prerelease named CRATE-VERSION.
- The binary is in TARGET.tar.gz and the hash is in TARGET.sha256.
