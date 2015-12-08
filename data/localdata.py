import sqlite3 as sql3
from tarea2.tarea2 import showmessagebox


class LocalData(object):
    __dspath = 'data'

    def __init__(self, dsname):
        self.__dsname = dsname
        self.__conn = sql3.Connection

    def getfilename(self):
        return "{0}/{1}".format(self.__dspath, self.__dsname)

    def conectar(self):
        """
            Inicia la coneccion con el archivo de la base de datos, lo crea de no existir este
        """
        try:
            self.__conn = sql3.connect(self.getfilename())
        except Exception as ex:
            showmessagebox('Error LocalData', ex.message)

    def getdbsettings(self):
        c = self.__conn.cursor()
        c.execute('SELECT lastuser, is_sync, carnet_sync, django_api FROM settings;')
        datos = c.fetchone()
        if datos is None:
            c.execute('INSERT INTO settings(id) VALUES (1);')
            c.execute('SELECT lastuser, is_sync, carnet_sync, django_api FROM settings;')
            datos = c.fetchone()
            self.__conn.commit()
        return datos


