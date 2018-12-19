init python:
    import random
    cities = renpy.file('/codes/cities/cities.txt').read()
    cities_db = [line.split(',')[0] for line in cities.split('\n')]
    cities_info = {}
    for line in cities.split('\n')[:101]:
        if len(line)>0:
            cities_info[line.split(',')[0]] = ','.join(line.split(',')[2:])
    cities_to_use = list(cities_info.keys())
    random.shuffle(cities_to_use)

define owl = Character("Сова", what_ysize = gui.textbox_height)
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
        cat_geo "Прррекрасно, мяу!"
        cat_geo "Но сначала послушай правила"
        show cat geo at left with move

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
            $ used_cities = []
            $ letter = False
            $ city = False
            if player == False:
                cat_geo "Отлично! Давай я начну, чтобы тебе было понятнее"
            else:
                cat_geo "Отлично! Начинай!"

            $ count = 0
            $ geo0_life = 3
            screen game_buttons:
                hbox xalign 1.0 yalign 1.0:
                    imagebutton auto ("owl_help_%s.png") action Jump("cities_help")
                    #textbutton "{b}{color=#6699FF}Не знаю :({/b}{/color}" action Jump("skip_word")
            show screen game_buttons
            while count<20:
                if player == False:
                    if letter:
                        $ k = 0
                        while k<len(cities_to_use):
                            if letter[0] == cities_to_use[k][0].upper() or letter[1] == cities_to_use[k][0].upper():
                                $ city = cities_to_use[k]
                                $ k=len(cities_to_use)
                            $ k+=1
                        if not city:
                            cat_geo "Я не знаю больше городов на [letter]."
                            jump geo_win
                    else:
                        $ city = random.choice(cities_to_use).title()

                    $ del cities_to_use[cities_to_use.index(str(city))]
                    $ used_cities.append(city)
                    $ letter = [city[-1].upper(), city[-2].upper()]

                    cat_geo "Я называю город: [city]. Тебе на [letter[0]] или [letter[1]]."
                    label continue_game:
                        $ player = True
                    $ player=True

                elif player == True:
                    $ city = renpy.input("Назови город: ").title()
                    while city.title() not in cities_db and geo0_life!=0:
                        $ geo0_life -=1
                        cat_geo "Такого города [city] нет! У тебя осталось [geo0_life] попытки"
                        $ city = renpy.input("Назови город: ").title()
                    if letter:
                        while (letter[0]!=city[0].upper() and letter[1]!=city[0].upper()) and geo0_life!=0:
                            $ geo0_life -=1
                            cat_geo "Твой город [city] начинается на неправильную букву! У тебя осталось [geo0_life] попытки"
                            $ city = renpy.input("Назови город: ")
                    while city in used_cities:
                        cat_geo "Город [city] уже был. Назови другой"
                        $ city = renpy.input("Назови город: ")

                    if geo0_life==0:
                        $ renpy.music.play(fail, loop=False)
                        cat_geo "Ты проиграл, и детальку я тебе не отдам!\nИзучи карту и приходи снова!"
                        menu:
                            cat_geo "Или может, хочешь попробовать еще раз?"

                            "Да, я готов!":
                                $ player = False
                                jump finally_game
                            "Нет, я лучше еще потренируюсь и приду":
                                cat_geo "До встречи, я буду тебя ждать!"
                                jump geo_level
                    init python:
                        try:
                            del cities_to_use[cities_to_use.index(str(city))]
                        except:
                            pass
                    $ letter = [city[-1].upper(), city[-2].upper()]
                    $ used_cities.append(city)
                    $ player=False

                $ count+=1

            label geo_win:
                $ renpy.music.play(success, loop=False)
                hide game_buttons
                cat_geo "Ты победил! :3"
                cat_geo "Молодец! Идем дальше?"
                $ score.append('level0')
                $ ship_status["geo"]["1"] = True

                menu:
                    cat_geo "Хочешь сыграть еще раз?"

                    "Хочу!":
                        $ player = False
                        jump finally_game
                    "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                        cat_geo "До встречи! Заходи еще!"
                        hide screen game_buttons
                        jump geo_level
