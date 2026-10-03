import sys
import tomllib


def main(item: str):
    with open("Cargo.toml", "rb") as file:
        cargo_toml = tomllib.load(file)
        package = cargo_toml["package"]

    if item in package:
        print(package[item].replace("'", "__SINGLE_QUOTE__"))
    else:
        print("")


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1])
