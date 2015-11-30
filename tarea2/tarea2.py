from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, ListProperty, BooleanProperty
from putils import PGDatos
from api_client.sqldata import SQLData


class GridField(object):

    def __init__(self, fldheader="", fldtype="", fldalign="", flddisabled=False, fldwidth=100, flddata=''):
        self.fldHeader = fldheader
        self.fldType = fldtype
        self.fldAlign = fldalign
        self.fldDisabled = flddisabled
        self.fldWidth = fldwidth
        self.fldData = flddata
        self.fldCol = -1


class GridFields(object):
    __fields = []
    __key = -1
    __columns = 0

    @property
    def columns(self):
        return self.__columns

    @property
    def key(self):
        return self.__key

    def add(self, field):
        if field.fldCol == -1:
            field.fldCol = self.__columns
        if field.fldType == "key":
            self.__key = self.__columns
        self.__fields.append(field)
        self.__columns += 1

    def getkey(self):
        return self.__fields[self.__key]

    def getfield(self, col):
        return self.__fields[col]


class GridProyecto(FloatLayout):
    """Inicializa la clase derivada de GridLayout para el manejo de grids"""
    gHeader = GridLayout
    gBody = GridLayout
    rHeight = NumericProperty(30)
    columnas = NumericProperty()
    filas = NumericProperty()
    # colHeaders = ListProperty()
    # rowTypes = ListProperty()
    # rowAlign = ListProperty()
    # colDisabled = ListProperty()
    # colSizes = ListProperty()
    gfields = GridFields()
    __datasource = SQLData
    __rows = PGDatos()

    @property
    def datasource(self):
        return self.__rows

    @datasource.setter
    def datasource(self, value):
        self.__datasource = value
        for rowdic in self.__datasource.getapidata():
            datarow = []
            for col in range(self.gfields.columns):
                datarow.append(rowdic[self.gfields.getfield(col).fldData])
            self.addgridrow(datarow)

    def addcolumna(self, colheader, rowtype="txt", rowalign="center", colsize=200, coldisable=False, datafield=''):
        """Agrega una columna al grid"""
        # self.colHeaders.append(colheader)
        # self.rowTypes.append(rowtype)
        # self.rowAlign.append(rowalign)
        # self.colDisabled.append(coldisable)
        # self.colSizes.append(colsize)
        self.gfields.add(GridField(fldheader=colheader, fldtype=rowtype, fldalign=rowalign, flddisabled=coldisable,
                                   fldwidth=colsize, flddata=datafield))
        self.columnas = self.gfields.columns
#        self.gfields.columns += 1

    def addheaders(self):
        """Funcion que crea todas las celdas para utilizarse como encabezado de los grids"""
        gHdr = self.gHeader
        self.filas += 1
        for col in range(self.columnas):
            hdr = GridHeader()
            hdr.id = "hdr_col{0}".format(col)
            hdr.width = self.gfields.getfield(col).fldWidth
            hdr.padding = [5, 5]
            hdr.text = '[color=ffffff][b][size=16]{0}[/size][/b][/color]'.format(self.gfields.getfield(col).fldHeader)
            hdr.halign = 'center'
            hdr.valign = 'middle'
            hdr.markup = True
#            hdr.text_size = hdr.size
            gHdr.add_widget(hdr)

    def addgridrow(self, rowdata):
        """Funcion que agrega todas las celdas por cada fila de un grid de datos"""
        gBdy = self.gBody
        gBdy.bind(minimum_height=gBdy.setter('height'), minimum_width=gBdy.setter('width'))
        self.filas += 1
        for col in range(self.columnas):
            if self.gfields.getfield(col).fldType == "txt" or self.gfields.getfield(col).fldType == "key":
                gBdy.add_widget(self.getcelllabel(self.filas, col, rowdata[col], self.gfields.getfield(col).fldAlign,
                                                  self.gfields.getfield(col).fldDisabled,
                                                  self.gfields.getfield(col).fldWidth,
                                                  self.gfields.getfield(col).fldType))
            else:
                gBdy.add_widget(self.getcellchk(self.filas, col, rowdata[col], self.gfields.getfield(col).fldDisabled,
                                                self.gfields.getfield(col).fldWidth,
                                                self.gfields.getfield(col).fldType))
        self.__rows.addrow(rowdata[self.gfields.key], rowdata[:self.gfields.key] + rowdata[(self.gfields.key + 1):])

    def getcellchk(self, fila, columna, Activo, Disabled = False, Size=200, Tipo="chk"):
        """Funcion que devuelve una celda completa para manejo de checkbox"""
        cell = GridCCell()
        cell.id = "{0}_row{1}_col{2}".format(Tipo, fila, columna)
        cell.width = Size
        cell.active = Activo
        cell.disabled = Disabled
        cell.background_checkbox_disabled_down = 'atlas://data/images/defaulttheme/checkbox_on'
        cell.text_size = cell.size
        if Tipo == "bor":
            cell.bind(active=self.borradoclick)
        return cell

    def getcelllabel(self, fila, columna, Texto, Halign='left', Disabled = False, Size=200, Tipo="txt", Valign='middle'):
        """Funcion que devuelve una celda completa para manejo de etiquitas"""
        cell = GridCell()
        cell.id = "{0}_row{0}_col{1}".format(Tipo, fila, columna)
        if Tipo == "key":
            cell.key = str(Texto)
        cell.width = Size
        cell.padding = [5,5]
        cell.text = '[color=000000]{0}[/color]'.format(Texto)
        cell.halign = Halign
        cell.valign = Valign
        cell.disabled = Disabled
        cell.markup = True
        cell.text_size = cell.size
        return cell

    def borradoclick(self, cell, value):
        """Funcion que marca las celdas para el borrado"""
        cell.borrado = cell.active
        count = 1
        for cella in cell.walk_reverse(loopback=False):
            if cella.id[4:7] == 'row':
                cella.borrado = cell.active
                count += 1
            if count >= self.columnas:
                break

    def delGridRow(self, range = "All"):
        """funcion para borrar celdas de un grid"""
        childs = self.gBody.parent.children
        for ch in childs:
            for c in reversed(ch.children):
                if range == "All" or c.borrado:
                    if range != "All" and c.id == "key":
                        self._rows.delrow(c.key)
                        self.gBody.remove_widget(c)


class GridHeader(Label):
    """Inicializa la clase derivada de BoxLayout como base del encabezado de los grids"""
    height = NumericProperty(40)
    bgcolor = ListProperty([0.4, 0.4, 0.4])


class GridCell(Label):
    """Inicializa la clase derivada de BoxLayout como base de las celdas de datos del grid"""
    key = StringProperty("")
    borrado = BooleanProperty(False)
    height = NumericProperty(30)
    bgcolor = ListProperty([0.7, 0.7, 0.7])


class GridCCell(CheckBox):
    """Inicializa la clase derivada de BoxLayout como base de las celdas de datos del grid"""
    key = StringProperty("")
    borrado = BooleanProperty(False)
    height = NumericProperty(30)
    bgcolor = ListProperty([0.7, 0.7, 0.7])