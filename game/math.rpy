define cat_math = Character("Пифагор")


label math:

    scene bg math
    show cat math

    cat_math "Добро пожаловать!"

    cat_math "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"

    label math_level:

        scene bg math
        show cat math
        hide cat math
        show cat math at left
        $ check_math = list(ship_status["math"].values())
        if False not in check_math:
            if math_status == False:
                $ math_status = True
                init:
                    image p4 = "images/ship_piece4.png"
                show p4 at Position(xalign=0.5, yalign=0.5)
                cat_math """
                Молодец, ты прошел все мои игры! Отдаю тебе детальку для твоего корабля.
                Удачи на других островах!
                """
                hide p4
                hide bg math
                hide cat math
                jump start
            else:
                menu:
                    cat_math "Ты здесь уже был и получил деталь. Но может, ты очень сыграть еще раз?"
                    "Хочу!":
                        jump math_menu
                    "Тогда я пойду дальше":
                        cat "Удачи!"
                        hide bg math
                        hide cat math
                        jump start
    label math_menu:
            menu:

                cat_math "Какой уровень пррредпочитаешь?"

                "Начнем с чего попроще":

                    jump level0_math

                "А есть что-то среднее?":

                    jump level1_math

                "Я уверен в себе! Давай самое сложное!":

                    jump level2_math
                "Хочу вернуться на карту":
                    jump start
