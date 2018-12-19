init python:
    import random
label level2_math:
    menu:
        cat_math "Иногда самые обычные вещи могут пригодиться неожиданным образом. Я покажу тебе, как можно устроить математическую игру из домино!"

        "Интересно!":
            hide cat math
            call game2_math pass (complete = 5, toadd =3, err_check = 3, right_check=0, used=[]) from _call_game2_math

        "Может другое?":
            jump math_level

label game2_math(complete = 5, toadd = 3, err_check = 3, right_check=0, used=[]):
    #$ used = []
    $ right = []
    $ wrong = []
    $ lst = []

label turn:
    python:
        sum = random.randint(2,11)
        for _ in range(2):
            if sum<8:
                first_right_num=random.randint(1,sum-1)
                new_right=(first_right_num, sum-first_right_num)
                while (new_right in used):
                    first_right_num=random.randint(1,sum-1)
                    new_right=(first_right_num, sum-first_right_num)
                right.append(new_right)
                used.append(new_right)

            else:
                first_right_num=random.randint(sum-6,6)
                new_right=(first_right_num, sum-first_right_num)
                while (new_right in used):
                    first_right_num=random.randint(sum-6,6)
                    new_right=(first_right_num, sum-first_right_num)
                right.append(new_right)
                used.append(new_right)
        for i in range(toadd):
            wrong_first = random.randint(1,6)
            wrong_sec = random.randint(1,6)
            while (wrong_first, wrong_sec) in wrong:
                wrong_first = random.randint(1,6)
                wrong_sec = random.randint(1,6)
            if wrong_first+wrong_sec == sum:
                right.append((wrong_first, wrong_sec))
            else:
                wrong.append((wrong_first, wrong_sec))
        lst+=wrong
        lst+=right[1:]
        random.shuffle(lst)
label math_show:
    $ i=0
    show screen lookatthis
    $ renpy.pause(3, hard=True)
    hide screen lookatthis
    #show screen void
    #$ renpy.pause(0.5, hard=True)
    #hide screen void
label guess:
    call screen check
    $ dasign=_return
    if not any(thesign == dasign for thesign in right):
        $ err_check-=1
        if not err_check:
            $ renpy.music.play(fail, loop=False)
            cat_math "Я победил! Деталька моя"
            menu:
                cat_math "Хочешь сыграть еще раз?"
                "А ты упорный!":
                    call game2_math pass (complete = 5, toadd=3, err_check = 3, right_check=0, used=[]) from _call_game2_math_1
                "Нет, надо передохнуть":
                    cat_math "Возвращайся в другой раз"
                    jump math_level
        else:
            "Ты ошибся! У тебя осталось попыток: [err_check]"
            call game2_math pass (complete = 5, toadd=3, err_check = err_check, right_check=right_check,  used=used[:]) from _call_game2_math_2
    else:
        $ i+=1

        if i == len(right)-1:
            "Правильно!"
            $ right_check+=1

            jump math_end
        else:
            $ num = len(right)-1-i
            "Верно, найди еще [num]!"
    jump guess

label math_end:
    if right_check==complete:
        $ renpy.music.play(success, loop=False)
        cat_math "Ты победил!"
        $ ship_status["math"]["3"] = True
        menu:
            cat_math "Хочешь сыграть еще раз?"
            "Конечно!":
                call game2_math pass (complete = 5, toadd=3, err_check = 3, right_check=0,  used=[]) from _call_game2_math_3
                return
            "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                cat_math "До встречи! Заходи еще!"
                jump math_level
                return
    call game2_math pass (complete = 5, toadd=toadd, err_check = err_check, right_check=right_check, used=used[:]) from _call_game2_math_4

screen lookatthis():
    text "У тебя есть несколько секунд, чтобы запомнить фигуру" xalign 0.5 yalign 0.1
    image "images/math2/"+str(right[0][0])+"_"+str(right[0][1])+".png" xalign 0.5 yalign 0.5

screen check():
    text "Найди такие доминошки, сумма чисел на которых будет равняться сумме чисел на исходном домино" xalign 0.5 yalign 0.1
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        imagebutton idle "images/math2/"+str(lst[0][0])+'_'+str(lst[0][1])+".png" hover_background "#00a" action Return((lst[0][0], lst[0][1]))
        imagebutton idle "images/math2/"+str(lst[1][0])+'_'+str(lst[1][1])+".png" hover_background "#00a" action Return((lst[1][0], lst[1][1]))
        imagebutton idle "images/math2/"+str(lst[2][0])+'_'+str(lst[2][1])+".png" hover_background "#00a" action Return((lst[2][0], lst[2][1]))
        imagebutton idle "images/math2/"+str(lst[3][0])+'_'+str(lst[3][1])+".png" hover_background "#00a" action Return((lst[3][0], lst[3][1]))
