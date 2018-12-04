define sphynx = Character("Сфинкс")

label logic:

    scene bg pyrs
    show sph

    sphynx "Добро пожаловать!"

    sphynx "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"

    sphynx "С чего начнем?"

    show sph at left with move
    label logic_level:
            menu:

                sphynx "Какой уровень пррредпочитаешь?"

                "Начнем с чего попроще":

                    jump level0_logic

                "А есть что-то среднее?":

                    jump level1_logic

                "Я уверен в себе! Давай самое сложное!":

                    jump level2_logic
