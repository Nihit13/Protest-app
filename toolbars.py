from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem


screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                title:"Help"
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                type:"bottom"
"""
helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:"vertical"
                    MDToolbar:
                        title:"Demo"
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:

        MDNavigationDrawer:
            id:nav_drawer
            size_hint:(0.5,0.9)
            
            Screen:
                BoxLayout:
                    orientation:"vertical"
                    padding:"20dp"
                    spacing:"20dp"
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text:"Start protest"
                                IconLeftWidget:
                                    icon:"android"
                            OneLineIconListItem:
                                text:"FAQ"
                                icon:"android"
                            OneLineIconListItem:
                                text:"Item3"
                                IconLeftWidget:
                                    icon:"android"
                            OneLineIconListItem:
                                text:"Item4"
                                IconLeftWidget:
                                    icon:"android"
                            OneLineIconListItem:
                                text:"Item5"
                                IconLeftWidget:
                                    icon:"android"

"""

class DemoApp( MDApp ):

    def build(self):
        screen = Builder.load_string( screen_helper )
        navigation = Builder.load_string(helper)
        screen.add_widget(navigation)

        return screen

    def navigation_draw(self):
        print( "Navigation" )
    def lv(self,obj):
        for i in range( 20 ):
            items = OneLineListItem( text="item" + str( i ) )
            self.root.ids.listh.add_widget( items )


DemoApp().run()