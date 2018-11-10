# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cat = Character("Шерлок")

init python:

    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        """
        Represents a section of the tutorial menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)


    Section(_("Quickstart"))

    Tutorial("english", _("Английский"))
    Tutorial("geography", _("География"))
    Tutorial("sand",_("Логика"))

screen tutorials(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for i in tutorials:

                    if i.kind == "tutorial":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt ""
                        null height 5




        bar adjustment adj style "vscrollbar"

        textbutton _("That's enough for now."):
            xfill True
            action Return(False)
            top_margin 10


# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()

# True if this is the first time through the tutorials.
default tutorials_first_time = True




# The game starts here.

label start:

    label tutorials:

        scene bg england

        if tutorials_first_time:
            $ cat(_("Выбери категорию!"), interact=False)
        else:
            $ cat(_("Хочешь выбрать другую категорию?"), interact=False)

        $ tutorials_first_time = False
        $ renpy.choice_for_skipping()

        call screen tutorials(adj=tutorials_adjustment)

        $ tutorial = _return

        if not tutorial:
            jump end

        if tutorial.move_before:
            show cat
            with move

        call expression tutorial.label from _call_expression

        if tutorial.move_after:
            hide example
            show cat at left
            with move

        jump tutorials
