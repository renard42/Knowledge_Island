label cities_help:
    $ info = cities_info[city][:-1].split('.')
    $ player = True
    $ ind =0
    while info[ind]:
        $ renpy.say(owl,info[ind])
        $ ind+=1

    jump continue_game

label skip_word:
    $ skip+=1
    jump game_game
    if skip == 3:
        cat_geo "Ты слишком часто пропускаешь города. Лучше изучи карту и вернись позже."
        jump geo_level
