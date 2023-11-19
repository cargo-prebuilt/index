import glob
import tomllib
import sys


def main():
    with open("./README.md", "r") as file:
        readme: str = file.read()

    for filename in glob.glob("./crates/*.toml"):
        with open(filename, "rb") as file:
            crate = tomllib.load(file)

            c: str = crate["info"]["id"]
            git: str = crate["info"]["git"]

            print(f"Checking [{c}]({git})...")
            if f"- [{c}]({git})" not in readme:
                print(f"{c} is missing from the README or is incorrect!")
                sys.exit(1)


if __name__ == "__main__":
    main()
