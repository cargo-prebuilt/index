# gh -R cargo-prebuilt/index release list -L 3000 > all-releases.txt
# gh api /rate_limit

import subprocess

def main():
    tags = []
    with open("./all-releases.txt", "rt") as file:
        filecon = file.read(-1).strip()
        taglines = filecon.splitlines()

        for tag in taglines:
            items = tag.split()
            tags.append(items[2])

    for tag in tags:
        if "rtx-cli" in tag:
            print("Del: " + tag)
            out = subprocess.run(["gh", "-R", "cargo-prebuilt/index", "release", "delete", "-y", tag])
            print(out.stdout)
            if out.returncode != 0:
              exit(1)

main()
