#!/usr/bin/python3

import sys, os, json, zipfile, hashlib


def main(crate_id, target, path, build_path):
    with open("./crates.json", "r") as file:
        crates = json.loads(file.read())

    crate = crates["crates"][crate_id]

    end = ""
    if "windows" in target:
        end = ".exe"

    with zipfile.ZipFile(target + ".zip", "w", strict_timestamps=False) as archive:
        for b in crate["bins"]:
            archive.write(build_path + "/" + b + end, "bins/" + b + end)
        for _, _, files in os.walk(path):
            for l in files:
                if l.startswith("LICENSE"):
                    archive.write(path + "/" + l, "licenses/" + l)

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
    main(argv[1], argv[2], argv[3], argv[4])
