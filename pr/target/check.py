#!/usr/bin/python3

import copy
import json
import sys
import time
import urllib.request

stable_index = "/releases/download/stable-index/"
crates_io_url = "https://crates.io"
crates_io_api = crates_io_url + "/api/v1/crates/{CRATE}/versions"
crates_io_cdn = "https://static.crates.io/crates/{CRATE}/{CRATE}-{VERSION}.crate"


def main(server_url, repo):
    with open("./crates.json", "r") as file:
        crates_json = json.loads(file.read())
        crates = crates_json["crates"]

    with open("./pr/target/target", "r") as file:
        targets = file.read()
        t = targets.split("\n")
        s_crates = t[0].split("=")[1].split(",")
        s_target = t[1].split("=")[1]
        s_push = t[2].split("=")[1]

    toUpdate = []
    for crate in crates:
        if (s_crates == "all" or crate in s_crates) and s_target not in crates[crate]["unsupported"]:
            res = urllib.request.urlopen(f"{server_url}/{repo}{stable_index}{crate}")
            version = (res.read().decode("utf-8").strip()) if res and res.status == 200 else sys.exit(3)

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

            for v in api["versions"]:
                if v["num"] == version:
                    toUpdate.append((crate, version,
                                     crates_io_cdn.replace("{CRATE}", crate).replace("{VERSION}", v["num"]),
                                     v["checksum"], ",".join(crates[crate]["bins"]), crates[crate]["flags"],
                                     s_target, s_push))

    x = {
        "include": []
    }
    model = {
        "crate": None,
        "version": None,
        "dl": None,
        "checksum": None,
        "bins": None,
        "flags": None,
        "unsupported": None,
        "target": None,
        "push": None
    }

    for c in toUpdate:
        model["crate"] = c[0]
        model["version"] = c[1]
        model["dl"] = c[2]
        model["checksum"] = c[3]
        model["bins"] = c[4]
        model["flags"] = c[5]
        model["target"] = c[6]
        model["push"] = c[7]

        x["include"].append(copy.deepcopy(model))

    if len(x["include"]) == 0:
        print("{}")
    else:
        print(json.dumps(x))


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2])
