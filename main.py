from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Dot 3D Maker - MIT License - Ready')

MyApp().run()