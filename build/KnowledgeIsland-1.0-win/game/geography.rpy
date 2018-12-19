define cat_geo = Character("Колумб")


label geography:

    scene bg geo
    show cat geo

    cat_geo "Добро пожаловать, странник!"

    show cat geo at right with move
    $ score = []

    label geo_level:
        #scene bg geo
        #show cat geo
        $ check_geo = list(ship_status["geo"].values())
        #cat_geo "[check_geo]"
        if False not in check_geo:
            if geo_status == False:
                $ geo_status = True
                init:
                    image p2 = "images/ship_piece2.png"
                show p2 at Position(xalign=0.5, yalign=0.5)
                cat_geo """
                Молодец, ты прошел все мои игры! Отдаю тебе детальку для твоего корабля.
                Удачи на других островах!
                """
                hide p2
                hide bg geo
                hide cat geo
                jump start
            else:
                menu:
                    cat_geo "Ты здесь уже был и получил деталь. Но может, ты очень сыграть еще раз?"
                    "Хочу!":
                        jump geo_menu
                    "Тогда я пойду дальше":
                        cat "Удачи!"
                        hide bg geo
                        hide cal geo
                        jump start

        label geo_menu:

            menu:

                cat_geo "Какой уровень пррредпочитаешь?"

                "Начнем с чего попроще":
                    $ i = 0
                    jump level0_geo

                "А есть что-то среднее?":
                    $ i = 0
                    jump level1_geo

                "Я уверен в себе! Давай самое сложное!":
                    $ i = 0
                    jump level2_geo
                "Хочу вернуться на карту":
                    jump start
