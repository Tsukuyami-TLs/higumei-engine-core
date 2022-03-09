init python in event_store:
    current_event = ""
    current_chapter = ""
    current_progress = 0
    notes = {}
    chapters = {}

    # Key: alphabetical ID for sorting
    # Value: (start label, title)
    event_list = {} 

    # Key: alphabetical ID for sorting
    # Value: (event id, chara id, start label, title) 
    ssr_list = {}

    # Key: character id
    # Valye: Character name
    character_list = {}
    


screen tl_notes(title="", contents=""):
    tag menu
    use game_menu(_("TL Notes")):
        style_prefix "about"
        has hbox

        
        viewport:
            area (0,0,500,1.0)

            draggable True
            mousewheel True
            scrollbars "vertical"

            has vbox
            
            for ntitle, ncontents in event_store.notes[event_store.current_event][:event_store.current_progress]:
                textbutton _(ntitle):
                    activate_sound "audio/sfx/SE_004_Tap.wav"
                    action ShowMenu("tl_notes", ntitle, ncontents)
                    selected title == ntitle

        null width 50
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            
            has vbox
            label title
            text contents
 
screen chapter_jump():
    tag menu
    use game_menu(_("Chapter Jump")):
        style_prefix "about"
        has hbox

        vbox:
            for title, label in event_store.chapters[event_store.current_event]:
                textbutton _(title):
                    activate_sound "audio/sfx/SE_002_Decision.wav"
                    action Start(label)
                    selected label == event_store.current_chapter

## Event Story Select screen ############################################################

screen events():

    tag menu

    add "images/menu/EventStoryBg.png" at center

    textbutton "Back" style "button_back" action ShowMenu("story_select")
        

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        for id, (label, title) in sorted(event_store.event_list.items()):
            textbutton title style "button_story" action Start(label)


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
        
        for id, chara_name in sorted(event_store.character_list.items()):
            textbutton chara_name style "button_story" action ShowMenu("stories", id, "char")


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
        
        for id, (label, title) in sorted(event_store.event_list.items()):
            textbutton title style "button_story" action ShowMenu("stories", id, "event")
        

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


        for id, (event_id, chara_id, label, title) in sorted(event_store.ssr_list.items()):
            if (type == "event" and key == event_id) or (type == "char" and key == chara_id):
                textbutton title style "button_story" action Start(label)

