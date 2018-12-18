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
        text_list = [[0.58, 0.5], [0.58, 0.4], [0.58, 0.3], [0.58, 0.6], [0.58, 0.8], [0.58, 0.05]]
        pic_list = [[0.28, 0.05], [0.28, 0.35], [0.28, 0.65], [0.03, 0.05], [0.03, 0.35], [0.03, 0.65]]
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
        pic4 = "Вестминистерское аббатство"
        picture4 = "images/eng_lev0/WestminsterAbbey.jpg"
        text4 = "images/eng_lev0/abbey_text.jpg"
        pic5 = "Биг Бен"
        picture5 = "images/eng_lev0/bigben.jpg"
        text5 = "images/eng_lev0/bigben_text.jpg"
        pic6 = "Музей восковых фигур имени Мадам Тюссо"
        picture6 = "images/eng_lev0/tussaud.jpg"
        text6 = "images/eng_lev0/tussaud_text.jpg"


        def word_dragged(drags, drop):
            if not drop:
                drags[0].snap(text_list[int(drags[0].drag_name[0])][0], text_list[int(drags[0].drag_name[0])][1], delay=0.1)
                return False

            else:
                store.word = drags[0].drag_name[1:]
                store.picture = drop.drag_name[:-1]
                #store.dra = drags[0]
                #store.dro = drop

                if store.word==store.picture:
                    drags[0].snap(-1000, -1000)
                    drop.snap(-1000, -1000)

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
            drag:
                drag_name "3"+pic4
                child text4
                droppable False
                draggable can_move
                dragged word_dragged
                pos (text_list[3][0], text_list[3][1])

            drag:
                drag_name pic4+"3"
                child picture4
                draggable False
                pos (pic_list[3][0], pic_list[3][1])
            drag:
                drag_name "4"+pic5
                child text5
                droppable False
                draggable can_move
                dragged word_dragged
                pos (text_list[4][0], text_list[4][1])

            drag:
                drag_name pic5+"4"
                child picture5
                draggable False
                pos (pic_list[4][0], pic_list[4][1])
            drag:
                drag_name "5"+pic6
                child text6
                droppable False
                draggable can_move
                dragged word_dragged
                pos (text_list[5][0], text_list[5][1])

            drag:
                drag_name pic6+"5"
                child picture6
                draggable False
                pos (pic_list[5][0], pic_list[5][1])



#where the game starts
$ text_list = [[0.58, 0.59], [0.58, 0.41], [0.58, 0.21], [0.58, 0.74], [0.58, 0.85], [0.58, 0.05]]
$ pic_list = [[0.28, 0.05], [0.28, 0.35], [0.28, 0.65], [0.03, 0.05], [0.03, 0.35], [0.03, 0.65]]
$ random.shuffle(pic_list)
$ err = 3
$ pic_dic = {'Кафедральный собор Дурхам':'durham_cathedral', 'Стоунхэндж': 'stonehenge', 'Озеро Лохнесс': 'lohness'}
$ pic_keys = list(pic_dic.keys())

$ num_right = 0
while True:
    window hide
    $ can_move = True
    show screen send_word_screen
    $ res = ui.interact(clear = True)
    $ can_move = False
    window show
    # можем как-то использовать значение, которое вернула игра
    if res:
        if res[:10]=="Правильно!":
            cat_eng "[res]"
            $ num_right += 1
            if num_right==6:
                $ renpy.music.play(success, loop=False)
                $ ship_status["eng"]["1"] = True
                cat_geo "Уррррраа! Ты прошел уровень!"


                menu:
                    cat_eng "Хочешь сыграть еще раз?"

                    "Хочу! Давай повторим!":
                        hide screen send_word_screen
                        show screen send_word_screen
                        jump game_curiosities
                    "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                        cat_eng "До встречи, умный ребенок!"
                        jump eng_level

        else:
            $ err-=1
            if err == 2:
                cat_eng "[res] Еще две жизни!"
            if err == 1:
                cat_eng "[res] Осторожно, осталась последняя попытка!"

            if err == 0:
                $ renpy.music.play(fail, loop=False)
                hide screen send_word_screen
                menu:
                    cat_eng "Ты проиграл!\n Хочешь попробовать еще раз?"
                    "Да, я готов!":
                        jump game_curiosities
                    "Нет, я лучше еще потренируюсь и приду":
                        cat_eng "До встречи, я буду тебя ждать!"

                        hide send_word_screen
                        hide img
                        jump eng_level


    $ can_move = True
