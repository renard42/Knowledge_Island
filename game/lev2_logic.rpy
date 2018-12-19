label level2_logic:
    menu:
        sphynx "Тебя ждет игра на внимательность и память"

        "Я готов!":
            jump game2_logic

        "Может другое?":
            jump logic_level


    label game2_logic:

        label repeat_rules:
            sphynx "Правила просты: в ход комьютера будут зажигаться огоньки в квадрате. Запомни их последовательность и повтори в свой ход"

            sphynx "Каждый ход количество зажигающихся огоньков увеличивается на 1 (от 1 до 5). Цель игры: правильно повторить за комьютером все 5 ходов."
            sphynx "При ошибке в каком-либо ходе всё начинается с начала: с одной клетки для потворения. У тебя три жизни, поэтому игра будет перезапускаться максимум два раза"
        menu:
            sphynx "Ты понял правила или хочешь послушать еще раз?"
            "Всё очевидно, давай скорее начнем!":
                sphynx "Ну, вперед"
                call simon pass (complete=5, toadd=1, err_check = 3) from _call_simon

            "А можешь повторить правила?":
                sphynx "Кто понял жизнь, тот не спешит... можно и еще раз"
                jump repeat_rules


label simon(complete=5, toadd=1, err_check = 3):
    $ sequence=[]
    $ yourguess=0
label simonturn:
    # add signs to the sequence, enlarging it each turn.
    python:
        for i in range(toadd):
            roll=renpy.random.randint(0,3)
            sequence.append(roll)
label simonshow:
    $ i=0
    $ random.shuffle(sequence)
    while i<len(sequence):
        $ thesign=sequence[i]

        show screen simonvoid
        $ renpy.pause(0.5, hard=True)
        hide screen simonvoid

        show screen simondisplay
        $ renpy.pause(0.5, hard=True)
        hide screen simondisplay
        $ i+=1
    $ i=0
label simonguess:
    $ thesign=sequence[i]
    call screen simoncheck
    $ dasign=_return
    if dasign!=thesign:
        $ err_check-=1
        if not err_check:
            $ renpy.music.play(fail, loop=False)
            sphynx "Я победил! Деталька моя"
            menu:
                sphynx "Хочешь сыграть еще раз?"
                "А ты упорный!":
                    call simon pass (complete=5, toadd=1, err_check = 3) from _call_simon_1
                "Нет, надо передохнуть":
                    sphynx "Возвращайся в другой раз"
                    jump logic_level
        else:
            "Ты ошибся! У тебя осталось [err_check] попыток"
            call simon pass (complete=5, toadd=1, err_check = err_check) from _call_simon_2
    if dasign==thesign:
        $ i+=1
        if i==len(sequence):
            jump simonend
    jump simonguess
label simonend:
    if len(sequence)==complete:
        $ renpy.music.play(success, loop=False)
        sphynx "Ты победил!"
        $ ship_status["logic"]["3"] = True
        menu:
            sphynx "Хочешь сыграть еще раз?"
            "Конечно!":
                call simon pass (complete=5, toadd=1, err_check = 3)
                return
            "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                sphynx "До встречи! Заходи еще!"
                jump logic_level
                return
    jump simonturn

screen simondisplay():
    text "Мой ход" xalign 0.5 yalign 0.2
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        if thesign==0:
            add "images/log_lev0/red.png"
        else:
            add "images/log_lev0/grey.png"

        if thesign==1:
            add "images/log_lev0/green.png"
        else:
            add "images/log_lev0/grey.png"

        if thesign==2:
            add "images/log_lev0/blue.png"
        else:
            add "images/log_lev0/grey.png"

        if thesign==3:
            add "images/log_lev0/yellow.png"
        else:
            add "images/log_lev0/grey.png"
screen simonvoid():
    text "Мой ход" xalign 0.5 yalign 0.2
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        for i in range(4):
            add "images/log_lev0/grey.png"
screen simoncheck():
    timer 10.0 action Return("bust")

    text "Теперь повтори!" xalign 0.5 yalign 0.2
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        imagebutton idle "images/log_lev0/grey.png" hover "images/log_lev0/red.png" action Return(0)
        imagebutton idle "images/log_lev0/grey.png" hover "images/log_lev0/green.png" action Return(1)
        imagebutton idle "images/log_lev0/grey.png" hover "images/log_lev0/blue.png" action Return(2)
        imagebutton idle "images/log_lev0/grey.png" hover "images/log_lev0/yellow.png" action Return(3)
