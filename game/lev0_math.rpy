label level0_math:
    cat_math "Я уверен, что ты справишься!"
    menu:
        cat_math "Хочешь узнать, насколько хорошо ты считаешь?"

        "Я в этом профи!":
            jump game_math

        "Ээээ... Пойду-ка я отсюда":
            jump math_level

    label game_math:

        cat_math "Прррекрасно!"
        cat_math "Но сначала послушай правила"

        label arithmetic_rules:
            $ arithmetic_rule = renpy.file('/codes/arithmetic/rules.txt').read().split('\n')
            $ m = 0
            while arithmetic_rule[m]:
                $ renpy.say(cat_math, arithmetic_rule[m][:-1])
                $ m+=1

        menu:
            cat_math "Ты понял правила или хочешь послушать еще раз?"

            "Какие тут могут быть вопросы?":
                cat_math "И то верно!"
                jump arithmetic_game

            "А можешь повторить правила?":
                cat_math "Как пожелаете!"
                jump arithmetic_rules

        label arithmetic_game:
            cat_math "Ну что ж, начнем!"

            $ i = 0
            $ k = 10
            $ end = k-1
            $ arithmetic_life = 3

            while i < k:
                if i != 0:
                    cat_math "Поехали дальше!"
                python:
                    import random
                    arithmetic = renpy.file('/codes/arithmetic/operations.txt').read()
                    elements = arithmetic.split('\n')
                    operation = random.choice(elements)
                    first_number = random.randint(0, 100)
                    second_number = random.randint(0, 100)
                    if operation[:-1] == 'Умножение':
                        line = str(first_number) + ' * ' + str(second_number)
                        result = eval(line)
                        some_number = str(first_number) + ' * ?? = ' + str(result)
                        if first_number == 0 and result==0:
                            second_number = 0
                        know_how = 'Чтобы получить пропущенную переменную, тебе нужно было разделить ' + str(result) + ' на ' + str(first_number)
                    elif operation[:-1] == 'Деление':
                        first_number = random.randint(1, 100)
                        second_number = random.randint(1, 100)
                        line = str(first_number) + ' * ' + str(second_number)
                        result = eval(line)
                        some_number = str(result) + ' / ?? = ' + str(first_number)
                        know_how = 'Чтобы получить пропущенную переменную, тебе нужно было разделить ' + str(result) + ' на ' + str(first_number)
                    elif operation[:-1] == 'Вычитание':
                        if second_number>first_number:
                            second_number = random.randint(0, first_number)
                        line = str(first_number) + ' - ' + str(second_number)
                        result = eval(line)
                        some_number = str(first_number) + ' - ?? = ' + str(result)
                        know_how = 'Чтобы получить пропущенную переменную, тебе нужно было из ' + str(first_number) + ' вычесть ' + str(result)
                    else:
                        line = str(first_number) + ' + ' + str(second_number)
                        result = eval(line)
                        some_number = str(first_number) + ' + ?? = ' + str(result)
                        know_how = 'Чтобы получить пропущенную переменную, тебе нужно было из ' + str(result) + ' вычесть ' + str(first_number)
                init:
                    image white = "images/white.png"
                screen something:
                    hbox xalign 0.5 yalign 0.5:
                        text "[some_number]" size 45
                show white at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
                show screen something
                $ user_number = str(renpy.input("Какое число пропущено?"))
                if user_number==str(second_number):
                    if i<end:
                        cat_math "Молодец!"
                    else:
                        $ renpy.music.play(success, loop=False)
                        cat_math "Поздравляю! Ты прошел уровень!"
                        $ ship_status["math"]["1"] = True
                        hide white
                        hide screen something
                        menu:
                            cat_math "Хочешь сыграть еще раз?"

                            "Конечно!":
                                jump arithmetic_game

                            "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                                cat_math "До встречи! Заходи еще!"
                                jump math_level
                else:
                    $ arithmetic_life -= 1
                    if arithmetic_life==2:
                        cat_math "Непррррравильно! [know_how], поэтому правильный ответ [second_number]"
                        cat_math "У тебя еще [arithmetic_life] жизни"
                    elif arithmetic_life==1:
                        cat_math "Ну как же так? [know_how], поэтому правильный ответ [second_number]"
                        cat_math "У тебя еще [arithmetic_life] жизнь"
                    else:
                        cat_math "Непррррраввильный ответ! [know_how], поэтому правильный ответ [second_number]"
                        hide white
                        hide screen something
                        $ renpy.music.play(fail, loop=False)
                        cat_math "Я победил! Деталька моя"
                        menu:
                            cat_math "Хочешь сыграть еще раз?"

                            "Конечно!":
                                jump arithmetic_game
                            "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                                cat_math "До встречи! Заходи еще!"
                                jump math_level

                $ i += 1
                hide white
                hide screen something
                if i == k:
                    if arithmetic_life>0:
                        hide white
                        hide screen something
                        cat_math "Ты победил!"
                    menu:
                        cat_math "Хочешь сыграть еще раз?"

                        "Конечно!":
                            jump arithmetic_game
                        "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                            cat_math "До встречи! Заходи еще!"
                            jump math_level
