## Due to memory problems when building in docker containers this project is currently being restructured.

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

## Binaries

## API (Will Change)

- Index is a list of ids split by newlines. (https://github.com/crow-rest/cargo-prebuilt-index/releases/download/stable-index/index)
- Each binary has it own index that stores the version info in a list split by newlines. [VERSION INDEX_LINK]
- Following the INDEX_LINK gets you a newline split list of targets. [TARGET BINARY_ZIP BINARY_SHA256]
