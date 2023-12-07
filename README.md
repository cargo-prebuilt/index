# cargo-prebuilt-index

Some crate.io binaries built for different platforms.

This is the index, if you are looking for the cli tool it is [here](https://github.com/cargo-prebuilt/cargo-prebuilt).

Request a crate to be added [here](https://github.com/cargo-prebuilt/index/issues/new?assignees=&labels=add-crate%2C+under-consideration&template=request-crate.md&title=).

To create your own GitHub public index use the template [here](https://github.com/cargo-prebuilt/gh-pub-index).

<sub>Only the latest versions of crates are guaranteed to be in the index.</sub>

## Public Key

The minisign public key for this index can be found in two formats:
- base64: [cargo-prebuilt-index.pub.base64](keys/cargo-prebuilt-index.pub.base64)
- asc: [cargo-prebuilt-index.pub](keys/cargo-prebuilt-index.pub)

## Platforms Supported (Targets)

Tier 1: Crates must build on these platforms
- x86_64-apple-darwin
- aarch64-apple-darwin
- x86_64-unknown-linux-gnu
- x86_64-unknown-linux-musl
- aarch64-unknown-linux-gnu
- aarch64-unknown-linux-musl

Tier 2: Crates optionally build for these platforms, but if one fails the entire build fails
- x86_64-pc-windows-msvc
- aarch64-pc-windows-msvc
- riscv64gc-unknown-linux-gnu
- s390x-unknown-linux-gnu
- powerpc64le-unknown-linux-gnu
- armv7-unknown-linux-gnueabihf
- armv7-unknown-linux-musleabihf

Tier 3: Crates optionally build for these platforms, but the build will still publish if any fail
- x86_64-unknown-freebsd
- x86_64-unknown-netbsd
- x86_64-unknown-illumos
- x86_64-sun-solaris
- powerpc64-unknown-linux-gnu

## Crates

- [bacon](https://github.com/Canop/bacon)
- [bandwhich](https://github.com/imsnif/bandwhich)
- [bat](https://github.com/sharkdp/bat)
- [bindgen-cli](https://github.com/rust-lang/rust-bindgen)
- [blob-dl](https://github.com/MicheleCioccarelli/blob-dl)
- [bob-nvim](https://github.com/MordechaiHadad/bob)
- [cargo](https://github.com/rust-lang/cargo)
- [cargo-asm](https://github.com/gnzlbg/cargo-asm)
- [cargo-audit](https://github.com/rustsec/rustsec/tree/main/cargo-audit)
- [cargo-auditable](https://github.com/rust-secure-code/cargo-auditable)
- [cargo-benchcmp](https://github.com/BurntSushi/cargo-benchcmp)
- [cargo-binstall](https://github.com/cargo-bins/cargo-binstall)
- [cargo-bitbake](https://github.com/meta-rust/cargo-bitbake)
- [cargo-bloat](https://github.com/RazrFalcon/cargo-bloat)
- [cargo-bom](https://github.com/sensorfu/cargo-bom)
- [cargo-build-deps](https://github.com/nacardin/cargo-build-deps)
- [cargo-cache](https://github.com/matthiaskrgr/cargo-cache)
- [cargo-careful](https://github.com/ralfjung/cargo-careful)
- [cargo-clone](https://github.com/JanLikar/cargo-clone)
- [cargo-deadlinks](https://github.com/deadlinks/cargo-deadlinks)
- [cargo-deb](https://github.com/kornelski/cargo-deb)
- [cargo-deny](https://github.com/EmbarkStudios/cargo-deny)
- [cargo-depgraph](https://git.sr.ht/~jplatte/cargo-depgraph)
- [cargo-diet](https://github.com/the-lean-crate/cargo-diet)
- [cargo-edit](https://github.com/killercup/cargo-edit)
- [cargo-expand](https://github.com/dtolnay/cargo-expand)
- [cargo-generate](https://github.com/cargo-generate/cargo-generate)
- [cargo-get](https://github.com/nicolaiunrein/cargo-get)
- [cargo-hack](https://github.com/taiki-e/cargo-hack)
- [cargo-info](https://gitlab.com/imp/cargo-info)
- [cargo-intraconv](https://github.com/poliorcetics/cargo-intraconv)
- [cargo-license](https://github.com/onur/cargo-license)
- [cargo-llvm-lines](https://github.com/dtolnay/cargo-llvm-lines)
- [cargo-local-registry](https://github.com/dhovart/cargo-local-registry)
- [cargo-make](https://github.com/sagiegurari/cargo-make)
- [cargo-modules](https://github.com/regexident/cargo-modules)
- [cargo-mpirun](https://github.com/AndrewGaspar/cargo-mpirun)
- [cargo-ndk](https://github.com/bbqsrc/cargo-ndk)
- [cargo-nextest](https://github.com/nextest-rs/nextest)
- [cargo-outdated](https://github.com/kbknapp/cargo-outdated)
- [cargo-prebuilt](https://github.com/cargo-prebuilt/cargo-prebuilt)
- [cargo-quickinstall](https://github.com/cargo-bins/cargo-quickinstall)
- [cargo-release](https://github.com/crate-ci/cargo-release)
- [cargo-semver-checks](https://github.com/obi1kenobi/cargo-semver-checks)
- [cargo-show-asm](https://github.com/pacak/cargo-show-asm)
- [cargo-smart-release](https://github.com/Byron/cargo-smart-release)
- [cargo-sort](https://github.com/devinr528/cargo-sort)
- [cargo-supply-chain](https://github.com/rust-secure-code/cargo-supply-chain)
- [cargo-update](https://github.com/nabijaczleweli/cargo-update)
- [cargo-wasi](https://github.com/bytecodealliance/cargo-wasi)
- [cargo-watch](https://github.com/watchexec/cargo-watch)
- [cargo-workspaces](https://github.com/pksunkara/cargo-workspaces)
- [cargo-xwin](https://github.com/rust-cross/cargo-xwin)
- [cargo-zigbuild](https://github.com/rust-cross/cargo-zigbuild)
- [cocogitto](https://github.com/cocogitto/cocogitto)
- [coreutils](https://github.com/uutils/coreutils)
- [cross](https://github.com/cross-rs/cross)
- [deepl-api](https://github.com/mgruner/deepl-api-rs)
- [difftastic](https://github.com/wilfred/difftastic)
- [discord-rpc-helper](https://github.com/kekonn/discord-rpc-helper)
- [du-dust](https://github.com/bootandy/dust)
- [erdtree](https://github.com/solidiquis/erdtree)
- [evcxr_jupyter](https://github.com/google/evcxr)
- [exa](https://github.com/ogham/exa)
- [eza](https://github.com/eza-community/eza)
- [flamegraph](https://github.com/flamegraph-rs/flamegraph)
- [gitoxide](https://github.com/Byron/gitoxide)
- [gitui](https://github.com/extrawurst/gitui)
- [grcov](https://github.com/mozilla/grcov)
- [hexyl](https://github.com/sharkdp/hexyl)
- [httm](https://github.com/kimono-koans/httm)
- [hyperfine](https://github.com/sharkdp/hyperfine)
- [irust](https://github.com/sigmaSd/IRust)
- [jql](https://github.com/yamafaktory/jql)
- [just](https://github.com/casey/just)
- [jxl-oxide-cli](https://github.com/tirr-c/jxl-oxide)
- [lsd](https://github.com/lsd-rs/lsd)
- [matrix-commander](https://github.com/8go/matrix-commander-rs)
- [nu](https://github.com/nushell/nushell)
- [oha](https://github.com/hatoo/oha)
- [oxipng](https://github.com/shssoichiro/oxipng)
- [railwayapp](https://github.com/railwayapp/cli)
- [ripgrep](https://github.com/BurntSushi/ripgrep)
- [rsign2](https://github.com/jedisct1/rsign2)
- [rtx-cli](https://github.com/jdxcode/rtx)
- [rust-script](https://github.com/fornwall/rust-script)
- [rustic-rs](https://github.com/rustic-rs/rustic)
- [rustypaste-cli](https://github.com/orhun/rustypaste-cli)
- [rustypaste](https://github.com/orhun/rustypaste)
- [sccache](https://github.com/mozilla/sccache)
- [spacedisplay](https://github.com/funbiscuit/spacedisplay-rs)
- [sqlx-cli](https://github.com/launchbadge/sqlx)
- [tauri-cli](https://github.com/tauri-apps/tauri)
- [trunk](https://github.com/thedodd/trunk)
- [typos-cli](https://github.com/crate-ci/typos)
- [volo-cli](https://github.com/cloudwego/volo)
- [wasm-pack](https://github.com/rustwasm/wasm-pack)
- [wasmer-cli](https://github.com/wasmerio/wasmer)
- [wasmtime-cli](https://github.com/bytecodealliance/wasmtime)
- [watchexec-cli](https://github.com/watchexec/watchexec)
- [webbundle-cli](https://github.com/google/webbundle)
- [websocat](https://github.com/vi/websocat)
- [whiz](https://github.com/zifeo/whiz)
- [wiki-tui](https://github.com/Builditluc/wiki-tui)
- [wit-bindgen-cli](https://github.com/bytecodealliance/wit-bindgen)
- [wthrr](https://github.com/tobealive/wthrr-the-weathercrab)
- [wthrr](https://github.com/tobealive/wthrr-the-weathercrab)
- [xsv](https://github.com/BurntSushi/xsv)
- [zellij](https://github.com/zellij-org/zellij)
- [zet](https://github.com/yarrow/zet)
- [zp](https://github.com/bahdotsh/zp)

## "API"

See [API](API.md)
