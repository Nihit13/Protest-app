from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem,ThreeLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker


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
                id:name
                hint_text:"Enter your protest name"
                required:True
                pos_hint:{"center_x":0.6,"center_y":0.8}
                size_hint:(0.7,0.1)
            MDLabel:
                text:"Description:"
                pos_hint:{"center_x":0.6,"center_y":0.65}
            MDTextField:
                multiline:True
                hint_text: "Enter protest description"
                required:True
                mode:"rectangle"
                pos_hint:{"center_x":0.59,"center_y":0.65}
                size_hint:(0.65,0.2)
            MDRectangleFlatButton:
                text:"Add date"
                pos_hint:{"center_x":0.3,"center_y":0.45}
                on_release:app.get_date()
            MDLabel:
                text:"Date:"
                pos_hint:{"center_x":0.6,"center_y":0.45}
            MDTextField:
                id:location
                hint_text:"Please enter the location/route of the protest"
                helper_text:"Enter the precise location"
                required:True
                helper_text_mode:"on_focus"
                pos_hint:{"center_x":0.6,"center_y":0.35}
                size_hint:(0.7,0.1)
            MDLabel:
                text:"Location:"
                pos_hint:{"center_x":0.6,"center_y":0.35}
            MDRaisedButton:
                text:"Create"
                pos_hint:{"center_x":0.5,"center_y":0.25}
                on_release:app.create_list()
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
            ScrollView:
                pos_hint:{"center_x":0.5,"center_y":0.4}
                MDList:
                    id:prolist
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
                text:"About us"
                pos_hint:{"center_x":0.95,"center_y":0.8}
            MDLabel:
                text:"We here at ___________ enhance the spirit of democracy by providing you the power to change the world. The world is in your hands."
                pos_hint:{"center_x":0.5,"center_y":0.7}

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
        self.app = Builder.load_string( helper )
        screen.add_widget( self.app )
        return screen
    def get_date(self):
        picker = MDDatePicker(callback=self.got_date)
        picker.open()
    def got_date(self,date):
        self.date = date
    def create_list(self):
        protest_name = self.app.ids.name.text
        protests = ThreeLineListItem(text="Name:"+protest_name,secondary_text="Location:"+self.app.ids.location.text,
                                     tertiary_text="Date:"+str(self.date))
        self.app.ids.prolist.add_widget(protests)
        self.app.ids.screen_manager.current = "screen5"
DemoApp().run()