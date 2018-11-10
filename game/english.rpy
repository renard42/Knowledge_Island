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

    cat "Добро пожаловать!"

    cat "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"

    cat "С чего начнем?"

    show cat england at left with move
    menu:

        cat "Какой уровень пррредпочитаешь?"

        "Начнем с чего попроще":

            jump level0

        "А есть что-то среднее?":

            jump level1

        "Я уверен в себе! Давай самое сложное!":

            jump level2

    label level0:

        cat "Ну что ж, начнем с простого, мррр"

        $ num = int(renpy.input("Загадай число от 1 до 5: "))
        cat "Теперь я загадаю число от 1 до 5"

        $ num_cat = renpy.random.randint(1,5)
        cat "Твое число [num], а я загадал [num_cat]"
        if num == num_cat:
            cat "Ты угадал! Идем дальше?"

        else:
            cat "Я победил, деталька моя!"

        return

    label level1:

        cat "Среднее не значит скучное! Начнем! Мряв"
        return

    label level2:

        cat "Ты смелый игрок! Вперед, мррр :3"
        return
