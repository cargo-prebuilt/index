#!/usr/bin/python3

import copy
import glob
import json
import sys
import time
import tomllib
import urllib.request

stable_index = "/releases/download/stable-index/"
banned_index = "/releases/download/banned-index/"
crates_io_url = "https://crates.io"
crates_io_api = crates_io_url + "/api/v1/crates/{CRATE}"
crates_io_cdn = "https://static.crates.io/crates/{CRATE}/{CRATE}-{VERSION}.crate"


def get_newest_crate(versions):
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


def main(pull_request, duplicate, server_url, repo):
    pull_request = True if pull_request.lower() == "true" else False
    duplicate = True if duplicate.lower() == "true" else False

    if not pull_request and duplicate:
        print("{}")
        return

    if pull_request:
        with open("./crates/_allowlist", "r") as file:
            allow = file.readline()

    crates = []
    for filename in glob.glob("./crates/*.toml"):
        with open(filename, "rb") as file:
            crate_toml = tomllib.load(file)
            crates.append(crate_toml["info"]["id"])

    to_update = []
    for crate in crates:
        if (not pull_request) or (allow == "" or crate in allow.split(",")):
            if not pull_request:
                try:
                    res = urllib.request.urlopen(f"{server_url}/{repo}{banned_index}{crate}")
                    if res.status == 200:
                        continue
                except urllib.error.HTTPError:
                    pass

            version = ""
            try:
                res = urllib.request.urlopen(f"{server_url}/{repo}{stable_index}{crate}")
                version = (res.read().decode("utf-8").strip())
            except urllib.error.HTTPError:
                pass

            # Get from crates.io
            req = urllib.request.Request(
                crates_io_api.replace("{CRATE}", crate),
                data=None,
                headers={
                    "User-Agent": f"cargo-prebuilt_bot ({server_url}/{repo})"
                }
            )
            res = urllib.request.urlopen(req)
            api = json.loads(res.read().decode("utf-8")) if res and res.status == 200 else sys.exit(3)
            time.sleep(1)

            versions = []
            for v in api["versions"]:
                versions.append((v["num"], v["yanked"], v["license"],
                                 crates_io_cdn.replace("{CRATE}", crate).replace("{VERSION}", v["num"]),
                                 v["checksum"]))
            latest_crate = get_newest_crate(versions)

            if pull_request or version != latest_crate[0]:
                to_update.append((crate, latest_crate[0], latest_crate[2], api["crate"]["description"], latest_crate[3],
                                  latest_crate[4]))

    x = {
        "include": []
    }
    model = {
        "crate": None,
        "version": None,
        "license": None,
        "description": None,
        "dl": None,
        "checksum": None,
    }

    for c in to_update:
        model["crate"] = c[0]
        model["version"] = c[1]
        model["license"] = c[2]
        model["description"] = c[2]
        model["dl"] = c[3]
        model["checksum"] = c[4]

        x["include"].append(copy.deepcopy(model))

    if len(x["include"]) == 0:
        print("{}")
    else:
        print(json.dumps(x))


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4])
