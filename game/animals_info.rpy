label animals_help:
    $ new_animal_descr_rus = random_animals_rus[i].split('.')
    $ n =0

    while n<len(new_animal_descr_rus)-1:
        $ renpy.say(owl_eng,new_animal_descr_rus[n])
        $ n+=1

    if animal_life<num:
        jump continue_animal
    else:
        jump continue_animals
