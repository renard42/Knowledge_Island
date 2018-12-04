define sphynx = Character("Сфинкс")


init python:
    import random

    # НАСТРОЙКИ ИГРЫ ПО УМОЛЧАНИЮ:

    # набор типов карточек по умолчанию
    all_cards = ['A', 'B', 'C']
    ww = 3
    hh = 3
    max_c = 2
    card_size = 48
    max_time = 25
    wait = 0.5
    img_mode = True

    values_list = []
    temp = []
    # объявляем картинки-карточки
    # должны быть в формате "images/card_*.png"
    # обязательны "card_back.png" и "card_empty.png"
    for fn in renpy.list_files():
        if fn.startswith("images/card_") and fn.endswith((".png")):
            name = fn[12:-4]
            renpy.image("card " + name, fn)
            if name != "empty" and name != "back":
                temp.append(str(name))
    if len(temp) > 1:
        all_cards = temp
    else:
        img_mode = False

    def cards_init():
        global values_list
        values_list = []
        p = 0
        store.v = []
        while len(values_list) + max_c <= ww * hh:
            current_card = renpy.random.choice(all_cards)
            v.append(current_card)
            for i in range(0, max_c):
                values_list.append(current_card)
        renpy.random.shuffle(values_list)
        while len(values_list) < ww * hh:
            values_list.append('empty')

screen memo_scr:
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    grid ww hh:
        align (.5, .5)
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                if card["c_value"] == 'empty':
                    if img_mode:
                        add "card empty"
                    else:
                        text " " size card_size
                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card " + card["c_value"]
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card back"
                        else:
                            text "#" size card_size
                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
    text str(memo_timer) xalign .5 yalign 0.0 size card_size

label memoria_game:
    $ cards_init()
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            if values_list[i] == 'empty':
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":True} )
            else:
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )
    $ memo_timer = max_time
    show screen memo_scr
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        $ can_click = False
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        else:
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_value"] = 'empty'
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("memo_game_loop")
                renpy.jump ("memo_game_win")
        jump memo_game_loop

label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    menu:
        sphynx "Ты проиграл! Попробуешь еще раз?"
        "Да!":
            jump memoria_game
        "Нет, я лучше потом зайду":
            sphynx "Возвррращайся!"
            jump start

label memo_game_win:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    show sph at left with move
    sphynx "Молодец, ты победил!"
    $ musical = renpy.file('/codes/memoria/music.txt').read().split('\n')
    $ ms = {}
    $ e = 0
    while e<len(musical):
        $ m1 = musical[e].split(';')
        $ ms[m1[0]] = [m1[1],m1[2]]
        $ e+=1

    $ names = ', '.join([n1[0] for n,n1 in ms.items() if n in v])
    $ temp_names = {n : n1[0] for n,n1 in ms.items() if n in v}
    $ desc = {n : n1[1] for n,n1 in ms.items() if n in v}
    menu:
        sphynx "В моей игре ты видел: [names]. Хочешь узнать об этих инструментах?"
        "Да, конечно!":
            jump explain
        "Нет, я все знаю. Давай дальше!":
            sphynx "Тогда удачи в другой игре!"
            jump start

    label explain:
        $ store.e=-1
        $ v = list(set(v))
        $ p = list(desc.keys())
        sphynx "[p]"
        while e<len(v)-1:
            $ e+=1
            if v[e]!='empty':
                $ t = v[e]
                image img = "images/card_[t].png"
                show img at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5):
                    zoom 3.0
                $ name = v[e]
                #sphynx "[name]"
                $ description = desc[name].split('.')
                $ e1 = 0
                while e1<len(description)-1:
                    $ speak = description[e1]
                    sphynx "[speak]"
                    $ e1+=1
        sphynx "У меня все. Отправляйся за другими детальками!"
        hide bg sand
        hide sph
        jump start



label level0_logic:
    scene bg pyrs
    $ max_time = 60
    $ ww, hh = 4, 4
    call memoria_game
    return
