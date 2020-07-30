from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen



helper = """

NavigationLayout:
    MDNavigationDrawer:
        size_hint:(0.5,0.9)
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
                        title:"Help"
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
            MDLabel:
                text: "Screen 7"
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
"""





screen = Screen()

class DemoApp( MDApp ):

    def build(self):
        app = Builder.load_string(helper)
        screen.add_widget(app)
        return screen




DemoApp().run()