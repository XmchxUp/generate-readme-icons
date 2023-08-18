import sys
import json
import random

DEFAULT_ICON_NAMES = "python,rust,ts"
DEFAULT_GENERATE_TYPE = "skills"


def random_color_generator():
    return "%06x" % random.randint(0, 0xFFFFFF)


def get_icons_hex_dict():
    with open("./res/simple-icons.json") as file:
        data = json.load(file)
        res = dict()
        for d in data["icons"]:
            res[d["title"].lower()] = d["hex"]
        return res


def get_skill_icons():
    with open("./res/skill-icons.txt", "r") as file:
        lines = file.readlines()
        return [line.strip("\n") for line in lines]


def generate(generator_name: str, icon_names: str, logo_color: str):
    if generator_name == "skills":
        with open("./skill.md", "w") as file:
            file.write(
                f"[![My Skills](https://skillicons.dev/icons?i={icon_names}&theme=light)](https://skillicons.dev)"
            )
    elif generator_name == "shields":
        icons_hex_map = get_icons_hex_dict()
        with open("./shields.md", "w") as file:
            lines = []
            icon_names = icon_names.lower()

            for icon_name in icon_names.split(","):
                tmp_logo_color = logo_color
                if logo_color != "white":
                    tmp_logo_color = random_color_generator()

                if icon_name in icons_hex_map:
                    lines.append(
                        f"https://img.shields.io/badge/-{icon_name}-{icons_hex_map[icon_name]}?style=flat-square&logo={icon_name}&logoColor={tmp_logo_color}\n"
                    )
            file.writelines(lines)
    else:
        raise Exception("not found generator name")


if __name__ == "__main__":
    icon_names = DEFAULT_ICON_NAMES
    generator_name = DEFAULT_GENERATE_TYPE
    if len(sys.argv) >= 4:
        generator_name = sys.argv[1]
        icon_names = sys.argv[2]
        logo_color = sys.argv[3]
    generate(generator_name, icon_names, logo_color)
