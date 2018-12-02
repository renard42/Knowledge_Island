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

        text_list = [[0.5, 0.1], [0.5, 0.5]]
        pic_list = [[0.1, 0.5], [0.1,0.1]]
        err = 3
        moves = 2*2+err #ходов на каждую картинку  + еще столько же на убирание панельки + 3 ошибки
        store.pic_dic = {'Кафедральный собор Дурхам':'durham_cathedral', 'Стоунхэндж': 'stonehenge'}
        store.pic_keys = list(pic_dic.keys())

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
                    drags[0].snap(text_list[int(drags[0].drag_name[0])][0], text_list[int(drags[0].drag_name[0])][1], delay=0.1)
                    return "Мимо!"


    cat_eng "Расставь достопримечательности Британии. У тебя есть право на три ошибки"

    screen send_word_screen:
        # Группа drag гарантирует, что можно перетащить
        draggroup:
            for i, pic in enumerate(pic_keys):
                # картинки
                $ store.t = pic_dic[pic]+'_text'
                $ store.p = pic_dic[pic]
                $ store.text = "images/eng_lev0/[t].jpeg"
                $ store.picture = "images/eng_lev0/[p].jpeg"

                drag:
                    drag_name "0"+pic
                    child text
                    droppable False
                    draggable can_move
                    dragged word_dragged
                    pos (text_list[i][0], text_list[i][1])

                drag:
                    drag_name pic+"1"
                    child picture
                    draggable False
                    pos (pic_list[i][0], pic_list[i][1])


#where the game starts
$ text_list = [[0.5, 0.1], [0.5, 0.5]]
$ pic_list = [[0.1, 0.5], [0.1,0.1]]
$ err = 3
$ moves = 2+err #ходов на каждую картинку + 3 ошибки
$ pic_dic = {'Кафедральный собор Дурхам':'durham_cathedral', 'Стоунхэндж': 'stonehenge'}
$ pic_keys = list(pic_dic.keys())


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
    else:
        $ err-=1
        if err == 2:
            cat_eng "[res] Еще две жизни!"
        if err == 1:
            cat_eng "[res] Осторожно, осталась последняя попытка!"

        else:
            menu:
                cat_geo "Ты проиграл, и детальку я тебе не отдам!\n Хочешь попробовать еще раз?"

                "Да, я готов!":
                    $ player = False
                    jump game_curiosities
                "Нет, я лучше еще потренируюсь и приду":
                    cat_geo "До встречи, я буду тебя ждать!"
                    jump start


    $ can_move = True
