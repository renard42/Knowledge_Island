define sphynx = Character("Сфинкс")

label logic:

    scene bg pyrs
    show sph


    sphynx "Добро пожаловать!"

    sphynx "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"



    label logic_level:

        scene bg pyrs
        hide sph
        show sph at left with move
        $ check_logic = list(ship_status["logic"].values())
        if False not in check_logic:
            if logic_status == False:
                $ logic_status = True
                init:
                    image p3 = "images/ship_piece3.png"
                show p3 at Position(xalign=0.5, yalign=0.5)
                sphynx """
                Молодец, ты прошел все мои игры! Отдаю тебе детальку для твоего корабля.
                Удачи на других островах!
                """
                hide p3
                hide bg pyrs
                hide sph
                jump start
            else:
                menu:
                    sphynx "Ты здесь уже был и получил деталь. Но может, ты очень сыграть еще раз?"
                    "Хочу!":
                        jump logic_menu
                    "Тогда я пойду дальше":
                        cat "Удачи!"
                        hide bg pyrs
                        hide sph
                        jump start
    label logic_menu:
            menu:

                sphynx "Какой уровень пррредпочитаешь?"

                "Начнем с чего попроще":

                    jump level0_logic

                "А есть что-то среднее?":

                    jump level1_logic

                "Я уверен в себе! Давай самое сложное!":

                    jump level2_logic
                "Хочу вернуться на карту":
                    hide bg pyrs
                    hide sph
                    jump start
