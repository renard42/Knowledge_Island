init python:
    store.ship_status = {"geo":{"1":False,"2":False,"3":False}, "math":{"1":False,"2":False,"3":False}, "eng":{"1":False,"2":False,"3":False}, "logic":{"1":False,"2":False,"3":False}}
    w = None
    eng_status = False
    geo_status = False
    math_status = False
    logic_status = False

define owl = Character("Сова")
screen map:
    imagemap:
        idle "images/Map_clean.png"
        hover "images/Map_labels.png"
        xfill True
        yfill True

        hotspot(388,3,416,204) action Return("english") alt "english"
        hotspot(750,204,348,216) action Return("geography") alt "geography"
        hotspot(96,204,404,208) action Return("russian") alt "russian"
        hotspot(709,424,423,280) action Return("math") alt "math"
        hotspot(251,419,463,257) action Return("logic") alt "logic"

    hbox xalign 1.0 yalign 1.0:
        imagebutton auto ("owl_help_%s.png") action Return("status")

label start:
    call screen map
    scene map bg
    $b = []
    $temp = [b.extend(list(i.values())) for i in ship_status.values()]

    if False not in b:
        $ w = True

    if w == True:
        init:
            image ship = "images/ship.png"
        scene map bg
        show ship at Position(xalign=0.5, yalign=0.5)
        owl """
        Ты победил! Вот твой корабль.
        Вперед, за новыми знаниями!
        """
        show ship at right with move
        $ renpy.full_restart(transition=False, label='_invoke_main_menu', target='_main_menu')

    if _return=="status":
        $ locs = {"geo":"Географии", "math":"Математики", "eng":"Английского языка", "logic":"Логики"}
        $ not_done = [locs[n] for n in ship_status.keys() if False in ship_status[n].values()]

        if len(not_done)>0:
            $ left = ', '.join(not_done)
            owl "Ты собрал еще не все детали! Остались игры на островах [left]"
            #hide map bg
            jump start


    if _return=="geography":
        hide screen status_owl
        jump geography

    elif _return=="english":
        hide screen status_owl
        jump english

    elif _return=="russian":
        hide screen status_owl
        jump russian

    elif _return=="math":
        hide screen status_owl
        jump math

    elif _return=="logic":
        hide screen status_owl
        jump logic
