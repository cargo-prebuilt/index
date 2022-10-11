# binary-cargo-tools
Some cargo tools built for different platforms.

## Tools

- [cargo-edit](https://github.com/killercup/cargo-edit)
- [cargo-generate](https://github.com/cargo-generate/cargo-generate)
- [trunk](https://github.com/thedodd/trunk)

## "API"

- Index is a list of ids split by newlines. (https://github.com/crow-rest/binary-cargo-tools/releases/download/stable-index/index)
- Each binary has it own index that stores the version info in a list split by newlines. [VERSION INDEX_LINK]
- Following the INDEX_LINK gets you a newline split list of targets. [TARGET BINARY_ZIP BINARY_SHA256]
