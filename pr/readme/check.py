#!/usr/bin/python3

import json
import sys


def main():
    with open("./crates.json", "r") as file:
        crates_json = json.loads(file.read())
        crates = crates_json["crates"]
        
    with open("./README.md", "r") as file:
        readme = file.read()
        
    for crate in crates:
        print(crate)
        git = crates[crate]["git"]
        print(git)
        if f"- [{crate}]({git})" not in readme:
            print(f"{crate} is missing from the README or is incorrect!")
            sys.exit(1)


if __name__ == "__main__":
    main()
