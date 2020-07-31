from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen

helper = """
NavigationLayout:
    ScreenManager:
        id: screen_manager
        Screen:
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "Your app"
                    elevation :5
                    left_action_items: [['menu', lambda x: toot.toggle_nav_drawer()]]
                Widget:
                MDBottomAppBar:
                    MDToolbar:
                        title:"help"
                        left_action_items:[["help",lambda x:app.draw()]]
                        type:"bottom"
        Screen:
            name: "screen2"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "Create"
                    elevation:5
                    left_action_items: [['menu', lambda x: toot.toggle_nav_drawer()]]
                Widget:
                MDBottomAppBar:
                    MDToolbar:
                        title:"Help"
                        left_action_items:[["help",lambda x:app.draw()]]
                        type:"bottom"
            MDLabel:
                text:"Name:"
                pos_hint:{"center_x":0.6,"center_y":0.8}
            MDTextField:
                hint_text:"Enter your protest name"
                pos_hint:{"center_x":0.6,"center_y":0.8}
                size_hint:(0.7,0.1)
            MDLabel:
                text:"Description:"
                pos_hint:{"center_x":0.6,"center_y":0.65}
            MDTextField:
                multiline:True
                hint_text: "Enter protest description"
                mode:"rectangle"
                pos_hint:{"center_x":0.59,"center_y":0.65}
                size_hint:(0.65,0.2)
            
        Screen:
            name: "screen3"
            MDLabel:
                text: "Screen 3"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "protest around"
                    elevation:5
                    left_action_items: [['menu', lambda x: toot.toggle_nav_drawer()]]
                Widget:
                MDBottomAppBar:
                    MDToolbar:
                        title:"Help"
                        left_action_items:[["help",lambda x:app.draw()]]
                        type:"bottom"
        Screen:
            name: "screen4"
            MDLabel:
                text: "Screen 4"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "FAQ"
                    elevation:5
                    left_action_items: [['menu', lambda x: toot.toggle_nav_drawer()]]
                Widget:
                MDBottomAppBar:
                    MDToolbar:
                        title:"Help"
                        left_action_items:[["help",lambda x:app.draw()]]
                        type:"bottom"
        Screen:
            name: "screen5"
            MDLabel:
                text: "Screen 5"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "Your protests"
                    elevation:5
                    left_action_items: [['menu', lambda x: toot.toggle_nav_drawer()]]
                Widget:
                MDBottomAppBar:
                    MDToolbar:
                        title:"Help"
                        left_action_items:[["help",lambda x:app.draw()]]
                        type:"bottom"
        Screen:
            name: "screen6"
            MDLabel:
                text: "Screen 6"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "protest merch"
                    elevation:5
                    left_action_items: [['menu', lambda x: toot.toggle_nav_drawer()]]
                Widget:
                MDBottomAppBar:
                    MDToolbar:
                        title:"Help"
                        left_action_items:[["help",lambda x:app.draw()]]
                        type:"bottom"
        Screen:
            name: "screen7"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "about us"
                    elevation:5
                    left_action_items: [['menu', lambda x: toot.toggle_nav_drawer()]]
                Widget:
                MDBottomAppBar:
                    MDToolbar:
                        title:"Help"
                        left_action_items:[["help",lambda x:app.draw()]]
                        type:"bottom"
            MDLabel:
                text:"Our Team"
                pos_hint:{"center_x":1,"center_y":0.85}
            MDTextField:
                hint_text:"This is our team"
                pos_hint:{"center_x":0.5,"center_y":0.6}
                size_hint:(0.7,0.1)
            
    MDNavigationDrawer:
        id:toot
        BoxLayout:
            orientation: 'vertical'
            padding:"30dp"
            spacing:"10dp"
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "Create"
                        on_release:
                            screen_manager.current = "screen2"
                            toot.toggle_nav_drawer()
                        IconLeftWidget:
                            icon:"android"
                    OneLineIconListItem:
                        text: "protests around"
                        on_release:
                            screen_manager.current = "screen3"
                            toot.toggle_nav_drawer()
                        IconLeftWidget:
                            icon:"android"
                    OneLineIconListItem:
                        text: "FAQ"
                        on_release:
                            screen_manager.current = "screen4"
                            toot.toggle_nav_drawer()
                        IconLeftWidget:
                            icon:"android"
                    OneLineIconListItem:
                        text: "your protests"
                        on_release:
                            screen_manager.current = "screen5"
                            toot.toggle_nav_drawer()
                        IconLeftWidget:
                            icon:"android"
                    OneLineIconListItem:
                        text: "protest merch"
                        on_release:
                            screen_manager.current = "screen6"
                            toot.toggle_nav_drawer()
                        IconLeftWidget:
                            icon:"android"
                    OneLineIconListItem:
                        text: "About us"
                        on_release:
                            screen_manager.current = "screen7"
                            toot.toggle_nav_drawer()
                        IconLeftWidget:
                            icon:"android"
"""

screen = Screen()


class DemoApp( MDApp ):

    def build(self):
        app = Builder.load_string( helper )
        screen.add_widget( app )
        return screen


DemoApp().run()
