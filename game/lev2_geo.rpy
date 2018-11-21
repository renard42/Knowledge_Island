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
        cat_geo "Отлично! Давай начнём!"

        $ i = 0
        $ life = 3

        while i<=9:
            $ country_new = random.choice(countries_to_use)
            init:
                image c = "images/[country_new].png"
            $ country_info = final[country_new].split('.')[:-1]

            show c at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5):
                zoom 3.0
            $ country = renpy.input("Угадай стрррррану:").title()
            if country == country_new:
                if i < 9:
                    cat_geo "Молодец! Вот тебе немного информации:"
                    $ n = 0
                    while n<len(country_info):
                        $ renpy.say(cat_geo,country_info[n])
                        $ n+=1
                        #$ renpy.say(cat_geo, str(len(country_info)))
                    #$ renpy.say(cat_geo, country_info)
                else:
                    cat_geo "Уррррраа! Ты прошел уровень!"

                    $ score.append('level2')
                    if len(score)==3:
                        cat_geo "Молодец! Я дарю тебе мачту для твоего корабля!"

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

            else:
                $ num_err -= 1
                if num_err==2:
                    cat_geo "Непррррравильно! У тебя еще [num_err] жизни"
                elif num_err==1:
                    cat_geo "Ну как же так? У тебя еще [num_err] жизнь"
                else:
                    cat_geo "Ты проиграл, и детальку я тебе не отдам!\nИзучи карту и приходи снова!"
                    menu:
                        cat_geo "Или может, хочешь попробовать еще раз?"

                        "Да, я готов!":
                            $ player = False
                            jump finally_game
                        "Нет, я лучше еще потренируюсь и приду":
                            cat_geo "До встречи, я буду тебя ждать!"
                            jump start
            $ i += 1

            $ player=False
