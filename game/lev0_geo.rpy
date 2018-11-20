init python:
    import random
    cities = renpy.file('/codes/cities/cities.txt').read()
    cities_db = [line.split(',')[0] for line in cities.split('\n')][1:]
    cities_info = {}
    for line in cities.split('\n')[1:101]:
        if len(line)>0:
            cities_info[line.split(',')[0]] = ','.join(line.split(',')[2:])
    cities_to_use = list(cities_info.keys())
    used_cities = []


label level0_geo:

    cat_geo "Что ж, начнем с разминки! :)"
    menu:
        cat_geo "Я предлагаю тебе поиграть в города. Что думаешь?"

        "Конечно!":
            jump game_cities

        "Не хочу. Давай другую игру!":
            jump geo_level

    label game_cities:

        $ player = False
        cat_geo "Прррекрасно, мяу! Тогда начнем!"
        cat_geo "Но сначала послушай правила игры:"

        label rules:
            $ rules = renpy.file('/codes/cities/rules.txt').read().split('\n')
            $ i = 0
            while rules[i]:
                $ renpy.say(cat_geo,rules[i][:-1])
                $ i+=1

            menu:
                cat_geo "Ты понял правила или хочешь послушать еще раз?"

                "Я все понял! Давай начинать!":
                    jump finally_game

                "А можно еще раз послушать правила? Я хочу быть уверен, что все запомнил":
                    cat_geo "Конечно, можно, мррр :3"
                    jump rules

            label finally_game:
                if player == False:
                    cat_geo "Отлично! Давай я начну, чтобы тебе было понятнее"
                else:
                    cat_geo "Отлично! Начинай!"

                $ count = 0
                $ life = 3

                while count <=10:
                    if player == False:
                        $ city = random.choice(cities_to_use)
                        $ del cities_to_use[cities_to_use.index(str(city))]
                        $ used_cities.append(city)
                        $ letter = [city[-1].upper(), city[-2].upper()]

                        cat_geo "Я называю город: [city]. Тебе на [letter[0]] или [letter[1]]."
                        $ player=True
                    elif player == True:
                        $ city = renpy.input("Назови город: ")
                        while city.title() not in cities_db and life!=0:
                            $ life -=1
                            cat_geo "Такого города [city] нет! У тебя осталось [life] попытки"
                            $ city = renpy.input("Назови город: ")
                        if letter:
                            while (letter[0]!=city[0].upper() and letter[1]!=city[0].upper()) and life!=0:
                                $ life -=1
                                cat_geo "Твой город [city] начинается на неправильную букву! У тебя осталось [life] попытки"
                                $ city = renpy.input("Назови город: ")


                        if life==0:
                            cat_geo "Ты проиграл, и детальку я тебе не отдам!\nИзучи карту и приходи снова!"
                            menu:
                                cat_geo "Или может, хочешь попробовать еще раз?"

                                "Да, я готов!":
                                    $ player = False
                                    jump finally_game
                                "Нет, я лучше еще потренируюсь и приду":
                                    cat_geo "До встречи, я буду тебя ждать!"
                                    jump start

                        $ del cities_to_use[cities_to_use.index(str(city))]
                        $ used_cities.append(city)
                        $ player=False


                    $ count+=1

                cat_geo "Ты победил! :3"
                cat_geo "Молодец! Я дарю тебе парус для твоего корабля!"
                $ score.append('level0')

                menu:
                    cat_geo "Хочешь сыграть еще раз?"

                    "Хочу! Ты первый!":
                        $ player = False
                        jump finally_game
                    "Хочу, только я называю первым!":
                        $ player = True
                        jump finally_game
                    "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                        cat_geo "До встречи, умный ребенок! заходит еще!"
                        jump start
