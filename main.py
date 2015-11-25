__version__ = "1.0"
import tarea1.tarea1
import tarea2.tarea2 as ui
import tarea4.tarea4
import tarea5.tarea5
from api_client.sqldata import SQLData
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout


class MainWindow(AnchorLayout):
    datos = SQLData('http://localhost:8000')
    gridTest = ui.GridProyecto
    texto = StringProperty("Proyecto Final Test")

    def __init__(self):

        AnchorLayout.__init__(self)

        self.gridTest.addcolumna("Carnet", "key", "center", 90, False, 'carnet')
        self.gridTest.addcolumna("Nombre", "txt", "left", 200, False, 'nombre')
        self.gridTest.addcolumna("Apellido", "txt", "left", 200, False, 'apellido')
        self.gridTest.addcolumna("Email", "txt", "left", 310, False, 'email')
        self.datos.view = "estudiantes"
        self.gridTest.datasource = self.datos

        self.gridTest.addheaders()

#        self.gridTest.addgridrow([True, "1", "Articulo 1", "10", False])


class PFinalApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    PFinalApp().run()
