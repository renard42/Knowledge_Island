label level2_eng:
    define cat = Character("Шерлок")
    $ count = 0
    $ words = renpy.file('/codes/eng/words.txt').read().split('\n')[:-1]
    $ import random
    style button:
        background "#FFDEAD"
        hover_background "#DEB887"
    screen numbers_scr:

        key "K_LEFT" action Hide("nonexistent_screen")
        key "K_RIGHT" action Hide("nonexistent_screen")
        key "K_UP" action Hide("nonexistent_screen")
        key "K_DOWN" action Hide("nonexistent_screen")
        key "K_RETURN" action Hide("nonexistent_screen")
        key "K_KP_ENTER" action Hide("nonexistent_screen")

        timer 1 action [Return("smth"), If( game_timer>1, If( numbers_buttons[-1]["b_to_show"] == False, Return("win"), SetVariable("game_timer", game_timer-1) ), Return("lose") ) ] repeat True
        text "[game_timer]" size 40 xpos 10 ypos 10

        for each_b in sorted(numbers_buttons, reverse=True):
                if each_b["b_to_show"]:
                    $ text_var = each_b["b_value"]
                    $ i = each_b["b_number"] - 1
                    button:
                        text '[text_var]{size=18}{/size}' size 30 align (0.5, 0.55) color "#000"
                        xminimum 100 xmaximum 100
                        yminimum 100 ymaximum 100
                        xpos each_b["b_x_pos"]
                        ypos each_b["b_y_pos"]
                        anchor (0.5, 0.5)
                        action If (i == -1, SetDict(numbers_buttons[each_b["b_number"] ], "b_to_show", False),
                            If (numbers_buttons[i]["b_to_show"] == False,
                                SetDict(numbers_buttons[each_b["b_number"] ], "b_to_show", False),
                                SetVariable("game_timer", game_timer-1) )  )

    cat "Давай поиграем в слова!"
    cat "Я буду показывать тебе картинки и буквы. Тебе нужно составить из букв то, что изображено на картинке"
    cat "Но только время ограничено - 20 секунд на одно слово. В левом верхнем углу будет таймер."
    cat "Если ты нажмешь на неверную букву, то времени станет меньше"

    menu:
        cat "Начнем?"
        "Да, давай!":
            jump numbers_game
        "Не хочу. Лучше другую игру":
            jump eng_level

    label numbers_game:
        scene game_bg

        $ numbers_buttons = []
        $ buttons_values = []


        $ word = random.choice(words)
        $ del words[words.index(str(word))]
        $ w = [i.upper() for i in word[:-1]]
        $ word_img = word[:-1].replace(' ', '_')

        init:
            image img = "images/eng_lev2/[word_img].png"

        show img at Position(xalign = 1.0, yalign=1.0)
        python:
            for i in w:
                buttons_values.append (str(i))

        python:
            for i in range (0, len(buttons_values) ):
                numbers_buttons.append ( {"b_number":i, "b_value":buttons_values[i], "b_x_pos":(renpy.random.randint (10, 70))*10, "b_y_pos":(renpy.random.randint (15, 50))*10, "b_to_show":True} )

            for num, dic in enumerate(numbers_buttons[:-1]):
                if dic["b_x_pos"] - numbers_buttons[num+1]["b_x_pos"] < 10:
                    numbers_buttons[num+1]["b_x_pos"] +=30

        $ game_timer = 20

        show screen numbers_scr

        label loop:
            $ result3 = ui.interact()
            $ game_timer = game_timer
            if result3 == "smth":
                jump loop

        if result3 == "lose":
            hide screen numbers_scr
            hide game_bg
            scene bg england
            show cat england
            $ renpy.pause (0.1, hard = True)
            $ renpy.pause (0.1, hard = True)
            $ renpy.pause (0.1, hard = True)
            $ renpy.pause (0.1, hard = True)
            menu:
                cat "Ты проиграл :( Попробуешь еще раз?"
                "Да, давай еще раз!":
                    jump numbers_game
                "Лучше еще потренируюсь":
                    cat "Возвращайся!"
                    jump eng_level

        if result3 == "win":
            hide screen numbers_scr
            hide img
            $ renpy.pause (0.1, hard = True)
            $ renpy.pause (0.1, hard = True)
            $ renpy.pause (0.1, hard = True)
            $ renpy.pause (0.1, hard = True)
            "Все верррно!"
            if count!=5:
                $count+=1
                jump numbers_game
            else:
                cat "Молодец, ты выиграл! Идем дальше?"
                hide game_bg
                scene bg england
                show cat england
                $ship_status["eng"]["3"] = True
                menu:
                    cat "Хочешь сыграть еще раз?"

                    "Хочу!":
                        $ count = 0
                        jump numbers_game
                    "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                        cat "До встречи! Заходи еще!"
                        jump eng_level
