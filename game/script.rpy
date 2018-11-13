# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cat = Character("Шерлок")

screen map:
    imagemap:
        idle "images/Map_clean.jpg"
        hover "images/Map_labels.png"

        hotspot(233,344,366,376) action Return("english") alt "english"
        hotspot(817,130,967,167) action Return("geography") alt "geography"
        hotspot(150,120,270,220) action Return("russian") alt "russian"
        hotspot(835,380,1040,450) action Return("math") alt "math"

label start:
        call screen map

        window show None

        if _return=="geography":
            jump geography

        elif _return=="english":
            jump english

        elif _return=="russian":
            jump russian

        elif _return=="math":
            jump math
