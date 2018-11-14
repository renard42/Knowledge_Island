define cat_math = Character("Пифагор")


label math:

    scene bg math
    show cat math

    cat_math "Здесь пока ничего нет, но мы скоро будем решать задачки!"

    show cat math at left with move

    init python:
        print("!")

    return
