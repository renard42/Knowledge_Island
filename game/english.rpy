define cat_eng = Character("Шерлок")

label english:

    scene bg england
    show cat england

    cat "Добро пожаловать!"

    cat_eng "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"

    cat_eng "С чего начнем?"

    label eng_level:
        scene bg england
        show cat england
        $ check_eng = list(ship_status["eng"].values())
        if False not in check_eng:
            if eng_status == False:
                $ eng_status = True
                init:
                    image p1 = "images/ship_piece1.png"
                show p1 at Position(xalign=0.5, yalign=0.5)
                cat_eng """
                Молодец, ты прошел все мои игры! Отдаю тебе детальку для твоего корабля.
                Удачи на других островах!
                """
                hide p1
                hide bg england
                hide cat england
                window hide
<<<<<<< HEAD
                call start
=======
                jump start
>>>>>>> 920ed9e... u need more fixes
            else:
                menu:
                    cat_eng "Ты здесь уже был и получил деталь. Но может, ты очень сыграть еще раз?"
                    "Хочу!":
                        jump eng_menu
                    "Тогда я пойду дальше":
                        cat "Удачи!"
                        jump start



        label eng_menu:
            show cat england at left with move
            menu:

                cat_eng "Какой уровень пррредпочитаешь?"
                "Начнем с чего попроще":
                    jump level0_eng
                "А есть что-то среднее?":
                    jump level1_eng
                "Я уверен в себе! Давай самое сложное!":
                    jump level2_eng
                "Хочу вернуться на карту":
                    jump start
