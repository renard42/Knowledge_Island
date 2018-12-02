init python:
    import random

label level0_eng:
    menu:
        cat_eng "Сможешь отгадать достопримечательности моей родной страны, Великобритании?"
        "Поехали!":
            jump game_curiosities

        "Давай на другой уровень":
            jump eng_level

label game_curiosities:
    init python:
        text_list = [[0.6, 0.5], [0.6, 0.3], [0.6, 0.05]]
        pic_list = [[0.28, 0.05], [0.03, 0.05], [0.03, 0.35]]
        random.shuffle(pic_list)
        err = 3

        pic1 = "Кафедральный собор Дурхам"
        picture1 = "images/eng_lev0/durham_cathedral.jpg"
        text1 = "images/eng_lev0/durham_cathedral_text.jpg"
        pic2 = "Стоунхэндж"
        picture2 = "images/eng_lev0/stonehenge.jpeg"
        text2 = "images/eng_lev0/stonehenge_text.jpeg"
        pic3 = "Озеро Лохнесс"
        picture3 = "images/eng_lev0/lochness.jpg"
        text3 = "images/eng_lev0/lochness_text.jpg"


        def word_dragged(drags, drop):
            if not drop:
                drags[0].snap(text_list[int(drags[0].drag_name[0])][0], text_list[int(drags[0].drag_name.split("-")[0])][1], delay=0.1)
                return "Мимо!"

            else:
                store.word = drags[0].drag_name[1:]
                store.picture = drop.drag_name[:-1]
                if store.word==store.picture:
                    return "Правильно! Это "+store.word
                else:
                    drags[0].snap(text_list[int(drags[0].drag_name[0])][0], text_list[int(drags[0].drag_name[0])][1])
                    return "Мимо!"


    cat_eng "Расставь достопримечательности Британии. У тебя есть право на три ошибки"

    screen send_word_screen:
        draggroup:
            drag:
                drag_name "0"+pic1
                child text1
                droppable False
                draggable can_move
                dragged word_dragged
                pos (text_list[0][0], text_list[0][1])

            drag:
                drag_name pic1+"0"
                child picture1
                draggable False
                pos (pic_list[0][0], pic_list[0][1])

            drag:
                drag_name "1"+pic2
                child text2
                droppable False
                draggable can_move
                dragged word_dragged
                pos (text_list[1][0], text_list[1][1])

            drag:
                drag_name pic2+"1"
                child picture2
                draggable False
                pos (pic_list[1][0], pic_list[1][1])
            drag:
                drag_name "2"+pic3
                child text3
                droppable False
                draggable can_move
                dragged word_dragged
                pos (text_list[2][0], text_list[2][1])

            drag:
                drag_name pic3+"2"
                child picture3
                draggable False
                pos (pic_list[2][0], pic_list[2][1])



#where the game starts
$ text_list = [[0.6, 0.5], [0.6, 0.3], [0.6, 0.05]]
$ pic_list = [[0.28, 0.05], [0.03, 0.05], [0.03, 0.35]]
$ random.shuffle(pic_list)
$ err = 3
$ moves = 3+err-1 #ходов на каждую картинку + 2 ошибки
$ pic_dic = {'Кафедральный собор Дурхам':'durham_cathedral', 'Стоунхэндж': 'stonehenge', 'Озеро Лохнесс': 'lohness'}
$ pic_keys = list(pic_dic.keys())

$ num_right = 0
while moves:
    window hide
    $ can_move = True
    show screen send_word_screen
    $ res = ui.interact()
    $ can_move = False
    window show
    $ moves-=1
    # можем как-то использовать значение, которое вернула игра
    if res[:10]=="Правильно!":
        cat_eng "[res]"
        $ num_right += 1
        if num_right==3:
            cat_geo "Уррррраа! Ты прошел уровень!"


            menu:
                cat_geo "Хочешь сыграть еще раз?"

                "Хочу! Давай повторим!":
                    hide screen send_word_screen
                    show screen send_word_screen
                    jump game_curiosities
                "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                    cat_geo "До встречи, умный ребенок!"
                    jump start

    else:
        $ err-=1
        if err == 2:
            cat_eng "[res] Еще две жизни!"
        if err == 1:
            cat_eng "[res] Осторожно, осталась последняя попытка!"

        if err == 0:
            menu:
                cat_geo "Ты проиграл, и детальку я тебе не отдам!\n Хочешь попробовать еще раз?"

                "Да, я готов!":
                    hide screen send_word_screen
                    show screen send_word_screen
                    jump game_curiosities
                "Нет, я лучше еще потренируюсь и приду":
                    cat_geo "До встречи, я буду тебя ждать!"
                    jump start


    $ can_move = True
