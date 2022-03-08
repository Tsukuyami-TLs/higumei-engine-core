## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

init -2 python:
    persistent.menu_return = ""
    class Start(Action, DictEquality):
        """
         :doc: menu_action

         Causes Ren'Py to jump out of the menu context to the named
         label. The main use of this is to start a new game from the
         main menu. Common uses are:

         * Start() - Start at the start label.
         * Start("foo") - Start at the "foo" label.
         """

        def __init__(self, label="start"):
            self.label = label

        def __call__(self):
            renpy.transition(Dissolve(0.3))
            renpy.jump_out_of_context(self.label)

screen main_menu():
    tag menu

    if persistent.menu_return == "event":
        $ persistent.menu_return = ""
        use events
    elif persistent.menu_return == "chara":
        $ persistent.menu_return = ""
        use characters_event
    else:
        use default_main_menu

screen default_main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background at truecenter

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    image "gui/higulogo_mei.png":
        xzoom 0.6
        yzoom 0.6
        xalign 0.9
        yalign -0.3

    if gui.show_name:

        vbox:
            
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")




## Story Select screen ############################################################

screen story_select():

    tag menu

    add "images/menu/PhotoStoryTop.png":
        xpos 67
        ypos 24
        xzoom 0.466
        yzoom 0.466
        rotate 10

    add "images/menu/BgStoryTop.png" at center

    textbutton "Title Screen" style "button_back" action ShowMenu("main_menu")
        

    vbox:
        xalign 0.9
        yalign 0.5
        spacing 18

        imagebutton idle "gui/button/BtnMainStory.png" at grayscale action NullAction()

        hbox:
            spacing 18

            imagebutton idle "gui/button/BtnCharaStory.png":
                activate_sound "audio/sfx/SE_002_Decision.wav"
                action ShowMenu("characters_event")


            imagebutton idle "gui/button/BtnTips.png" at grayscale action NullAction()

            imagebutton idle "gui/button/BtnEventStory.png":
                activate_sound "audio/sfx/SE_002_Decision.wav"
                action ShowMenu("events")


## TIPS Select screen ############################################################

screen tips():

    tag menu

    add "images/menu/TipsStoryBg.png" at center

    textbutton "Back" style "button_back" action ShowMenu("story_select")
        

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        textbutton "TIPS" style "button_story" action NullAction()


## Event Story Select screen ############################################################

screen events():

    tag menu

    add "images/menu/EventStoryBg.png" at center

    textbutton "Back" style "button_back" action ShowMenu("story_select")
        

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        textbutton "The Witch's Bloodstained Birthday Banquet" style "button_story" action Start("event_umi1")
        textbutton "1983, The Bewilderment of Ange Ushiromiya" style "button_story" action Start("event_umi2")


## Character Story Select screen ############################################################

screen characters():
    tag menu
    add "images/menu/CharaStoryBg.png" at center
    textbutton "Back" style "button_back" action ShowMenu("story_select")
    textbutton "Sort by Character" style "button_sort" action ShowMenu("characters_event")


    vpgrid:
        cols 1
        xalign 0.5
        yalign 0.5
        spacing 10
        ymaximum 860

        draggable True
        mousewheel True
        if renpy.variant("android"):
            scrollbars "vertical"

        textbutton "Nao" style "button_story" action ShowMenu("stories", "nao", "char")
        textbutton "Rika" style "button_story" action ShowMenu("stories", "rika", "char")
        textbutton "Akasaka" style "button_story" action ShowMenu("stories", "akasaka", "char")
        textbutton "Others" style "button_story" action ShowMenu("stories", "others", "char")

screen characters_event():
    tag menu
    add "images/menu/CharaStoryBg.png" at center
    textbutton "Back" style "button_back" action ShowMenu("story_select")
    textbutton "Sort by Event" style "button_sort" action ShowMenu("characters")

    vpgrid:
        cols 1
        xalign 0.5
        yalign 0.5
        spacing 10
        ymaximum 860

        draggable True
        mousewheel True
        if renpy.variant("android"):
            scrollbars "vertical"

        textbutton "The Witch's Bloodstained Birthday Banquet" style "button_story" action ShowMenu("stories", "witch", "event")
        textbutton "1983, The Bewilderment of Ange Ushiromiya" style "button_story" action ShowMenu("stories", "ange", "event")


screen stories(key, type):
    tag menu
    add "images/menu/CharaStoryBg.png" at center

    if type == "event":
        textbutton "Back" style "button_back" action ShowMenu("characters_event")
    if type == "char":
        textbutton "Back" style "button_back" action ShowMenu("characters")

    vpgrid:
        cols 1
        xalign 0.5
        yalign 0.5
        spacing 10
        ymaximum 860

        draggable True
        mousewheel True
        if renpy.variant("android"):
            scrollbars "vertical"

        if(key == "witch"):
            textbutton "\"Chiester Sister Corps\" Nao Houtani" style "button_story" action Start('chara032009')
            textbutton "\"The Golden Witch\" Beatrice" style "button_story" action Start('chara452001')
            textbutton "\"Witch of Truth\" Erika Furudo" style "button_story" action Start('chara462001')
            textbutton "\"Inquisitor of Heresy\" Dlanor" style "button_story" action Start('chara472001')

        if(key == "ange"):
            textbutton "\"Chiester Sister Corps\" Furude Rika" style "button_story" action Start('event_chara072016')
            textbutton "\"Game Master\" Mamoru Akasaka" style "button_story" action Start('event_chara142002')
            textbutton "\"Endless Sorcerer\" Battler Ushiromiya" style "button_story" action Start('event_chara482001')
            textbutton "\"Witch of Resurrection\" Ange Ushiromiya" style "button_story" action Start('event_chara492001')

       
        if(key == "nao"):
           textbutton "\"Chiester Sister Corps\" Nao Houtani" style "button_story" action Start('chara032009')


        if(key == "rika"):
            textbutton "\"Chiester Sister Corps\" Furude Rika" style "button_story" action Start('event_chara072016')

        if(key == "akasaka"):
            textbutton "\"Game Master\" Mamoru Akasaka" style "button_story" action Start('event_chara142002')

        if(key == "others"):
            textbutton "\"The Golden Witch\" Beatrice" style "button_story" action Start('chara452001')
            textbutton "\"Witch of Truth\" Erika Furudo" style "button_story" action Start('chara462001')
            textbutton "\"Inquisitor of Heresy\" Dlanor" style "button_story" action Start('chara472001')
            textbutton "\"Endless Sorcerer\" Battler Ushiromiya" style "button_story" action Start('event_chara482001')
            textbutton "\"Witch of Resurrection\" Ange Ushiromiya" style "button_story" action Start('event_chara492001')