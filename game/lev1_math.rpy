define cat_math = Character("Пифагор")

init python:
    import random
    card_size = 48
    wait = 0.5
    f = renpy.file('images/figures/tasks.txt').read().split('\n')

    mistakes = 3

screen figure_scr:
    grid 2 2:
        align (.5, .5)
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                add card["value"]
                action Return(card["correct"])

label figures_game:
    init python:
        store.used = []
    label figures_turns_loop:
        while r!=5:
            python:
                cards_list = []
                task = random.choice(f)
                while task in used:
                    task = random.choice(f)
                used.append(task)
                store.task, store.imgs, store.correct = task.split(';')
                imgs = imgs.split(',')
                for i in range (0, len(imgs)):
                    if imgs[i].split('.')[0] == correct.split('.')[0]:
                        cards_list.append ( {"value": "/images/figures/"+imgs[i], "correct":True} )
                    else:
                        cards_list.append ( {"value": "/images/figures/"+imgs[i], "correct":False} )
            show screen figure_scr
            $ renpy.say(cat_math,task)
            $ result2 = ui.interact()
            $ r+=1
            while result2!=True and mistakes!=0:
                $ mistakes -=1
                cat_math "Неправильно! У тебя осталось попыток: [mistakes]. Попробуй еще раз!"
                $ renpy.say(cat_math,task)
                $ result2 = ui.interact()
            if mistakes == 0:
                jump figure_lose
            if result2 == True and r!=5:
                cat_math "Правильно! Слушай следующий вопрос."

        if mistakes == 0:
            jump figure_lose
        elif r == 5:
            jump figure_win


label figure_lose:
    hide screen figure_scr
    $ renpy.pause (0.1, hard = True)
    menu:
        cat_math "Ты проиграл! Хочешь попробовать еще раз?"

        "Хочу!":
            $ r = 0
            $mistakes = 3
            jump figures_game
        "Лучше еще потренируюсь и приду.":
            cat_math "Возвращайся, буду ждать!"
            jump math_level

label figure_win:
    hide screen figure_scr
    $ renpy.pause (0.1, hard = True)
    $ ship_status["math"]["2"] = True
    menu:
        cat_math "Ты выиграл! Хочешь сыграть еще раз или пойдешь дальше?"
        "Давай!":
            $ r = 0
            $mistakes = 3
            jump figures_game
        "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
            cat_math "До встречи!"
            jump math_level

label level1_math:
    scene bg math
    show cat math at right

    menu:
        cat_math "Я предлагаю тебе поиграть с фигурами. Что думаешь?"
        "Согласен, начнем!":
            cat_math "Отлично! Давай я расскажу тебе правила."
            jump rules_figures
        "Не хочу, давай в другой раз.":
            cat_math "Заходи еще!"
            jump math_level
    label rules_figures:
        cat_math """
        Правила этой игры просты, как дважды два:

        Я буду задавать тебе задачку о фигурах, а тебе нужно будет выбрать картинку-ответ.

        Задачки разные, надеюсь, тебе понравится. Начнем!
        """
    $ r = 0
    jump figures_game
    return
