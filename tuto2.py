#!/usr/bin/env python3
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.widget import Widget

class CustomWidget(Widget):

    pass

class CustomWidgetApp(App):

    def build(self):

        return customWidget()

customWidget = customWidgetApp()

customWidget.run()
