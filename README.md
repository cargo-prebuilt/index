# cargo-prebuilt-index

Some crate.io binaries built for different platforms.

This is the index, if you are looking for the cli tool it is [here](https://github.com/cargo-prebuilt/cargo-prebuilt).

Request a crate to be added [here](https://github.com/cargo-prebuilt/index/issues/new?assignees=&labels=add-crate%2C+under-consideration&template=request-crate.md&title=).

To create your own GitHub public index use the template [here](https://github.com/cargo-prebuilt/gh-pub-index).

<sub>Only the latest versions of crates are guaranteed to be in the index.</sub>

## Platforms Supported (Targets)

Tier 1: Crates must build on these platforms
- x86_64-unknown-linux-gnu
- x86_64-unknown-linux-musl
- x86_64-apple-darwin
- aarch64-apple-darwin
- aarch64-unknown-linux-gnu
- aarch64-unknown-linux-musl

Tier 2: Crates optionally build for these platforms, but if one fails the entire build fails
- x86_64-pc-windows-msvc
- aarch64-pc-windows-msvc
- i686-pc-windows-msvc
- x86_64-unknown-freebsd
- riscv64gc-unknown-linux-gnu
- s390x-unknown-linux-gnu

Tier 3: Crates optionally build for these platforms, but the build will still publish if any fail
- x86_64-unknown-netbsd
- x86_64-unknown-illumos
- x86_64-sun-solaris
- powerpc64-unknown-linux-gnu
- powerpc64le-unknown-linux-gnu
- mips64-unknown-linux-gnuabi64
- mips64-unknown-linux-muslabi64
- mips64el-unknown-linux-gnuabi64
- mips64el-unknown-linux-muslabi64
- i686-unknown-linux-gnu
- i686-unknown-linux-musl
- i686-unknown-freebsd
- armv7-unknown-linux-gnueabihf
- armv7-unknown-linux-musleabihf
- powerpc-unknown-linux-gnu
- mips-unknown-linux-gnu
- mips-unknown-linux-musl
- mipsel-unknown-linux-gnu
- mipsel-unknown-linux-musl

## Crates

- [bacon](https://github.com/Canop/bacon)
- [bat](https://github.com/sharkdp/bat)
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
- [cargo-clone](https://github.com/JanLikar/cargo-clone)
- [cargo-deadlinks](https://github.com/deadlinks/cargo-deadlinks)
- [cargo-deb](https://github.com/kornelski/cargo-deb)
- [cargo-deny](https://github.com/EmbarkStudios/cargo-deny)
- [cargo-depgraph](https://git.sr.ht/~jplatte/cargo-depgraph)
- [cargo-diet](https://github.com/the-lean-crate/cargo-diet)
- [cargo-edit](https://github.com/killercup/cargo-edit)
- [cargo-generate](https://github.com/cargo-generate/cargo-generate)
- [cargo-get](https://github.com/nicolaiunrein/cargo-get)
- [cargo-hack](https://github.com/taiki-e/cargo-hack)
- [cargo-info](https://gitlab.com/imp/cargo-info)
- [cargo-make](https://github.com/sagiegurari/cargo-make)
- [cargo-mpirun](https://github.com/AndrewGaspar/cargo-mpirun)
- [cargo-nextest](https://github.com/nextest-rs/nextest)
- [cargo-outdated](https://github.com/kbknapp/cargo-outdated)
- [cargo-prebuilt](https://github.com/cargo-prebuilt/cargo-prebuilt)
- [cargo-quickinstall](https://github.com/cargo-bins/cargo-quickinstall)
- [cargo-semver-checks](https://github.com/obi1kenobi/cargo-semver-checks)
- [cargo-show-asm](https://github.com/pacak/cargo-show-asm)
- [cargo-update](https://github.com/nabijaczleweli/cargo-update)
- [cargo-wasi](https://github.com/bytecodealliance/cargo-wasi)
- [cargo-watch](https://github.com/watchexec/cargo-watch)
- [cargo-workspaces](https://github.com/pksunkara/cargo-workspaces)
- [cargo-zigbuild](https://github.com/rust-cross/cargo-zigbuild)
- [cocogitto](https://github.com/cocogitto/cocogitto)
- [coreutils](https://crates.io/crates/coreutils)
- [cross](https://github.com/cross-rs/cross)
- [deepl-api](https://github.com/mgruner/deepl-api-rs)
- [discord-rpc-helper](https://github.com/kekonn/discord-rpc-helper)
- [du-dust](https://github.com/bootandy/dust)
- [erdtree](https://github.com/solidiquis/erdtree)
- [evcxr_jupyter](https://github.com/google/evcxr)
- [exa](https://github.com/ogham/exa)
- [gitoxide](https://github.com/Byron/gitoxide)
- [gitui](https://github.com/extrawurst/gitui)
- [grcov](https://github.com/mozilla/grcov)
- [httm](https://github.com/kimono-koans/httm)
- [hyperfine](https://github.com/sharkdp/hyperfine)
- [irust](https://github.com/sigmaSd/IRust)
- [jql](https://github.com/yamafaktory/jql)
- [just](https://github.com/casey/just)
- [matrix-commander](https://github.com/8go/matrix-commander-rs)
- [nu](https://github.com/nushell/nushell)
- [railwayapp](https://github.com/railwayapp/cli)
- [ripgrep](https://github.com/BurntSushi/ripgrep)
- [rtx-cli](https://github.com/jdxcode/rtx)
- [rust-script](https://github.com/fornwall/rust-script)
- [rustic-rs](https://github.com/rustic-rs/rustic)
- [sccache](https://github.com/mozilla/sccache)
- [spacedisplay](https://github.com/funbiscuit/spacedisplay-rs)
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
- [xsv](https://github.com/BurntSushi/xsv)
- [zellij](https://github.com/zellij-org/zellij)
- [zet](https://github.com/yarrow/zet)
- [zp](https://github.com/bahdotsh/zp)

## "API"

- Index holds the latest version built. (https://github.com/cargo-prebuilt/index/releases/download/stable-index/CRATE)
- Builds are put under a prerelease named/tagged CRATE-VERSION.
- The binary is in TARGET.tar.gz file and the hash for the compressed tar file is in TARGET.sha256 file.
- There are also three different report files generated.
  - deps.report is a list of deps used generated by cargo tree.
  - audit.report is an audit report generated using cargo-audit.
  - license.report is a file holding information about the license(s) and the license(s) themselves.
