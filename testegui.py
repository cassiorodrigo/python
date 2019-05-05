#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class loginscreen(GridLayout):
    def __init__(self, **kwargs):
        super(loginscreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

class SimpleKivy(App):
    def build(self):
        return loginscreen()



SimpleKivy().run()