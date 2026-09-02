from pathlib import Path


def generate_profile(theme, **kwargs):
    # Read Theme
    with open(f"source/themes/{theme}/profile.txt") as f:
        profile = f.read()

    # Replace Placeholders with user input
    for item, value in kwargs.items():
        path_item = Path(f"source/themes/{theme}/{item}.txt")
        if not path_item.exists():
            continue

        with open(path_item) as f:
            profile_item = f.read().strip()
        profile_item = profile_item.replace("{ value }", value)
        profile = profile.replace(f"{{ {item} }}", profile_item)
        print(profile)

    return profile


if __name__ == "__main__":
    #Personal Info
    name ="Arnold"
    email ="arnol.hd@gmail.com"
    phone = "+1 145 989 8765"
    homepage = "https://arnold.com"
    location = "japon"

    # Social Media
    github = "arnold..."
    linkedin = "arl...."
    twitter = "arnolddlsls"
    facebook = "arno34392"
    instagram = "arno0302"
    youtube = "airnells"
    website = "arnold"

    # Select Theme
    theme ="default"

    #generate profile
    profile = generate_profile(theme, name=name, email=email)
    #print(profile)