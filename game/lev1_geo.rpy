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
            $ countries = ["Мексика", "Украина", "Швеция", "Исландия", "Китай", "Индия", "Канада", "Австралия", "США", "Италия", "Россия", "Египет", "Япония", "Великобритания", "Франция"]
            $ i = 0
            $ country_new = ''
            $ countries_dict = {"Мексика": "мексика", "Украина": "украина", "Швеция": "швеция", "Исландия": "исландия", "Китай": ["китай", "кнр"], "Индия": "индия", "Канада": "канада", "Австралия": "австралия", "Франция": "франция", "США": ["америка", "сша"], "Италия": "италия", "Россия": ["россия", "рф", "российская федерация"], "Египет": "египет", "Япония": "япония", "Великобритания": ["англия", "британия", "великобритания"]}

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
                image num5 = "images/[country_new]/num5.png"
            $ file_path = 'images/' + str([country_new][0]) + '/country.txt'
            $ new_info = renpy.file(file_path).readlines()


            show num1 at Position(xpos = 0.45, xanchor=0.3, ypos=0.2, yanchor=0.5)
            show num2 at Position(xpos = 0.45, xanchor=0.3, ypos=0.55, yanchor=0.5)
            show num3 at Position(xpos = 0.65, xanchor=0.3, ypos=0.55, yanchor=0.5)
            show num4 at Position(xpos = 0.65, xanchor=0.3, ypos=0.2, yanchor=0.5)
            $ country = str(renpy.input("Угадай стрррррану:").lower())
            show num5 at Position(xpos = 0.85, xanchor=0.3, ypos=0.4, yanchor=0.6):
                zoom 2.0

            if country in countries_dict[country_new]:
                if i < 4:
                    cat_geo "Молодец! Вот тебе информация:"
                    $ n = 0
                    while n<len(new_info):
                        $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                        $ n+=1
                    cat_geo "Давай еще?"
                else:
                    $ n = 0
                    while n<len(new_info):
                        $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                        $ n+=1
                    cat_geo "Уррррррраа! Ты прошел уровень!"

            else:
                $ num_err -= 1
                if num_err==2:
                    cat_geo "Непррррравильно! Это [country_new]! У тебя еще [num_err] жизни"
                    cat_geo "Давай разеберем картинки!"
                    $ n = 0
                    while n<len(new_info):
                        $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                        $ n+=1
                elif num_err==1:
                    cat_geo "Ну как же так? Это [country_new]! У тебя еще [num_err] жизнь"
                    cat_geo "Давай разеберем картинки!"
                    $ n = 0
                    while n<len(new_info):
                        $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                        $ n+=1
                else:
                    cat_geo "Это [country_new]!"
                    cat_geo "Давай разеберем картинки!"
                    $ n = 0
                    while n<len(new_info):
                        $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                        $ n+=1
                    cat_geo "Я победил! Деталька моя"
                    hide num5
                    jump geo_level
            hide num5
            $ i += 1

        jump start
