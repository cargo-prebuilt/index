#!/usr/bin/python3

import sys, os, json


def main(index):
    if index == "stable":
        with open("./stable.template.yml", "r") as file:
            action_template = file.read()
        with open("./README.template.md", "r") as file:
            readme_template = file.read()

        with open("./crates.json", "r") as file:
            info = json.loads(file.read())
            info = info["crates"]
        os.makedirs("./index", exist_ok=True)
        with open("./index/index", "w"):
            pass

        readme = []
        counter = 0
        for c in info:
            action = action_template.replace("%%CRATE%%", c)
            action = action.replace("%%TIME%%", str(counter % 60))
            with open("./.github/workflows/" + c + ".yml", "w") as file:
                file.write(action)

            readme.append("- [" + c + "](" + info[c]["github"] + ")")

            with open("./index/index", "a") as file:
                file.write(c + "\n")
            with open("./index/" + c, "w") as file:
                file.write("#META " + c + " " + info[c]["github"])

            counter += 1

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
