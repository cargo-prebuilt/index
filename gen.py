#!/usr/bin/python3

import sys


def main(index):
    if index == "stable":
        with open("template.yml", "r") as file:
            action_template = file.read()
        with open("README.template.md", "r") as file:
            readme_template = file.read()

        with open("crate-list", "r") as file:
            info = file.read().strip()

        crates = info.split("\n")
        readme = []
        for c in crates:
            data = c.strip().split(" ")
            action = action_template.replace("%%CRATE%%", data[0])
            action = action.replace("%%LICENSE%%", data[2])
            action = action.replace("%%BINS%%", data[3])
            action = action.replace("%%WIN_BINS%%", ",".join(map(lambda x: x + ".exe", data[3].split(","))))
            with open("./.github/workflows/" + data[0] + ".yml", "w") as file:
                file.write(action)

            readme.append("- [" + data[0] + "](" + data[1] + ")")

        readme = readme_template.replace("%%BINARIES%%", "\n".join(readme))
        with open("README.md", "w") as file:
            file.write(readme)
    elif index == "nightly":
        print("nightly not supported yet")
        sys.exit(1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1])
