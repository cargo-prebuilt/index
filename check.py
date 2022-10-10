#!/usr/bin/python3

import sys, os, urllib.request, json

crates_io_url = "https://crates.io"
crates_io_api = crates_io_url + "/api/v1/crates/{CRATE}/versions"
github_api = "https://api.github.com/repos/{REPO}/commits/main"


# Gets the latest version from index file.
def getLatest(index):
    latest = index.strip().split("\n")[-1]
    if latest[0] == "#":
        return ""

    latest = latest.split(" ")[0]
    return latest


def getNewestCrate(versions):
    latest = (-1, None)
    for v in versions:
        if "-" in v[0]:
            pass
        elif not v[1]:
            semver = v[0].split(".")
            total = 100 * int(semver[0]) + 10 * int(semver[1]) + int(semver[2])
            if total > latest[0]:
                latest = (total, v)

    return latest


def main(mode, index, crate):
    if mode != "stable" and mode != "nightly":
        print("first arg must be stable or nightly")
        sys.exit(1)

    repo = ""
    if mode == "nightly":
        sections = crate.split(":")
        repo = sections[0]
        crate = sections[1]

    # Get version from cache
    if not os.path.exists(crate + ".cache"):
        with open(crate + ".cache", "w"):
            pass

    with open(crate + ".cache", "r") as file:
        cached = file.read()

    if mode == "stable":
        if cached == "":
            res = urllib.request.urlopen(index + crate)
            res_body = res.read().decode("utf-8")
            v = getLatest(res_body)
            if v == "":
                cached = -1
            else:
                semver = v[0].split(".")
                cached = 100 * int(semver[0]) + 10 * int(semver[1]) + int(semver[2])
        else:
            cached = int(cached)

        # Get from crates.io
        res = urllib.request.urlopen(crates_io_api.replace("{CRATE}", crate))
        api_json = json.loads(res.read().decode("utf-8"))

        versions = []
        for v in api_json["versions"]:
            versions.append((v["num"], v["yanked"], crates_io_url + v["dl_path"], v["checksum"]))
        latest = getNewestCrate(versions)

        if latest[0] == -1 or latest[1] is None:
            print("Something when wrong with getting the highest version.")
            sys.exit(1)

        if latest[0] > cached:
            with open(crate + ".cache", "w") as file:
                file.write(str(latest[0]))
            print("::set-output name=build::true")
        else:
            print("::set-output name=build::false")

        print("::set-output name=version::" + latest[1][0])
        print("::set-output name=dl::" + latest[1][2])
        print("::set-output name=hash::" + latest[1][3])
    else:
        if cached == "":
            res = urllib.request.urlopen(index + crate)
            res_body = res.read().decode("utf-8")
            cached = getLatest(res_body)

        # Get from GitHub
        res = urllib.request.urlopen(github_api.replace("{REPO}", repo))
        api_json = json.loads(res.read().decode("utf-8"))
        sha = api_json["sha"]

        if cached != sha:
            with open(crate + ".cache", "w") as file:
                file.write(sha)
            print("::set-output name=build::true")
        else:
            print("::set-output name=build::false")


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3])
