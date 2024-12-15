import sys
import tomllib

import misc

t2_targets: list[str] = [
    "riscv64gc-unknown-linux-gnu",  # Optional Support (64-bit)
    "s390x-unknown-linux-gnu",
    "powerpc64le-unknown-linux-gnu",
    "armv7-unknown-linux-gnueabihf",  # Optional Support (32-bit)
    "armv7-unknown-linux-musleabihf",
]

win_targets: list[str] = ["x86_64-pc-windows-msvc", "aarch64-pc-windows-msvc"]

t3_targets: list[str] = [
    "x86_64-unknown-freebsd",
    "x86_64-unknown-netbsd",
    "powerpc64-unknown-linux-gnu",
]


def replace(template: str, flag: str, value: str) -> str:
    if "\n" in value:
        print("Found newline for " + flag + " flag.")
        sys.exit(1)
    return template.replace(flag, value)


def main(
    pull_request: str,
    index: str,
    crate: str,
    version: str,
    dl: str,
    checksum: str,
    filename: str,
):
    pull_request: bool = pull_request == "true"

    with open(filename, "rb") as file:
        crate_toml = tomllib.load(file)
        unsupported: str = crate_toml["info"]["unsupported"]
        git_url: str = crate_toml["info"]["git"]
        bins: str = ",".join(crate_toml["info"]["bins"])

    with open("./stable.template.yml") as file:
        action_template: str = file.read()

    action = replace(action_template, "__INDEX__", index)
    action = replace(action, "__CRATE__", crate)
    action = replace(action, "__VERSION__", version)
    action = replace(action, "__DOWNLOAD__", dl)
    action = replace(action, "__CHECKSUM__", checksum)
    action = replace(action, "__GIT__", git_url)
    action = replace(action, "__BINS__", bins)
    action = replace(action, "__FILE__", filename)
    action = replace(action, "__IF__", str(not pull_request).lower())

    # Flags
    flags = misc.gen_flags(crate_toml)

    apple_flags = flags["apple"]
    final_apple_flags = ""
    if apple_flags[0] is not None:
        final_apple_flags += f"--features '{apple_flags[0]}' "
    if apple_flags[1]:
        final_apple_flags += "--no-default-features "
    final_apple_flags += apple_flags[2]

    linux_flags = flags["linux"]
    final_linux_flags = ""
    if linux_flags[0] is not None:
        final_linux_flags += f"--features '{linux_flags[0]}' "
    if linux_flags[1]:
        final_linux_flags += "--no-default-features "
    final_linux_flags += linux_flags[2]

    windows_flags = flags["windows"]
    final_windows_flags = ""
    if windows_flags[0] is not None:
        final_windows_flags += f"--features '{windows_flags[0]}' "
    if windows_flags[1]:
        final_windows_flags += "--no-default-features "
    final_windows_flags += windows_flags[2]

    # Write Flags
    action = replace(action, "__APPLE_FLAGS__", final_apple_flags)
    action = replace(action, "__LINUX_FLAGS__", final_linux_flags)
    action = replace(action, "__WINDOWS_FLAGS__", final_windows_flags)

    # T2
    # Cross
    targets = ""
    for possible in t2_targets:
        if possible not in unsupported:
            if len(targets) != 0:
                targets += ","
            targets += possible
    if len(targets) != 0:
        action = replace(action, "__T2_CROSS_HAS_TARGETS__", "true")
        action = replace(action, "__T2_CROSS_TARGETS__", targets)
    else:
        action = replace(action, "__T2_CROSS_HAS_TARGETS__", "false")
        action = replace(action, "__T2_CROSS_TARGETS__", "err_no_targets")
    # Windows
    targets = ""
    for possible in win_targets:
        if possible not in unsupported:
            if len(targets) != 0:
                targets += ","
            targets += possible
    if len(targets) != 0:
        action = replace(action, "__T2_WIN_HAS_TARGETS__", "true")
        action = replace(action, "__T2_WIN_TARGETS__", targets)
    else:
        action = replace(action, "__T2_WIN_HAS_TARGETS__", "false")
        action = replace(action, "__T2_WIN_TARGETS__", "err_no_targets")

    # T3
    # Cross
    targets = ""
    for possible in t3_targets:
        if possible not in unsupported:
            if len(targets) != 0:
                targets += ","
            targets += possible
    if len(targets) != 0:
        action = replace(action, "__T3_CROSS_HAS_TARGETS__", "true")
        action = replace(action, "__T3_CROSS_TARGETS__", targets)
    else:
        action = replace(action, "__T3_CROSS_HAS_TARGETS__", "false")
        action = replace(action, "__T3_CROSS_TARGETS__", "err_no_targets")

    with open("./.github/workflows/stable-" + crate + ".yml", "w") as file:
        file.write(action)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6], argv[7])
