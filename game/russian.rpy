define cat_russian = Character("Кот Учёный")


label russian:

    scene bg russian
    show cat russian

    cat_russian "Приветствую тебя, путник!"

    show cat russian at right with move

    menu:

          cat "Какой путь выбираешь?"

          "Налево по проторенной сказочной дорожке":

              jump level0

          "Направо по тонкой песенной тропинке":

              jump level1

          "Прямо через бурелом!":

              jump level2

    label rus_level1:

        cat "В сказках народная мудрость! Начнём!"
        return


    label rus_level0:

        cat "Скорррей за мной!"
        return


    label rus_level2:

        cat "Вперррёд через тернии к звёздам!"
        return

    return
