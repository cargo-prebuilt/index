#!/usr/bin/python3

import copy
import json
import sys
import urllib.request

stable_index = "https://github.com/crow-rest/cargo-prebuilt-index/releases/download/stable-index/"
crates_io_url = "https://crates.io"
crates_io_api = crates_io_url + "/api/v1/crates/{CRATE}/versions"
github_api = "https://api.github.com/repos/{REPO}/commits/main"


def getNewestCrate(versions):
    latest = None
    store = (-1, -1, -1)
    for v in versions:
        if "-" in v[0]:
            pass
        elif not v[1]:
            semver = v[0].split(".")
            semver = (int(semver[0]), int(semver[1]), int(semver[2]))
            if semver[0] > store[0]:
                store = semver
                latest = v
            elif semver[0] == store[0]:
                if semver[1] > store[1]:
                    store = semver
                    latest = v
                elif semver[1] == store[1]:
                    if semver[2] > store[2]:
                        store = semver
                        latest = v
    return latest


def main(mode):
    with open("./crates.json", "r") as file:
        crates = json.loads(file.read())
        crates = crates["crates"]

    if mode == "stable":
        toUpdate = []
        for crate in crates:
            version = ""
            try:
                res = urllib.request.urlopen(stable_index + crate)
                version = (res.read().decode("utf-8").strip())
            except urllib.error.HTTPError:
                pass

            # Get from crates.io
            res = urllib.request.urlopen(crates_io_api.replace("{CRATE}", crate))
            api = json.loads(res.read().decode("utf-8")) if res and res.status == 200 else sys.exit(3)

            versions = []
            for v in api["versions"]:
                versions.append((v["num"], v["yanked"], crates_io_url + v["dl_path"], v["checksum"]))
            latestCrate = getNewestCrate(versions)

            if version != latestCrate[0]:
                toUpdate.append((crate, latestCrate[0], latestCrate[2], latestCrate[3], ",".join(crates[crate]["bins"]),
                                 crates[crate]["flags"]))

        x = {
            "include": []
        }
        model = {
            "crate": None,
            "version": None,
            "dl": None,
            "checksum": None,
            "bins": None,
            "flags": None
        }

        for c in toUpdate:
            model["crate"] = c[0]
            model["version"] = c[1]
            model["dl"] = c[2]
            model["checksum"] = c[3]
            model["bins"] = c[4]
            model["flags"] = c[5]

            x["include"].append(copy.deepcopy(model))

        if len(x["include"]) == 0:
            print("{}")
        else:
            print(json.dumps(x))
    elif mode == "nightly":
        sys.exit(100)
    else:
        sys.exit(1)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1])
