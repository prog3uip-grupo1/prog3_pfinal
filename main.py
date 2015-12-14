__version__ = "1.0"
import tarea1.tarea1
import tarea2.tarea2 as ui
import tarea4.tarea4
import tarea5.tarea5
from api_client.sqldata import SQLData
from kivy.app import App
#from kivy.config import Config
from kivy.properties import StringProperty, ObjectProperty
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
    __api_success = False

    ldatos = LocalData('pfinal.sqlite3')
    datos_api = SQLData
    horario_grid = ui.GridProyecto
    texto = StringProperty("Proyecto Final Test")
    manager = ObjectProperty(None)
    carnet_sync = ObjectProperty(None)
    carnet_text = ObjectProperty(None)
    api_url = ObjectProperty(None)
    estudiante_form = ObjectProperty(None)

    nombredb = ObjectProperty(None)
    apellidodb = ObjectProperty(None)
    correodb = ObjectProperty(None)

    def __init__(self):
        try:

            FloatLayout.__init__(self)
            self.ldatos.conectar()
            self.getappsettings()

            self.datos_api = SQLData(self.__django_api)
            #self.__api_success = datos_api.testapi()
            self.horario_grid.addcolumna("Codigo", "txt", "left", .15, False, 'codigo')
            self.horario_grid.addcolumna("Materia", "key", "center", .55, False, 'nombre')
            self.horario_grid.addcolumna("Dia", "txt", "left", .05, False, 'dia')
            self.horario_grid.addcolumna("Hora", "txt", "left", .15, False, 'hora')
            self.horario_grid.addcolumna("Aula", "txt", "left", .1, False, 'aula')
            self.horario_grid.addheaders()
            # self.gridTest.datasource = self.datos
#        self.gridTest.addgridrow([True, "1", "Articulo 1", "10", False])
            if not self.__is_sync or self.__carnet_sync == '':
                self.showloginform()
            else:
                self.showhorario()
        except AppMiscError as exp:
            showmessagebox(exp.title, exp.message)

    def getappsettings(self):
        settings = self.ldatos.getdbsettings()
        self.__lastuser = settings[0]
        self.__is_sync = settings[1]
        self.__carnet_sync = settings[2]
        self.__django_api = settings[3]

    def setappsettings(self):
        self.ldatos.setdbsettings(self.__lastuser, self.__is_sync, self.__carnet_sync, self.__django_api)

    def showajustes(self):
        self.getappsettings()
        self.carnet_text.text = self.__carnet_sync
        self.api_url.text = self.__django_api
        self.manager.current = 'ajustes'

    def saveajustes(self, carnet_text, api_url):
        if carnet_text != '':
            self.__is_sync = True
        else:
            self.__is_sync = False
        self.__carnet_sync = carnet_text
        self.__django_api = api_url
        self.datos_api = SQLData(self.__django_api)
        self.setappsettings()

    def showloginform(self):
        self.carnet_sync.text = self.__carnet_sync
        self.manager.current = 'carnet'

    def showhorario(self):
        if not self.__is_sync or self.__carnet_sync == '':
            self.showloginform()
        else:
            self.estudiante_form.title = 'Estudiante ' + self.__carnet_sync
            if self.ldatos.is_exist(self.__carnet_sync):
                estudiante = self.ldatos.getestudiante(self.__carnet_sync)
                self.nombredb.texto = estudiante[1]
                self.apellidodb.texto = estudiante[2]
                self.correodb.texto = estudiante[3]
                if self.ldatos.is_existhorario(self.__carnet_sync):
                    horario = self.ldatos.gethorario(self.__carnet_sync)
                    self.horario_grid.datasource = horario
            self.manager.current = 'horario'

    def syncronizar(self, carnet):
        try:
            if carnet != '':
                self.datos_api.view = 'estudiante/{0}'.format(carnet)
                resultados = self.datos_api.getapidata()
                if self.ldatos.is_exist(resultados['carnet']):
                    self.ldatos.delestudiante(resultados['carnet'])

                if self.ldatos.addestudiante(resultados['carnet'], resultados['nombre'], resultados['apellido'], resultados['email']):
                    self.datos_api.view = 'horarios/?estudiante={0}'.format(carnet)
                    if self.ldatos.is_existhorario(resultados['carnet']):
                        self.ldatos.delhorarios(resultados['carnet'])
                    horarios = self.datos_api.getapidatafiltered()
                    for horario in horarios:
                        self.ldatos.addhorario(horario['id'], horario['estudiante'], horario['codmateria'], horario['materia'], horario['dia'], horario['hora'], horario['aula'], horario['profesor'], horario['tiempo'],)
                    self.__is_sync = True
                    self.__carnet_sync = resultados['carnet']
                    self.ldatos.setdbsettings(self.__lastuser, self.__is_sync, self.__carnet_sync, self.__django_api)
                    self.showhorario()
        except AppMiscError as exp:
            ui.showmessagebox(exp.title, exp.message, 2)


class PFinalApp(App):
    def build(self):
        self.title = 'Proyecto Final - Horario'
        return MainWindow()

if __name__ == "__main__":
    PFinalApp().run()
