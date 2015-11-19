__version__ = "1.0"
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    texto = StringProperty("Proyecto Final Test")


class PFinalApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    PFinalApp().run()
