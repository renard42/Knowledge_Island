init python:
    import random
    stroka = renpy.file("/codes/countries/countries.txt").read()
    #with open("/codes/countries/countries.txt", "r") as f:
        #s = f.read()
    new_s = []
    for el in stroka.split('\n'):
        new_s.append(tuple(el.split('\t')))
    final = {el[0]:el[1] for el in new_s[:-1]}

    countries_to_use = list(final.keys())
    used = []
    info=[]
    for co in countries_to_use:
        info.append(final[co])




label level2_geo:

    cat_geo "Ты дошел до самого сложного уровня!"
    #cat_geo "[countries_to_use[0]]"
    #cat_geo "[info[0]]"
    menu:
        cat_geo "У каждой страны есть свой флаг. Давай проверим, знаешь ли ты их."

        "Я готов!":
            jump game_countries

        "Не хочу... Давай вернемся!":
            jump geo_level

    label game_countries:

        $ player = False

        $ i = 0
        $ num_err = 3

        while i<=4:
            $ country_new = random.choice(list(set(countries_to_use) - set(used)))
            $ used.append(country_new)
            init:
                image c = "images/[country_new].png"
            $ country_info = final[country_new].split('.')[:-1]

            show c at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5):
                zoom 3.0
            $ country = renpy.input("Угадай стрррррану:").title()
            hide c
            if country == country_new:
                if i < 4:
                    cat_geo "Молодец! Вот тебе немного информации:"
                    $ n = 0
                    while n<len(country_info):
                        $ renpy.say(cat_geo,country_info[n])
                        $ n+=1
                        #$ renpy.say(cat_geo, str(len(country_info)))
                    #$ renpy.say(cat_geo, country_info)
                else:
                    $ renpy.music.play(success, loop=False)
                    cat_geo "Уррррраа! Ты прошел уровень!"

                    $ship_status["geo"]["3"] = True

                    menu:
                        cat_geo "Хочешь сыграть еще раз?"

                        "Хочу! Давай повторим!":
                            jump finally_game
                        "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                            cat_geo "До встречи, умный ребенок!"
                            jump geo_level

            else:
                $ num_err -= 1
                if num_err==2:
                    cat_geo "Непррррравильно! Это [country_new]. У тебя еще [num_err] жизни"
                elif num_err==1:
                    cat_geo "Ну как же так? Это [country_new]. У тебя осталась всего [num_err] жизнь"
                else:
                    $ renpy.music.play(fail, loop=False)
                    menu:
                        cat_geo "Это [country_new], а ты проиграл, и детальку я тебе не отдам!\nИзучи карту и приходи снова! Или может, хочешь попробовать еще раз?"

                        "Да, я готов!":
                            $ player = False
                            jump game_countries
                            $ num_err = 3
                        "Нет, я лучше еще потренируюсь и приду":
                            cat_geo "До встречи, я буду тебя ждать!"
                            jump geo_level
            $ i += 1

            $ player=False
