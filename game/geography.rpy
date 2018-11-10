define cat_geo = Character("Колумб")


label geography:

    scene bg geo
    show cat geo

    cat_geo "Здесь пока ничего нет, но мы уже в пути!"

    show cat geo at right with move

    init python:
        print("!")

    return
