label level0_geo:

    cat_geo "Что ж, начнем с разминки! :)"
    menu:
        cat_geo "Я предлагаю тебе поиграть в города. Что думаешь?"

        "Конечно!":
            jump game_cities

        "Не хочу. Давай другую игру!":
            jump geo_level

    label game_cities:

        cat_geo "Прррекрасно, мяу! Тогда начнем!"

        init python:
            import numpy as np
            import pandas as pd
            cities = pd.read_cvs('codes/cities/cities.csv')

        cat_geo "Но сначала послушай правила игры:"
        $ test = "Это тест"
        cat_geo "[test]"
