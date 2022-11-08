#!/usr/bin/python3

import sys


extra_targets = [
    "x86_64-unknown-linux-musl",  # Must support
    "aarch64-unknown-linux-gnu",
    "aarch64-unknown-linux-musl",

    "riscv64gc-unknown-linux-gnu",  # Optional Support
    "powerpc64-unknown-linux-gnu",
    "powerpc64le-unknown-linux-gnu",
    "s390x-unknown-linux-gnu"
]


def main(mode, crate, version, dl, checksum, bins, flags, unsupported):
    if mode == "stable":
        with open("./stable.template.yml", "r") as file:
            action_template = file.read()

        action = action_template.replace("%%CRATE%%", crate)
        action = action.replace("%%VERSION%%", version)
        action = action.replace("%%DOWNLOAD%%", dl)
        action = action.replace("%%CHECKSUM%%", checksum)
        action = action.replace("%%BINS%%", bins)
        action = action.replace("%%FLAGS%%", flags)

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
    main(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6], argv[7], argv[8])
