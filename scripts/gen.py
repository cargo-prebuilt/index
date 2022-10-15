#!/usr/bin/python3

import sys, os, json


def main(index):
    if index == "stable":
        with open("./check.template.yml", "r") as file:
            check_template = file.read()
        with open("./README.template.md", "r") as file:
            readme_template = file.read()

        with open("./crates.json", "r") as file:
            info = json.loads(file.read())
            info = info["crates"]
        os.makedirs("./index", exist_ok=True)
        with open("./index/index", "w"):
            pass

        check = []
        readme = []
        for c in info:
            check.append(c)
            readme.append("- [" + c + "](" + info[c]["github"] + ")")

            with open("./index/index", "a") as file:
                file.write(c + "\n")
            with open("./index/" + c, "w") as file:
                file.write("#META " + c + " " + info[c]["github"])

        check = check_template.replace("%%CRATES%%", ", ".join(check))
        with open("./.github/workflows/check.yml", "w") as file:
            file.write(check)

        readme.sort()
        readme = readme_template.replace("%%BINARIES%%", "\n".join(readme))
        with open("./README.md", "w") as file:
            file.write(readme)
    elif index == "nightly":
        print("nightly not supported yet")
        sys.exit(1)
    else:
        sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1])
