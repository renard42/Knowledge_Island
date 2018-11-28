label level1_geo:

    menu:
        cat_geo "Хочешь поиграть в ассоциации?"

        "Поехали!":
            jump fourpics

        "Может другое?":
            jump geo_level

    label fourpics:
        cat_geo "Для начала я расскажу тебе о правилах игры"

        label fourpics_rules:
            $ fourpic_rules = renpy.file('/codes/fourpics/rules.txt').read().split('\n')
            $ m = 0
            while fourpic_rules[m]:
                $ renpy.say(cat_geo, fourpic_rules[m][:-1])
                $ m+=1

            menu:
                cat_geo "Ты понял правила или хочешь послушать еще раз?"

                "Готов играть!":
                    jump game_pics

                "А можешь повторить правила?":
                    cat_geo "Конечно!"
                    jump fourpics_rules


            label game_pics:

                $ fourpics_life = 3
                $ countries = ["Мексика", "Украина", "Швеция", "Исландия", "Китай", "Индия", "Канада", "Австралия", "США", "Италия", "Россия", "Египет", "Япония", "Великобритания", "Франция"]
                $ i = 0
                $ countries_dict = {"Мексика": ["мексика"], "Украина": ["украина"], "Швеция": ["швеция"], "Исландия": ["исландия"], "Китай": ["китай", "кнр"], "Индия": ["индия"], "Канада": ["канада"], "Австралия": ["австралия"], "Франция": ["франция"], "США": ["америка", "сша"], "Италия": ["италия"], "Россия": ["россия", "рф", "российская федерация"], "Египет": ["египет"], "Япония": ["япония"], "Великобритания": ["англия", "британия", "великобритания"]}

                show cat geo at left with move
                cat_geo "Начнем же!"
                $ random_countries = renpy.random.sample(countries, 5)
                while i<5:
                    $ fourpics_country = random_countries[i]
                    init:
                        image num1 = "images/[fourpics_country]/num1.png"
                        image num2 = "images/[fourpics_country]/num2.png"
                        image num3 = "images/[fourpics_country]/num3.png"
                        image num4 = "images/[fourpics_country]/num4.png"
                        image num5 = "images/[fourpics_country]/num5.png"
                    $ file_path = 'images/' + str([fourpics_country][0]) + '/country.txt'
                    $ new_info = renpy.file(file_path).readlines()


                    show num1 at Position(xpos = 0.45, xanchor=0.3, ypos=0.2, yanchor=0.5)
                    show num2 at Position(xpos = 0.45, xanchor=0.3, ypos=0.55, yanchor=0.5)
                    show num3 at Position(xpos = 0.65, xanchor=0.3, ypos=0.55, yanchor=0.5)
                    show num4 at Position(xpos = 0.65, xanchor=0.3, ypos=0.2, yanchor=0.5)
                    $ user_country = str(renpy.input("Угадай стрррррану:").lower())
                    show num5 at Position(xpos = 0.85, xanchor=0.3, ypos=0.4, yanchor=0.6):
                        zoom 2.0

                    if user_country in countries_dict[fourpics_country]:
                        if i < 4:
                            cat_geo "Молодец! Вот тебе информация:"
                            $ n = 0
                            while n<len(new_info):
                                $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                                $ n+=1
                            cat_geo "Давай еще?"
                        else:
                            cat_geo "Молодец! Вот тебе информация:"
                            $ n = 0
                            while n<len(new_info):
                                $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                                $ n+=1
                            cat_geo "Уррррррраа! Ты прошел уровень!"
                            hide num1
                            hide num2
                            hide num3
                            hide num4
                            hide num5
                            menu:
                                cat_geo "Хочешь сыграть еще раз?"
                                "Конечно!":
                                    jump game_pics
                                "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                                    cat_geo "До встречи! Заходи еще, юный географ!"
                                    hide bg geo
                                    hide cat geo
                                    jump start

                    else:
                        $ fourpics_life -= 1
                        if fourpics_life==2:
                            cat_geo "Непррррравильно! Это [fourpics_country]! У тебя еще [fourpics_life] жизни"
                            cat_geo "Давай разеберем картинки!"
                            $ n = 0
                            while n<len(new_info):
                                $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                                $ n+=1
                        elif fourpics_life==1:
                            cat_geo "Ну как же так? Это [fourpics_country]! У тебя еще [fourpics_life] жизнь"
                            cat_geo "Давай разеберем картинки!"
                            $ n = 0
                            while n<len(new_info):
                                $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                                $ n+=1
                        else:
                            cat_geo "Это [fourpics_country]!"
                            cat_geo "Давай разеберем картинки!"
                            $ n = 0
                            while n<len(new_info):
                                $ renpy.say(cat_geo,new_info[n][:1 + new_info[n].rfind('.')])
                                $ n+=1
                            cat_geo "Я победил! Деталька моя"
                            hide num1
                            hide num2
                            hide num3
                            hide num4
                            hide num5

                            menu:
                                cat_geo "Хочешь сыграть еще раз?"
                                "Конечно!":
                                    jump game_pics
                                "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                                    cat_geo "До встречи! Заходи еще, юный географ!"
                                    hide bg geo
                                    hide cat geo
                                    jump start
                    hide num5
                    $ i += 1
