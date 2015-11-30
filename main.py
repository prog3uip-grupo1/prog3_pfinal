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
        self.gridTest.addcolumna("Carnet", "txt", "left", 50, False, 'carnet')
        self.gridTest.addcolumna("Usuario", "key", "center", 90, False, 'username')
        self.gridTest.addcolumna("Nombre", "txt", "left", 150, False, 'first_name')
        self.gridTest.addcolumna("Apellido", "txt", "left", 150, False, 'last_name')
        self.gridTest.addcolumna("Email", "txt", "left", 355, False, 'email')
        self.datos.view = "rest-auth/user"
        self.gridTest.datasource = self.datos

        self.gridTest.addheaders()

#        self.gridTest.addgridrow([True, "1", "Articulo 1", "10", False])


class PFinalApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    PFinalApp().run()
