import glob
import json
import sys
import tomllib
import urllib.request
from typing import Any, Optional

stable_index: str = "/releases/download/stable-index/"
banned_index: str = "/releases/download/banned-index/"
crates_io_index: str = "https://index.crates.io/"
crates_io_cdn: str = "https://static.crates.io/crates/{CRATE}/{CRATE}-{VERSION}.crate"


def get_index_url(crate: str) -> str:
    crate: str = crate.lower()
    length: int = len(crate)
    url: str = crates_io_index
    if 1 <= length <= 2:
        url += f"{length}/{crate}"
    elif length == 3:
        url += f"3/{crate[0]}/{crate}"
    else:
        url += f"{crate[0:2]}/{crate[2:4]}/{crate}"
    return url


def get_newest_crate(versions: list[Any]) -> Any:
    latest: Optional[Any] = None
    store = (-1, -1, -1)
    for v in versions:
        if "-" in v["vers"]:
            pass
        elif not v["yanked"]:
            semver = v["vers"].split(".")
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


def main(pull_request: str, duplicate: str, server_url: str, repo: str):
    pull_request: bool = True if pull_request.lower() == "true" else False
    duplicate: bool = True if duplicate.lower() == "true" else False

    if not pull_request and duplicate:
        print("{}")
        return

    if pull_request:
        with open("./pr/_allowlist", "r") as file:
            allow: str = file.readline()

    to_update = []
    for filename in glob.glob("./crates/*.toml"):
        with open(filename, "rb") as file:
            crate_toml = tomllib.load(file)
            crate: str = crate_toml["info"]["id"]

        if (not pull_request) or (allow == "" or crate in allow.split(",")):
            if not pull_request:
                try:
                    res = urllib.request.urlopen(f"{server_url}/{repo}{banned_index}{crate}")
                    if res.status == 200:
                        continue
                except urllib.error.HTTPError:
                    pass

            version: str = ""
            try:
                res = urllib.request.urlopen(f"{server_url}/{repo}{stable_index}{crate}")
                version = (res.read().decode("utf-8").strip())
            except urllib.error.HTTPError:
                pass

            # Get from index.crates.io
            req = urllib.request.Request(
                get_index_url(crate),
                data=None,
                headers={
                    "User-Agent": f"cargo-prebuilt_bot ({server_url}/{repo})"
                }
            )
            res = urllib.request.urlopen(req)
            crate_infos_raw: str = res.read().decode("utf-8") if res and res.status == 200 else sys.exit(3)
            crate_infos_raw: list[str] = crate_infos_raw.strip().split("\n")

            crate_infos: list[Any] = []
            for c in crate_infos_raw:
                crate_infos.append(json.loads(c))

            latest_crate: Any = get_newest_crate(crate_infos)

            if pull_request or version != latest_crate["vers"]:
                to_update.append({
                    "crate": crate,
                    "version": latest_crate["vers"],
                    "dl": crates_io_cdn.replace("{CRATE}", crate).replace("{VERSION}", latest_crate["vers"]),
                    "checksum": latest_crate["cksum"],
                    "file": filename,
                })

    x = {
        "include": []
    }
    for c in to_update:
        x["include"].append(c)

    if len(x["include"]) == 0:
        print("{}")
    else:
        print(json.dumps(x))


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4])
