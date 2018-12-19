label cities_help:
    $ info = cities_info[city][:-1].split('. ')
    $ player = True
    $ ind =0
    $ p1 = city +'.png'
    $ p2 = city + '_герб.png'
    init:
        image city_pic = "images/cities/[p1]"
        image gerb = "images/cities/[p2]"
    show city_pic at Position(xalign=0.8, yalign=0.2)
    show gerb at Position(xalign=0.85, yalign=0.2)
    while ind<len(info):
        $ renpy.say(owl,info[ind])
        $ ind+=1
    hide city_pic
    hide gerb

    jump continue_game

label skip_word:
    $ skip+=1
    jump game_game
    if skip == 3:
        cat_geo "Ты слишком часто пропускаешь города. Лучше изучи карту и вернись позже."
        jump geo_level
