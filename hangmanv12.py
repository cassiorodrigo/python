from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
texto = ''

class hangman(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.ids.palavra.text = texto
        self.ids.palavra.text = ''

    def recpal(self, palavra):

        return palavra


class interface(App):
    def build(self):
        return hangman()
interface().run()


