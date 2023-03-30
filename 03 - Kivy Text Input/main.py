# Using Python 3.10
from kivy.app import App
from kivy.uix.widget import Widget


# Interface
class Interface(Widget):
    def on_enter_pressed(self):
        print("Enter has been pressed!")


# App Creation
class TestApp(App):
    pass


TestApp().run()