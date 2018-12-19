define owl_eng = Character("Owl", what_ysize = gui.textbox_height)
label level1_eng:
    cat_eng "Я уверен, что ты справишься!"
    menu:
        cat_eng "Сможешь угадать, как называются животные на английском по их описанию?"

        "Конечно!":
            jump game_eng

        "Может другое?":
            jump eng_level

    label game_eng:

        cat_eng "Прррекрасно!"
        cat_eng "Но сначала послушай правила"

        label animals_rules:
            #$ animal_rules = renpy.file('/codes/animals/rules.txt').read().split('\n')
            #$ m = 0
            #while animal_rules[m]:
                #$ renpy.say(cat_eng,animal_rules[m][:-1])
                #$ m+=1
            cat_eng """
            Тебе будет дано описание какого-то животного на английском.
            По нему ты должен будешь угадать наименование этого животного на английском.
            Если ты чего-то не поймешь, не волнуйся: в правом нижнем углу совушка переведет описание на русский язык.
            """

        menu:
            cat_eng "Ты понял правила или хочешь послушать еще раз?"

            "У матросов нет вопросов!":
                jump game_animal

            "А можешь повторить правила?":
                cat_eng "Конечно, мррр :3"
                jump animals_rules

        label game_animal:
            cat_eng "Ну что ж, начнем!"

            python:
                import random
                animals = renpy.file('/codes/animals/animals.txt').read()
                animals_rus = renpy.file('/codes/animals/animals_rus.txt').read()
                animal = []
                animal_rus = []
                for el in animals.split('\n'):
                    animal.append(tuple(el.split('\t')))
                final = {el[0]:el[1] for el in animal[:-1]}
                animals_to_use = list(final.keys()) #список животных на английском
                for el in animals_rus.split('\n'):
                    animal_rus.append(tuple(el.split('\t')))
                final_rus = {el[0]:el[1] for el in animal_rus[:-1]}
                random_animals_eng = []
                random_animals_rus = []
                random_animals = random.sample(animals_to_use, 5)
                for i in random_animals:
                    random_animals_eng.append(final[i])
                for i in random_animals:
                    random_animals_rus.append(final_rus[i])

            $ i = 0
            $ k = len(random_animals)
            $ end = k-1
            $ animal_life = 3
            $ num = 3


            while i < k:
                if i != 0:
                    cat_eng "Поехали дальше!"
                $ new_animal = random_animals[i].lower()

                init:
                    image given_animal = "images/animals/[new_animal].png"
                $ new_animal_descr_eng = random_animals_eng[i].split('.')
                $ n = 0
                screen game_eng_buttons:
                    hbox xalign 1.0 yalign 1.0:
                        imagebutton auto ("owl_eng_%s.png") action Jump("animals_help")
                        #textbutton "{b}{color=#6699FF}Не знаю :({/b}{/color}" action Jump("skip_word")
                show screen game_eng_buttons

                while n<len(new_animal_descr_eng)-1:
                    $ renpy.say(cat_eng,new_animal_descr_eng[n])
                    $ n+=1
                label continue_animals:
                $ user_animal = str(renpy.input("Как называется это животное на английском?").lower())
                if user_animal==new_animal:
                    show given_animal at Position(xpos = 0.60, xanchor=0.3, ypos=0.2, yanchor=0.2)
                    if i<end:
                        cat_eng "Молодец!"
                        hide given_animal
                    else:
                        $ renpy.music.play(success, loop=False)
                        cat_eng "Поздравляю! Ты прошел уровень!"
                        hide given_animal
                        menu:
                            cat_eng "Хочешь сыграть еще раз?"

                            "Конечно!":
                                $ ship_status["eng"]["2"] = True
                                jump game_animal
                            "Извини, но я пойду дальше - мне еще нужно в другие игры поиграть":
                                cat_eng "До встречи! Заходи еще!"
                                $ ship_status["eng"]["2"] = True
                                hide screen game_eng_buttons
                                jump eng_level
                else:
                    show given_animal at Position(xpos = 0.60, xanchor=0.3, ypos=0.2, yanchor=0.2)
                    if i == k-1:
                        if animal_life>0:
                            cat_eng "This is a [new_animal]! Хоть ты и ошибся, но ты все равно победил!"
                            $ ship_status["eng"]["2"] = True
                            hide given_animal
                        menu:
                            cat_eng "Хочешь сыграть еще раз?"

                            "Конечно!":
                                jump game_animal
                            "Извини, но я пойду дальше - мне еще нужно в другие игры поиграть":
                                cat_eng "До встречи! Заходи еще!"
                                hide screen game_eng_buttons
                                jump eng_level
                    $ animal_life -= 1
                    if animal_life==2:
                        cat_eng "Непррррравильно! This is a [new_animal]! У тебя еще [animal_life] жизни"
                        cat_eng "Нажми на сову снизу и посмотри на перевод. Должно стать понятнее!"
                    elif animal_life==1:
                        cat_eng "Ну как же так? This is a [new_animal]! У тебя еще [animal_life] жизнь"
                        cat_eng "Нажми на сову снизу и посмотри на перевод. Должно стать понятнее!"
                    else:
                        cat_eng "This is a [new_animal]!"
                        cat_eng "Нажми на сову снизу и посмотри на перевод. Должно стать понятнее!"
                        hide given_animal
                        $ renpy.music.play(fail, loop=False)
                        cat_eng "Я победил! Деталька моя"
                        menu:
                            cat_eng "Хочешь сыграть еще раз?"

                            "Конечно!":
                                jump game_animal
                            "Извини, но я пойду дальше - мне еще нужно в другие игры поиграть":
                                cat_eng "До встречи! Заходи еще!"
                                hide screen game_eng_buttons
                                jump eng_level

                label continue_animal:
                    $ num = animal_life
                hide given_animal
                $ i += 1
