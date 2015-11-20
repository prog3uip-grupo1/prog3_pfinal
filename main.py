__version__ = "1.0"
import tarea1.tarea1
import tarea2.tarea2 as ui
import tarea4.tarea4
import tarea5.tarea5
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout


class MainWindow(AnchorLayout):
    gridTest = ui.GridProyecto
    texto = StringProperty("Proyecto Final Test")

    def __init__(self):

        AnchorLayout.__init__(self)

        self.gridTest.addcolumna("Activo", "chk", "na", 70, True)
        self.gridTest.addcolumna("Articulo", "key", "center", 200, False)
        self.gridTest.addcolumna("Descripcion", "txt", "left", 356, False)
        self.gridTest.addcolumna("Cantidad", "txt", "right", 100, False)
        self.gridTest.addcolumna("Borrar", "bor", "na", 70, False)
        self.gridTest.addheaders()

        self.gridTest.addgridrow([True, "1", "Articulo 1", "10", False])



class PFinalApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    PFinalApp().run()
