from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from random import random

class Gerenciador (ScreenManager):
    pass
    
class Primeira(Screen):
    pass

class Segunda(Screen):
    pass
    
class PaintApp(App):
    def build (self):
        return Gerenciador()
        
PaintApp().run()
