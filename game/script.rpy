screen map:
    imagemap:
        idle "images/Map_clean.png"
        hover "images/Map_labels.png"
        xfill True
        yfill True

        hotspot(357,0,400,228) action Return("english") alt "english"
        hotspot(701,251,316,223) action Return("geography") alt "geography"
        hotspot(89,229,382,235) action Return("russian") alt "russian"
        hotspot(675,475,399,242) action Return("math") alt "math"
        hotspot(247,477,418,240) action Return("logic") alt "logic"

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
