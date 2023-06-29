# Misc code to reduce duplicate blocks

def gen_flags(crate_toml):
    apple_flags = [None, False, ""]  # FEATURES(0), NO_DEFAULT_FEATURES(1), EXTRA_FLAGS(2)
    linux_flags = [None, False, ""]
    windows_flags = [None, False, ""]

    if "target" in crate_toml:
        targets = crate_toml["target"]
        if "all" in targets:
            if "features" in targets["all"]:
                f = targets["all"]["features"]
                apple_flags[0] = f
                linux_flags[0] = f
                windows_flags[0] = f
            if "no-default-features" in targets["all"]:
                f = targets["all"]["no-default-features"]
                apple_flags[1] = f
                linux_flags[1] = f
                windows_flags[1] = f
            if "flags" in targets["all"]:
                f = targets["all"]["flags"]
                apple_flags[2] = f
                linux_flags[2] = f
                windows_flags[2] = f

        if "apple" in targets:
            if "features" in targets["apple"]:
                apple_flags[0] = targets["apple"]["features"]
            if "no-default-features" in targets["apple"]:
                apple_flags[1] = targets["apple"]["no-default-features"]
            if "flags" in targets["apple"]:
                apple_flags[2] = targets["apple"]["flags"]

        if "linux" in targets:
            if "features" in targets["linux"]:
                linux_flags[0] = targets["linux"]["features"]
            if "no-default-features" in targets["linux"]:
                linux_flags[1] = targets["linux"]["no-default-features"]
            if "flags" in targets["linux"]:
                linux_flags[2] = targets["linux"]["flags"]

        if "windows" in targets:
            if "features" in targets["windows"]:
                windows_flags[0] = targets["windows"]["features"]
            if "no-default-features" in targets["windows"]:
                windows_flags[1] = targets["windows"]["no-default-features"]
            if "flags" in targets["windows"]:
                windows_flags[2] = targets["windows"]["flags"]

    return {
        "apple": apple_flags,
        "linux": linux_flags,
        "windows": windows_flags,
    }
