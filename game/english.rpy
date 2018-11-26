define cat = Character("Шерлок")

label english:


scene bg england
show cat england

cat "Добро пожаловать!"

cat "Если ты хочешь, чтобы я отдал тебе деталь корабля, тебе нужно пройти мое испытание!"

cat "С чего начнем?"

show cat england at left with move
menu:

    cat "Какой уровень пррредпочитаешь?"

    "Начнем с чего попроще":

        jump level0_eng

    "А есть что-то среднее?":
        cat "Среднее не значит скучное! Начнем! Мряв"
        jump level1_eng

    "Я уверен в себе! Давай самое сложное!":
        cat "Ты смелый игрок! Вперед, мррр :3"
        jump level2_eng
