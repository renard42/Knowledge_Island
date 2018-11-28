define cat_eng = Character("Шерлок")

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.
label english:


    scene bg england

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cat england

    # These display lines of dialogue.

    cat_eng "Добро пожаловать!"

    cat_eng "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"

    cat_eng "С чего начнем?"

    show cat england at left with move
    label eng_level:
        menu:

            cat_eng "Какой уровень пррредпочитаешь?"

            "Начнем с чего попроще":

                jump level0_eng

            "А есть что-то среднее?":

                jump level1_eng

            "Я уверен в себе! Давай самое сложное!":

                jump level2_eng
