import hashlib
import json
import os
import stat
import sys
import tarfile


def main(target, build_path, bins):
    bins = bins.split(",")

    hash_obj = {
        "bins": [],
        "archive": [],
    }

    ending = ""
    if "windows" in target:
        ending = ".exe"

    with tarfile.open(target + ".tar.gz", "w:gz") as archive:
        for b in bins:
            basename = b + ending
            path = build_path + "/" + basename

            # Permission Fix
            if "windows" not in target:
                st = os.stat(path)
                os.chmod(path, st.st_mode | stat.S_IEXEC)

            # Hashes
            with open(path, "rb") as file:
                file = file.read()
                h = hashlib.sha256(file).hexdigest()
                hash_obj["bins"].append({"bin": basename, "hash": h, "type": "sha256"})
                h = hashlib.sha512(file).hexdigest()
                hash_obj["bins"].append({"bin": basename, "hash": h, "type": "sha512"})
                h = hashlib.sha3_256(file).hexdigest()
                hash_obj["bins"].append({"bin": basename, "hash": h, "type": "sha3_256"})
                h = hashlib.sha3_512(file).hexdigest()
                hash_obj["bins"].append({"bin": basename, "hash": h, "type": "sha3_512"})

            # Add to archive
            archive.add(path, basename)

    with open(target + ".tar.gz", "rb") as file:
        file = file.read()
        h = hashlib.sha256(file).hexdigest()
        hash_obj["archive"].append({"hash": h, "type": "sha256"})

        # For hashes.sha256 (TODO: Maybe just use hashes.json)
        with open(target + ".sha256", "w") as tmp_file:
            tmp_file.write(h)
            tmp_file.write("  ")
            tmp_file.write(target + ".tar.gz")

        h = hashlib.sha512(file).hexdigest()
        hash_obj["archive"].append({"hash": h, "type": "sha512"})
        h = hashlib.sha3_256(file).hexdigest()
        hash_obj["archive"].append({"hash": h, "type": "sha3_256"})
        h = hashlib.sha3_512(file).hexdigest()
        hash_obj["archive"].append({"hash": h, "type": "sha3_512"})

    with open(target + ".hashes.json", "w") as file:
        file.write(json.dumps(hash_obj))


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3])
