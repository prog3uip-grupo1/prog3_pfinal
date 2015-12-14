import sqlite3 as sql3
from tarea2.tarea2 import showmessagebox


class LocalData(object):
    """
        Clase que maneja datos de la base de datos local en sqlite3
    """
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

    def setdbsettings(self, lastuser, is_sync, canet_sync, django_api):
        try:
            c = self.__conn.cursor()
            t = (lastuser, is_sync, canet_sync, django_api,)
            c.execute('UPDATE settings SET lastuser=?, is_sync=?, carnet_sync=?, django_api=? WHERE id=1;', t)
            self.__conn.commit()
        except Exception:
            return False
        return True

    def is_exist(self, carnet):
        try:
            c = self.__conn.cursor()
            t = (carnet,)
            c.execute('SELECT 1 FROM estudiantes WHERE carnet=?;', t)
            datos = c.fetchone()
            self.__conn.commit()
            if len(datos) > 0:
                return True
            else:
                return False
        except Exception:
            return False


    def delestudiante(self, carnet):
        try:
            c = self.__conn.cursor()
            t = (carnet,)
            c.execute('DELETE FROM estudiantes WHERE carnet=?;', t)
            self.__conn.commit()
        except Exception:
            return False
        return True

    def addestudiante(self, carnet, nombre, apellido, email):
        try:
            c = self.__conn.cursor()
            t = (carnet, nombre, apellido, email,)
            c.execute('INSERT INTO estudiantes(carnet, nombre, apellido, email) VALUES(?, ?, ?, ?);', t)
            self.__conn.commit()
        except Exception:
            return False
        return True

    def is_existhorario(self, carnet):
        try:
            c = self.__conn.cursor()
            t = (carnet,)
            c.execute('SELECT 1 FROM horario WHERE carnet=?;', t)
            datos = c.fetchone()
            self.__conn.commit()
            if len(datos) > 0:
                return True
            else:
                return False
        except Exception:
            return False

    def delhorarios(self, carnet):
        try:
            c = self.__conn.cursor()
            t = (carnet,)
            c.execute('DELETE FROM horario WHERE carnet=?;', t)
            self.__conn.commit()
        except Exception:
            return False
        return True

    def addhorario(self, id, carnet, codigo, nombre, dia, hora, aula, profesor, tiempo):
        try:
            c = self.__conn.cursor()
            t = (id, carnet, codigo, nombre, self.changedia(dia), hora, aula, profesor, tiempo,)
            c.execute('INSERT INTO horario(id, carnet, codigo, nombre, dia, hora, aula, profesor, tiempo) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);', t)
            self.__conn.commit()
        except Exception:
            return False
        return True

    def changedia(self, value):
        dias = {0: 'L', 1: 'M', 2: 'W', 3: 'J', 4: 'V', 5: 'S', 6: 'D',}
        return dias[value]

    def getestudiante(self, carnet):
        c = self.__conn.cursor()
        t = (carnet,)
        c.execute('SELECT carnet, nombre, apellido, email FROM estudiantes WHERE carnet=?;', t)
        datos = c.fetchone()
        self.__conn.commit()
        return datos

    def gethorario(self, carnet):
        c = self.__conn.cursor()
        t = (carnet,)
        c.execute('SELECT codigo, nombre, dia, hora, aula FROM horario WHERE carnet=?;', t)
        datos = c.fetchall()
        self.__conn.commit()
        return datos