label level1_logic:
    sphynx "Я уверен, что ты справишься!"
    menu:
        sphynx "Хочешь поиграть в верю-не верю?"

        "Конечно!":
            jump game_logic

        "Может другое?":
            jump logic_level

    label game_logic:

        sphynx "Прррекрасно!"
        sphynx "Но сначала послушай правила"

        label yes_or_no_rules:
            $ yes_or_no_rule = renpy.file('/codes/yes_or_no/rules.txt').read().split('\n')
            $ m = 0
            while yes_or_no_rule[m]:
                $ renpy.say(sphynx, yes_or_no_rule[m][:-1])
                $ m+=1

        menu:
            sphynx "Ты понял правила или хочешь послушать еще раз?"

            "Какие тут могут быть вопросы?":
                sphynx "И то верно!"
                jump yes_or_no_game

            "А можешь повторить правила?":
                sphynx "Как пожелаете!"
                jump yes_or_no_rules

        label yes_or_no_game:
            sphynx "Ну что ж, начнем!"

            python:
                import random
                yesorno = renpy.file('/codes/yes_or_no/yes_or_no.txt').read()
                yesno = renpy.file('/codes/yes_or_no/yes_or_no_description.txt').read()
                elements = []
                for el in yesorno.split('\n'):
                    elements.append(tuple(el.split('\t')))
                final_el = {el[0]:el[1] for el in elements[:-1]}
                yesorno_questions = list(final_el.keys())
                elements = []
                for el in yesno.split('\n'):
                    elements.append(tuple(el.split('\t')))
                final_descr = {el[0]:el[1] for el in elements[:-1]}
                yesorno_answers = []
                yesorno_description = []
                random_questions = random.sample(yesorno_questions, 10)
                for i in random_questions:
                    yesorno_answers.append(final_el[i][:-1])
                for i in random_questions:
                    yesorno_description.append(final_descr[i][:-1])

            $ i = 0
            $ k = len(random_questions)
            $ end = k-1
            $ yesorno_life = 3
            $ yes = 'Да'
            $ no = 'Нет'


            while i < k:
                if i != 0:
                    sphynx "Поехали дальше!"
                $ new_question = random_questions[i]
                $ new_description = yesorno_description[i]
                $ new_answer = yesorno_answers[i]

                menu:
                    sphynx "[new_question]"

                    "[yes]":
                        $ answer = yes
                        jump yesorno_continue

                    "[no]":
                        $ answer = no
                        jump yesorno_continue

                label yesorno_continue:
                    if answer==new_answer:
                        if i<end:
                            sphynx "Молодец!"
                            if answer=='Нет':
                                sphynx "[new_description]"
                        else:
                            if answer=='Нет':
                                sphynx "Молодец! [new_description]"
                            sphynx "Поздравляю! Ты прошел уровень!"
                            menu:
                                sphynx "Хочешь сыграть еще раз?"

                                "Конечно!":
                                    jump yes_or_no_game
                                "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                                    sphynx "До встречи! Заходи еще!"
                                    hide bg pyrs
                                    hide sph
                                    jump start
                    else:
                        $ yesorno_life -= 1
                        if yesorno_life==2:
                            sphynx "Непррррравильно! [new_description]"
                            sphynx "У тебя еще [yesorno_life] жизни"
                        elif yesorno_life==1:
                            sphynx "Ну как же так? [new_description]"
                            sphynx "У тебя еще [yesorno_life] жизнь"
                        else:
                            sphynx "Непррррраввильный ответ! [new_description]"
                            sphynx "Я победил! Деталька моя"
                            menu:
                                sphynx "Хочешь сыграть еще раз?"

                                "Конечно!":
                                    jump yes_or_no_game
                                "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                                    sphynx "До встречи! Заходи еще!"
                                    hide bg pyrs
                                    hide sph
                                    jump start


                    $ i += 1

                if i == k:
                    if yesorno_life>0:
                        sphynx "Ты победил!"
                    menu:
                        sphynx "Хочешь сыграть еще раз?"

                        "Конечно!":
                            jump yes_or_no_game
                        "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                            sphynx "До встречи! Заходи еще!"
                            hide bg pyrs
                            hide sph
                            jump start
