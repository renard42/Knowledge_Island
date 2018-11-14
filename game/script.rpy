# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cat = Character("Шерлок")

screen map:
    imagemap:
        idle "images/Map_clean.jpg"
        hover "images/Map_labels.png"

        hotspot(748,234,1037,476) action Return("english") alt "english"
        hotspot(440,10,753,214) action Return("geography") alt "geography"
        hotspot(159,391,433,605) action Return("russian") alt "russian"
        hotspot(103,44,408,322) action Return("math") alt "math"
        hotspot(503,495,776,691) action Return("logic") alt "logic"

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
