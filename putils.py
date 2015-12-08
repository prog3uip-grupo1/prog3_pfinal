from kivy.uix.popup import Popup
from kivy.uix.label import Label


def showmessagebox(Titulo, Mensaje):
    """Inicializa la clase con el nombre del archivo a utilizar"""
    popup = Popup(title=Titulo, content=Label(text=Mensaje), auto_dismiss=False, size_hint=(None, None), size=(400, 200))
    popup.open()


class AppMiscError(RuntimeError):

    def __init__(self, title, message):
        self.title = title
        self.message = message
        self.args = [title, message]


class PGDatos(object):
    _dic = {}
    _nombreArchivo = ""

    def existerow(self, keyID):
        """funcion que verifica si existe un articulo en el diccionario por la llave"""
        if len(self._dic) != 0:
            if keyID in self._dic:
                return True
            else:
                return False
        else:
            return False

    def getrowdata(self, keyID):
        """funcion que devuelve la cantidad de una llave en el diccionario de articulos"""
        if self.existerow(keyID):
            return self._dic[keyID]
        else:
            return 0

    def addrow(self, keyID, data):
        """funcion que agrega un articulo al diccionario de articulos"""
        if self.existerow(keyID) == False:
            self._dic[keyID] = data

    def delrow(self, keyID):
        """funcion que remueve un articulo al diccionario de articulos"""
        if self.existerow(keyID) == True:
            del self._dic[keyID]

    def saveFile(self):
        """Funcion que escribe un diccionario de datos a un archivo de texto"""
        try:
            archivo = open(self._nombreArchivo, "wt")
            for key in sorted(self._dic):
                datos = ""
                for item in self._dic[key]:
                    datos = "{0},".format(str(item))
                archivo.write("{0}:{1}\n".format(key, datos[:-1]))
            archivo.close()
            showmessagebox("Exportar Archivo","Archivo {0} Exportado con Exito".format(self._nombreArchivo))
        except:
            showmessagebox("Exportar Archivo","Error al Guardar Archivo {0}".format(self._nombreArchivo))

    def loadFile(self):
        """Funcion que lee de un archivo de texto y rellena un diccionario de datos"""
        try:
            archivo = open(self._nombreArchivo, "rt")
            self._dic = {}
            while True:
                linea = archivo.readline()
                if not linea:
                    break
                linea = linea[:-1]
                key, lista = linea.split(":")
                if lista.strip() == "":
                    listaF = []
                else:
                    listaF = lista.split(",")
                self.addrow(key, listaF)
        except:
            showmessagebox("Importar Archivo","Error al Cargar Archivo {0}".format(self._nombreArchivo))

    def getDiccionario(self):
        """Funcion que devuelve el diccionario de datos de la clase"""
        dict = self._dic
        return dict