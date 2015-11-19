__version__ = "1.0"
import tarea1.tarea1
import tarea2.tarea2
import tarea4.tarea4
import tarea5.tarea5
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
