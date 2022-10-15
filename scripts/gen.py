#!/usr/bin/python3

import sys, os, json


def main(index):
    if index == "stable":
        with open("../README.template.md", "r") as file:
            readme_template = file.read()

        with open("../crates.json", "r") as file:
            info = json.loads(file.read())
        os.makedirs("../index", exist_ok=True)
        with open("../index/index", "w"):
            pass

        readme = []
        for c in info["crates"]:
            print(c)
        #     readme.append("- [" + data[0] + "](" + data[1] + ")")
        #
        #     with open("../index/index", "a") as file:
        #         file.write(data[0] + "\n")
        #     with open("../index/" + data[0], "w") as file:
        #         file.write("#META " + data[0] + " " + data[1])
        #
        # readme = readme_template.replace("%%BINARIES%%", "\n".join(readme))
        # with open("../README.md", "w") as file:
        #     file.write(readme)
    elif index == "nightly":
        print("nightly not supported yet")
        sys.exit(1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1])
