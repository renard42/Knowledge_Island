
define cat_russian = Character("Кот Учёный")


label russian:

    scene bg russian
    show cat russian at Position(xpos = 0.3, xanchor=0.3, ypos=0.5, yanchor=0.5)

    cat_russian "Приветствую тебя, путник!"
    show cat russian at left

    menu:

          cat_russian "Какой путь выбираешь?"

          "Налево по проторенной сказочной дорожке":

              jump rus_level0

          "Направо по тонкой песенной тропинке":

              jump rus_level1

          "Прямо через бурелом!":

              jump rus_level2

    label rus_level0:

        cat_russian "В сказках народная мудрость! Начнём!"
        jump start


    label rus_level1:

        cat_russian "С песней жить веселей!"
        jump start


    label rus_level2:

        cat_russian "Вперррёд через тернии к звёздам!"
        jump start

    jump start
