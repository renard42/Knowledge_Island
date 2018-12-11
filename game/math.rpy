define cat_math = Character("Пифагор")


label math:

    scene bg math
    show cat math

    cat_math "Добро пожаловать!"

    cat_math "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"

    cat_math "С чего начнем?"

    show cat math at left with move
    label math_level:
            menu:

                cat_math "Какой уровень пррредпочитаешь?"

                "Начнем с чего попроще":

                    jump level0_math

                "А есть что-то среднее?":

                    jump level1_math

                "Я уверен в себе! Давай самое сложное!":

                    jump level2_math
