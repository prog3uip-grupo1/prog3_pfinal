__version__ = "1.0"
import tarea1.tarea1
import tarea2.tarea2 as ui
import tarea4.tarea4
import tarea5.tarea5
from api_client.sqldata import SQLData
from kivy.app import App
#from kivy.config import Config
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from putils import AppMiscError, showmessagebox
from data.localdata import LocalData

# Config.set('graphics', 'resizable', '1')
# Config.set('graphics', 'width', '600')
# Config.set('graphics', 'height', '900')


class MainWindow(FloatLayout):
    __lastuser = ''
    __is_sync = False
    __carnet_sync = ''
    __django_api = ''

    ldatos = LocalData('pfinal.sqlite3')
    datos_api = SQLData
    # gridTest = ui.GridProyecto
    texto = StringProperty("Proyecto Final Test")

    def __init__(self):
        try:

            FloatLayout.__init__(self)
            self.ldatos.conectar()
            self.getappsettings()

#            if not self.__is_sync:
#                self.showloginform()

            datos_api = SQLData(self.__django_api)
            # self.gridTest.addcolumna("Carnet", "txt", "left", 50, False, 'carnet')
            # self.gridTest.addcolumna("Usuario", "key", "center", 90, False, 'username')
            # self.gridTest.addcolumna("Nombre", "txt", "left", 150, False, 'first_name')
            # self.gridTest.addcolumna("Apellido", "txt", "left", 150, False, 'last_name')
            # self.gridTest.addcolumna("Email", "txt", "left", 355, False, 'email')
            # self.datos.view = "rest-auth/user"
            # self.gridTest.addheaders()
            # self.gridTest.datasource = self.datos
#        self.gridTest.addgridrow([True, "1", "Articulo 1", "10", False])
        except AppMiscError as exp:
            showmessagebox(exp.title, exp.message)

    def getappsettings(self):
        settings = self.ldatos.getdbsettings()
        self.__lastuser = settings[0]
        self.__is_sync = settings[1]
        self.__carnet_sync = settings[2]
        self.__django_api = settings[3]



class PFinalApp(App):
    def build(self):
        self.title = 'Proyecto Final - Horario'
        return MainWindow()

if __name__ == "__main__":
    PFinalApp().run()
