#!/usr/bin/python3

import sys

extra_targets = [
    # "x86_64-unknown-linux-musl",  # Must support
    # "aarch64-unknown-linux-gnu",
    # "aarch64-unknown-linux-musl",

    "x86_64-unknown-freebsd",  # Optional Support (64-bit)
    "x86_64-unknown-netbsd",
    "x86_64-unknown-illumos",
    "x86_64-sun-solaris",
    "riscv64gc-unknown-linux-gnu",
    "powerpc64-unknown-linux-gnu",
    "powerpc64le-unknown-linux-gnu",
    "s390x-unknown-linux-gnu",
    "mips64-unknown-linux-gnuabi64",
    "mips64-unknown-linux-muslabi64",
    "mips64el-unknown-linux-gnuabi64",
    "mips64el-unknown-linux-muslabi64",

    "i686-unknown-linux-gnu",  # Optional Support (32-bit)
    "i686-unknown-linux-musl",
    "i686-unknown-freebsd",
    "armv7-unknown-linux-gnueabihf",
    "armv7-unknown-linux-musleabihf",
    "powerpc-unknown-linux-gnu",
    "mips-unknown-linux-gnu",
    "mips-unknown-linux-musl",
    "mipsel-unknown-linux-gnu",
    "mipsel-unknown-linux-musl",
]


def main(mode, pull_request, crate, version, dl, checksum, bins, flags, unsupported):
    pull_request = True if pull_request == "true" else False

    if mode == "stable":
        with open("./stable.template.yml", "r") as file:
            action_template = file.read()

        action = action_template.replace("%%CRATE%%", crate)
        action = action.replace("%%VERSION%%", version)
        action = action.replace("%%DOWNLOAD%%", dl)
        action = action.replace("%%CHECKSUM%%", checksum)
        action = action.replace("%%BINS%%", bins)
        action = action.replace("%%FLAGS%%", flags)
        action = action.replace("%%IF%%", str(not pull_request))

        # Windows 32 bit
        action = action.replace("%%WIN_32_BUILD%%", str("i686-pc-windows-msvc" not in unsupported))

        # Other optional
        targets = ""
        for possible in extra_targets:
            if possible not in unsupported:
                if len(targets) != 0:
                    targets += ","
                targets += possible
        action = action.replace("%%TARGETS%%", targets)

        with open("./.github/workflows/stable-" + crate + ".yml", "w") as file:
            file.write(action)
    elif mode == "nightly":
        print("nightly not supported yet")
        sys.exit(1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6], argv[7], argv[8], argv[9])
