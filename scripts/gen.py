#!/usr/bin/python3

import sys


def main(mode, crate, version, dl, checksum, bins):
    if mode == "stable":
        with open("./stable.template.yml", "r") as file:
            action_template = file.read()

        action = action_template.replace("%%CRATE%%", crate)
        action = action.replace("%%VERSION%%", version)
        action = action.replace("%%DOWNLOAD%%", dl)
        action = action.replace("%%CHECKSUM%%", checksum)
        action = action.replace("%%BINS%%", bins)

        with open("./.github/workflows/stable.yml", "w") as file:
            file.write(action)
    elif mode == "nightly":
        print("nightly not supported yet")
        sys.exit(1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6])
