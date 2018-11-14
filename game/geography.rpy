define cat_geo = Character("Колумб")


label geography:

    scene bg geo
    show cat geo

    cat_geo "Добро пожаловать, странник!"


    show cat geo at right with move

    menu:

        cat_geo "Какой уровень пррредпочитаешь?"

        "Начнем с чего попроще":

            jump level3

        "А есть что-то среднее?":

            jump level4

        "Я уверен в себе! Давай самое сложное!":

            jump level5


    label level3:

        cat_geo "Ну что ж, начнем с простого, мррр"


        jump start

    label level4:
        show cat geo at left with move
        cat_geo "Среднее не значит скучное! Начнем! Мряв"

        show ben at Position(xpos = 0.45, xanchor=0.3, ypos=0.2, yanchor=0.5)
        show tea at Position(xpos = 0.45, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show monarchy at Position(xpos = 0.65, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show stonehedge at Position(xpos = 0.65, xanchor=0.3, ypos=0.2, yanchor=0.5)
        $ country = str(renpy.input("Угадай стрррррану:"))
        if country == "Великобритания" or country == "Англия" :
            cat_geo "Ты угадал! Давай еще?"

        else:
            cat_geo "Я победил, деталька моя!"


        show boot at Position(xpos = 0.45, xanchor=0.3, ypos=0.2, yanchor=0.5)
        show pasta at Position(xpos = 0.45, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show piza at Position(xpos = 0.65, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show pizza at Position(xpos = 0.65, xanchor=0.3, ypos=0.2, yanchor=0.5)
        $ country = str(renpy.input("Угадай стрррррану:"))
        if country == "Италия":
            cat_geo "Ты угадал! Идем дальше?"

        else:
            cat_geo "Я победил, деталька моя!"


        show balalaika at Position(xpos = 0.45, xanchor=0.3, ypos=0.2, yanchor=0.5)
        show borsch at Position(xpos = 0.45, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show snowflake at Position(xpos = 0.65, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show kremlin at Position(xpos = 0.65, xanchor=0.3, ypos=0.2, yanchor=0.5)
        $ country = str(renpy.input("Угадай стрррррану:"))
        if country == "Россия":
            cat_geo "Ты угадал! Идем дальше?"

        else:
            cat_geo "Я победил, деталька моя!"

        show sun at Position(xpos = 0.45, xanchor=0.3, ypos=0.2, yanchor=0.5)
        show samurai at Position(xpos = 0.45, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show sakura at Position(xpos = 0.65, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show robot at Position(xpos = 0.65, xanchor=0.3, ypos=0.2, yanchor=0.5)
        $ country = str(renpy.input("Угадай стрррррану:"))
        if country == "Япония":
            cat_geo "Ты угадал! Идем дальше?"

        else:
            cat_geo "Я победил, деталька моя!"

        show pyramid at Position(xpos = 0.45, xanchor=0.3, ypos=0.2, yanchor=0.5)
        show pharaoh at Position(xpos = 0.45, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show kitty at Position(xpos = 0.65, xanchor=0.3, ypos=0.55, yanchor=0.5)
        show camel at Position(xpos = 0.65, xanchor=0.3, ypos=0.2, yanchor=0.5)
        $ country = str(renpy.input("Угадай стрррррану:"))
        if country == "Египет":
            cat_geo "Ты прошел урррровень! Молодец!"

        else:
            cat_geo "Я победил, деталька моя!"

        jump start

    label level5:

        cat_geo "Ты смелый игрок! Вперед, мррр :3"
        jump start
