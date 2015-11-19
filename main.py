__version__ = "1.0"
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    texto = "Proyecto Final Test"


class PFinalApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    PFinalApp().run()
