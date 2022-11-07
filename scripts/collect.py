#!/usr/bin/python3

import hashlib
import os
import stat
import sys
import tarfile


def main(target, build_path, bins):
    bins = bins.split(",")

    ending = ""
    if "windows" in target:
        ending = ".exe"

    with tarfile.open(target + ".tar.gz", "w:gz") as archive:
        for b in bins:
            path = build_path + "/" + b + ending
            # Permission Fix
            if "windows" not in target:
                st = os.stat(path)
                os.chmod(path, st.st_mode | stat.S_IEXEC)
            # Add to archive
            archive.add(path, b + ending)

    file_hash = None
    with open(target + ".tar.gz", "rb") as file:
        file = file.read()
        file_hash = hashlib.sha256(file).hexdigest()

    if file_hash is None:
        print("Hashing failed.")
        sys.exit(1)

    with open(target + ".sha256", "w") as file:
        file.write(file_hash)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3])
