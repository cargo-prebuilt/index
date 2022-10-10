#!/usr/bin/python3

import sys, zipfile, hashlib


def main(bins, licenses, target, path, build_path):
    with zipfile.ZipFile(target + ".zip", "w") as archive:
        for b in bins.split(","):
            archive.write(build_path + "/" + b, b)
        for l in licenses.split(","):
            archive.write(path + "/" + l, l)

    file_hash = None
    with open(target + ".zip", "rb") as file:
        file = file.read()
        file_hash = hashlib.sha256(file).hexdigest()

    if file_hash is None:
        print("Hashing failed.")
        sys.exit(1)

    with open(target + ".sha256", "w") as file:
        file.write(file_hash)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4], argv[5])
