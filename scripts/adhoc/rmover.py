# Remove older releases of crates

# gh -R cargo-prebuilt/index release list -L 3000 > all-releases.txt
# gh api /rate_limit

import subprocess

LIMIT = 5


def badSemVerKey(ver):
    items = ver.split(".")
    if len(items) > 3:
        print("Version is bad: " + ver)
        exit(100)
    return int(items[0]) * 10000_00000 + int(items[1]) * 100000 + int(items[2])


def main():
    tags = {}
    with open("./all-releases.txt", "rt") as file:
        filecon = file.read(-1).strip()
        taglines = filecon.splitlines()

        for tagline in taglines:
            items = tagline.split()
            item = items[2].rsplit("-", 1)

            # Remove index items
            if tagline == "" or len(items) != 4 or "index" in item:
                print("Ignored item: " + tagline)
                continue

            key = item[0]
            val = item[1]
            if key in tags:
                tags[key].append(val)
            else:
                tags[key] = [val]

    # Remove tags <= LIMIT. For those over remove 10 latest versions.
    keylist = list(tags.keys())
    for key in keylist:
        if len(tags[key]) <= LIMIT:
            tags.pop(key)
        else:
            vals = tags[key]
            vals.sort(key=badSemVerKey)  # Get versions in least to most recent order
            to_keep = vals[-LIMIT:]
            vals = vals[:-LIMIT]  # Remove latest LIMIT versions
            tags[key] = vals

            print("For removal: " + key + " " + str(vals))  # Print versions for removal
            print("  To keep: " + key + " " + str(to_keep))

    # Recreate removal tags
    retags = []
    for k in tags.keys():
        for v in tags[k]:
            retags.append(k + "-" + v)
    print("Will remove " + str(len(retags)) + " crate releases!")

    for tag in retags:
        pass

        # Uncomment below when ready!
        # print("Del: " + tag)
        # out = subprocess.run(["gh", "-R", "cargo-prebuilt/index", "release", "delete", "-y", tag])
        # print(out.stdout)
        # if out.returncode != 0:
        #  exit(1)


main()
