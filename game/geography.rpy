define cat_geo = Character("Колумб")


label geography:

    scene bg geo
    show cat geo

    cat_geo "Добро пожаловать, странник!"


    show cat geo at right with move
    $ score = []

    label geo_level:

        menu:

            cat_geo "Какой уровень пррредпочитаешь?"

            "Начнем с чего попроще":

                jump level0_geo

            "А есть что-то среднее?":

                jump level1_geo

            "Я уверен в себе! Давай самое сложное!":

                jump level2_geo


        label level3_geo:

            cat_geo "Ты смелый игрок! Вперед, мррр :3"
            jump start
