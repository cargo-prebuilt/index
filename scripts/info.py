import datetime
import glob
import json
import sys
import tomllib
from datetime import datetime
import misc


def main(filename, version, license_spdx, description, rustc_version_guess):
    with open(filename, "rb") as file:
        crate_toml = tomllib.load(file)

    description = json.loads(description)["description"].replace("%%SINGLE_QUOTE%%", "'")
    features = misc.gen_flags(crate_toml)

    targets = []
    for t in glob.glob("target-*"):
        targets.append(t[7:])

    info = {  # info.json
        "info_version": "1",
        "id": crate_toml["info"]["id"],
        "version": version,
        "license": license_spdx,
        "git": crate_toml["info"]["git"],
        "description": description,
        "bins": crate_toml["info"]["bins"],
        "info": {
            "rustc_version_guess": rustc_version_guess[6:],
            "index_publish_date": datetime.utcnow().strftime("%Y-%m-%d"),
            "features_apple": str(features["apple"][0]),
            "features_linux": str(features["linux"][0]),
            "features_windows": str(features["windows"][0]),
            "no_default_features_apple": str(features["apple"][1]),
            "no_default_features_linux": str(features["linux"][1]),
            "no_default_features_windows": str(features["windows"][1]),
        },
        "archive": {
            "compression": "gz",
            "ext": "tar.gz"
        },
        "files": {
            "hash": "hashes.json",
            "license": "license.report",
            "deps": "deps.report",
            "audit": "audit.report",
            "sig_info": "info.json.minisig",
            "sig_hash": "hashes.json.minisig",
        },
        "targets": targets,
    }

    with open("./info.json", "w") as file:
        file.write(json.dumps(info))

    hashes = {  # hashes.json
        "hashes_version": "1",
        "hashes": {}
    }

    # Fill hashes
    for t in targets:
        with open(f"./target-{t}/{t}.hashes.json", "r") as file:
            blob = {
                "archive": {},
                "bins": {}
            }
            hash_file = json.loads(file.read())

            for h in hash_file["archive"]:
                blob["archive"][h["type"]] = h["hash"]

            for b in hash_file["bins"]:
                if b["bin"] not in blob["bins"]:
                    blob["bins"][b["bin"]] = {}
                blob["bins"][b["bin"]][b["type"]] = b["hash"]

            hashes["hashes"][t] = blob

    with open("./hashes.json", "w") as file:
        file.write(json.dumps(hashes))


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4], argv[5])
