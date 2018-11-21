label level1_geo:

    menu:
        cat_geo "Хочешь поиграть в ассоциации?"

        "Поехали!":
            jump game_pics

        "Может другое?":
            jump geo_level

    label game_pics:
        init:
            $ num_err = 3
            $ countries = ["ukraine", "sweden", "iceland", "china", "india", "canada", "australia", "usa", "italy", "russia", "egypt", "japan", "uk", "france"]
            $ i = 0
            $ country_new = ''
            $ countries_dict = {"ukraine": "украина", "sweden": "швеция", "iceland": "исландия", "china": ["китай", "кнр"], "india": "индия", "canada": "канада", "australia": "австралия", "france": "франция", "usa": ["америка", "сша"], "italy": "италия", "russia": ["россия", "рф", "российская федерация"], "egypt": "египет", "japan": "япония", "uk": ["англия", "британия", "великобритания"]}

        show cat geo at left with move
        cat_geo "Среднее не значит скучное! Начнем! Мряв"
        $ random_countries = renpy.random.sample(countries, 5)
        while i<5:
            $ country_new = random_countries[i]
            init:
                image num1 = "images/[country_new]/num1.png"
                image num2 = "images/[country_new]/num2.png"
                image num3 = "images/[country_new]/num3.png"
                image num4 = "images/[country_new]/num4.png"
            show num1 at Position(xpos = 0.45, xanchor=0.3, ypos=0.2, yanchor=0.5)
            show num2 at Position(xpos = 0.45, xanchor=0.3, ypos=0.55, yanchor=0.5)
            show num3 at Position(xpos = 0.65, xanchor=0.3, ypos=0.55, yanchor=0.5)
            show num4 at Position(xpos = 0.65, xanchor=0.3, ypos=0.2, yanchor=0.5)
            $ country = str(renpy.input("Угадай стрррррану:").lower())
            if country in countries_dict[country_new]:
                if i < 4:
                    cat_geo "Молодец! Давай еще?"
                else:
                    cat_geo "Уррррррраа! Ты прошел уровень!"

            else:
                $ num_err -= 1
                if num_err==2:
                    cat_geo "Непррррравильно! У тебя еще [num_err] жизни"
                elif num_err==1:
                    cat_geo "Ну как же так? У тебя еще [num_err] жизнь"
                else:
                    cat_geo "Я победил! Деталька моя"
                    jump geo_level
            $ i += 1

        jump start
