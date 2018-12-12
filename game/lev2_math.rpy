init python:
    import random
label level2_math:
    menu:
        cat_math "Иногда самые обычные вещи могут пригодиться неожиданным образом. Я покажу тебе, как можно устроить математическую игру из домино!"

        "Интересно!":
            hide cat math
            call game2_math pass (complete = 5, toadd =3, err_check = 3, right_check=0)

        "Может другое?":
            jump math_level

label game2_math(complete = 5, toadd = 3, err_check = 3, right_check=0):
    $ used = []
    $ right = []
    $ wrong = []
    $ lst = []

label turn:
    python:
        sum = random.randint(2,11)
        for e in range(2):
            if sum<8:
                first_right_num=random.randint(1,sum-1)
                new_right=(first_right_num, sum-first_right_num)
                while (new_right in right) or (new_right in used):
                    first_right_num=random.randint(1,sum-1)
                    new_right=((first_right_num, sum-first_right_num))
                right.append(new_right)
                used.append(new_right)

            else:
                first_right_num=random.randint(sum-6,6)
                new_right=(first_right_num, sum-first_right_num)
                while (new_right in right) or (new_right in used):
                    first_right_num=random.randint(sum-6,6)
                    new_right=(first_right_num, sum-first_right_num)
                right.append(new_right)
                used.append(new_right)
        for i in range(toadd):
            wrong_first = random.randint(1,6)
            wrong_sec = random.randint(1,6)
            while ((wrong_first, wrong_sec) in wrong) or ((wrong_first, wrong_sec) in right):
                wrong_first = random.randint(1,6)
                wrong_sec = random.randint(1,6)
            if wrong_first+wrong_sec == sum:
                right.append((wrong_first, wrong_sec))
            else:
                wrong.append((wrong_first, wrong_sec))
        lst+=wrong
        lst+=right[1:]
        random.shuffle(lst)
    #cat_math "[right] and [wrong]"
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
            cat_math "Я победил! Деталька моя"
            menu:
                cat_math "Хочешь сыграть еще раз?"
                "А ты упорный!":
                    call game2_math pass (complete = 5, toadd=3, err_check = 3, right_check=0)
                "Нет, надо передохнуть":
                    cat_math "Возвращайся в другой раз"
                    hide bg math
                    hide cat math
                    jump start
        else:
            "Ты ошибся! У тебя осталось попыток: [err_check]"
            call game2_math pass (complete = 5, toadd=3, err_check = err_check, right_check=right_check)
    else:
        $ i+=1

        if i == len(right)-1:
            "Правильно!"
            $ right_check+=1

            jump math_end
        else:
            "Верно, найди еще [len(right)-1-i]!"
    jump guess

label math_end:

    if right_check==complete:
        cat_math "Ты победил!"
        menu:
            cat_math "Хочешь сыграть еще раз?"
            "Конечно!":
                call game2_math pass (complete = 5, toadd=3, err_check = 3, right_check=0)
                return
            "Извини, но я пойду дальше - мне еще много деталек нужно собрать":
                cat_math "До встречи! Заходи еще!"
                hide bg math
                hide cat math
                jump start
                return
    call game2_math pass (complete = 5, toadd=toadd, err_check = err_check, right_check=right_check)

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
