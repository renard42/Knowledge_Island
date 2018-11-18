# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cat = Character("Шерлок")

screen map:
    imagemap:
        idle "images/Map_clean.png"
        hover "images/Map_labels.png"

        hotspot(287,5,442,240) action Return("english") alt "english"
        hotspot(670,151,337,297) action Return("geography") alt "geography"
        hotspot(23,195,435,332) action Return("russian") alt "russian"
        hotspot(608,433,393,283) action Return("math") alt "math"
        hotspot(154,434,442,278) action Return("logic") alt "logic"

label start:
        call screen map

        if _return=="geography":
            jump geography

        elif _return=="english":
            jump english

        elif _return=="russian":
            jump russian

        elif _return=="math":
            jump math

        elif _return=="logic":
            jump logic
