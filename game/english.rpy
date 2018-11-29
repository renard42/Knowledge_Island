define cat_eng = Character("Шерлок")

label english:

scene bg england
show cat england

cat "Добро пожаловать!"

cat_eng "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"

cat_eng "С чего начнем?"

show cat england at left with move
label eng_level:
        menu:

            cat_eng "Какой уровень пррредпочитаешь?"

            "Начнем с чего попроще":

                jump level0_eng

            "А есть что-то среднее?":

                jump level1_eng

            "Я уверен в себе! Давай самое сложное!":

                jump level2_eng
