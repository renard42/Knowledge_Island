label level2_eng:
    scene bg england

    init python:
        import os,glob
        import random
        os.chdir("C:/Users/Олеся/Anaconda projects/НИС/Knowledge_Island/game/images/eng_lev2")
        obj = glob.glob('*.png')

    label game_start:
        $ i = 0
        $ img = random.sample(obj,4)

        while i!=4:
            $ flag1 = False
            $ flag2 = False
            $ flag3 = False
            $ flag4 = False
            $ flags = [flag1, flag2, flag3,flag4]


            screen choices:
                imagebutton xpos 0.45 xanchor 0.3 ypos 0.2 yanchor 0.5 idle ("images/eng_lev2/"+img[0]) action NullAction()
                imagebutton xpos 0.45 xanchor 0.3 ypos 0.55 yanchor 0.5 idle ("images/eng_lev2/"+img[1]) action NullAction()
                imagebutton xpos 0.65 xanchor 0.3  ypos 0.55 yanchor 0.5 idle ("images/eng_lev2/"+img[2]) action NullAction()
                imagebutton xpos 0.65 xanchor 0.3 ypos 0.2 yanchor 0.5 idle ("images/eng_lev2/"+img[3]) action NullAction()

            show screen choices
