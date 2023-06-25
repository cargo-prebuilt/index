#!/usr/bin/python3

import sys

t2_targets = [
    "x86_64-unknown-freebsd",
    "riscv64gc-unknown-linux-gnu",
    "s390x-unknown-linux-gnu",
]

win_targets = [
    "x86_64-pc-windows-msvc",
    "aarch64-pc-windows-msvc"
]

t3_targets = [
    "x86_64-unknown-netbsd",  # Optional Support (64-bit)
    "x86_64-unknown-illumos",
    "x86_64-sun-solaris",
    "powerpc64-unknown-linux-gnu",
    "powerpc64le-unknown-linux-gnu",
    "mips64-unknown-linux-gnuabi64",
    "mips64-unknown-linux-muslabi64",
    "mips64el-unknown-linux-gnuabi64",
    "mips64el-unknown-linux-muslabi64",

    "armv7-unknown-linux-gnueabihf", # Optional Support (32-bit)
    "armv7-unknown-linux-musleabihf",
]


def main(mode, pull_request, index, crate, version, crate_license, dl, checksum, bins, flags, unsupported):
    pull_request = True if pull_request == "true" else False

    if mode == "stable":
        with open("./stable.template.yml", "r") as file:
            action_template = file.read()

        action = action_template.replace("%%INDEX%%", index)
        action = action.replace("%%CRATE%%", crate)
        action = action.replace("%%VERSION%%", version)
        action = action.replace("%%LICENSE%%", crate_license)
        action = action.replace("%%DOWNLOAD%%", dl)
        action = action.replace("%%CHECKSUM%%", checksum)
        action = action.replace("%%BINS%%", bins)
        action = action.replace("%%FLAGS%%", flags)
        action = action.replace("%%IF%%", str(not pull_request).lower())

        # T2
        # Cross
        targets = ""
        for possible in t2_targets:
            if possible not in unsupported:
                if len(targets) != 0:
                    targets += ","
                targets += possible
        if len(targets) != 0:
            action = action.replace("%%T2_CROSS_HAS_TARGETS%%", "true")
            action = action.replace("%%T2_CROSS_TARGETS%%", targets)
        else:
            action = action.replace("%%T2_CROSS_HAS_TARGETS%%", "false")
            action = action.replace("%%T2_CROSS_TARGETS%%", "err_no_targets")
        # Windows
        targets = ""
        for possible in win_targets:
            if possible not in unsupported:
                if len(targets) != 0:
                    targets += ","
                targets += possible
        if len(targets) != 0:
            action = action.replace("%%T2_WIN_HAS_TARGETS%%", "true")
            action = action.replace("%%T2_WIN_TARGETS%%", targets)
        else:
            action = action.replace("%%T2_WIN_HAS_TARGETS%%", "false")
            action = action.replace("%%T2_WIN_TARGETS%%", "err_no_targets")

        # T3
        # Cross
        targets = ""
        for possible in t3_targets:
            if possible not in unsupported:
                if len(targets) != 0:
                    targets += ","
                targets += possible
        if len(targets) != 0:
            action = action.replace("%%T3_CROSS_HAS_TARGETS%%", "true")
            action = action.replace("%%T3_CROSS_TARGETS%%", targets)
        else:
            action = action.replace("%%T3_CROSS_HAS_TARGETS%%", "false")
            action = action.replace("%%T3_CROSS_TARGETS%%", "err_no_targets")

        with open("./.github/workflows/stable-" + crate + ".yml", "w") as file:
            file.write(action)
    elif mode == "nightly":
        print("nightly not supported yet")
        sys.exit(1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6], argv[7], argv[8], argv[9], argv[10], argv[11])
