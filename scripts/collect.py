import hashlib
import json
import os
import stat
import sys
import tarfile


def main(target, bin_file):
    with open(f"./{bin_file}", "r") as file:
        bins = []
        for path in file.readlines():
            path = path.strip()
            if path is not "null" and path is not "":
                basename = os.path.basename(path)
                print(f"Collecting {basename} from {path}.")
                bins.append((path, basename))

    hash_obj = {
        "bins": [],
        "archive": None
    }

    with tarfile.open(target + ".tar.gz", "w:gz") as archive:
        for b in bins:
            path = b[0]
            basename = b[1]

            # Permission Fix
            if "windows" not in target:
                st = os.stat(path)
                os.chmod(path, st.st_mode | stat.S_IEXEC)

            # Hashes
            with open(path, "rb") as file:
                file = file.read()
                h = hashlib.sha256(file).hexdigest()
                hash_obj["bins"].append({basename: h, "type": "sha256"})

            # Add to archive
            archive.add(path, basename)

    with open(target + ".tar.gz", "rb") as file:
        file = file.read()
        h = hashlib.sha256(file).hexdigest()
        hash_obj["archive"] = {"hash": h, "type": "sha256"}

    with open(target + ".sha256.json", "w") as file:
        print(json.dumps(hash_obj))  # TODO: Remove!
        file.write(json.dumps(hash_obj))


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2])
