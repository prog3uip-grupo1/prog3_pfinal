import re
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics import Line, Rectangle, Color
from kivy.properties import StringProperty, NumericProperty, ListProperty, BooleanProperty, ObjectProperty
from putils import PGDatos
from api_client.sqldata import SQLData


class LabelPopup(Label):
    """
        Objeto de texto principal de la aplicacion, permite modificar el color de fondo, color de texto
        y agregar bordes
    """
    __texto = StringProperty('')
    __textocolor = StringProperty('FFFFFF')
    __bordercolor = ListProperty([])
    __backcolor = ListProperty([])
    __borderwidth = NumericProperty(1)

    def __init__(self, **kwargs):
        """
            Sobre escribe el constructor de objeto Label
        """

        if 'texto' in kwargs:
            self.texto = kwargs['texto']
        if 'textocolor' in kwargs:
            self.textocolor = kwargs['textocolor']
        if 'backcolor' in kwargs:
            self.backcolor = kwargs['backcolor']
        if 'bordercolor' in kwargs:
            self.bordercolor = kwargs['bordercolor']
        if 'borde' in kwargs:
            self.borde = kwargs['borde']

        self.line = ObjectProperty(None)
        self.linecolor = ObjectProperty(None)
        self.fondo = ObjectProperty(None)
        self.fondocolor = ObjectProperty(None)
        Label.__init__(self, **kwargs)

    @property
    def texto(self):
        """
            Propiedad texto: contiene el texto del objeto
        """
        return self.__texto

    @texto.setter
    def texto(self, value):
        self.text = '[color={0}]{1}[/color]'.format(self.__textocolor, value)
        self.markup = True
        self.__texto = value

    @property
    def textocolor(self):
        """
            Propiedad textocolor: contiene el color del texto en formato RGB Hex
        """
        return self.__textocolor

    @textocolor.setter
    def textocolor(self, value):
        self.text = '[color={0}]{1}[/color]'.format(value, self.__texto)
        self.markup = True
        self.__textocolor = value

    @property
    def borde(self):
        """
            Propiedad bordercolor: contiene el color del borde en formato RGB Dec list
        """
        return self.__borderwidth

    @borde.setter
    def borde(self, value):
        with self.canvas.after:
            self.canvas.after.clear()
            self.linecolor = Color(self.__bordercolor)
            self.line = Line(rectangle=[self.x + self.__borderwidth, self.y + self.__borderwidth, self.width - self.__borderwidth * 2, self.height - self.__borderwidth * 2], width=value)
        self.__borderwidth = value

        self.bind(pos=self.update_canvas, size=self.update_canvas)


    @property
    def bordercolor(self):
        """
            Propiedad bordercolor: contiene el color del borde en formato RGB Dec list
        """
        return self.__bordercolor

    @bordercolor.setter
    def bordercolor(self, value):
        with self.canvas.after:
            self.canvas.after.clear()
            self.linecolor = Color(value)
            self.line = Line(rectangle=[self.x, self.y, self.width-1, self.height-6], width=self.__borderwidth)
        self.__bordercolor = value

        self.bind(pos=self.update_canvas, size=self.update_canvas)

    @property
    def backcolor(self):
        """
            Propiedad backcolor: contiene el color del fondo en formato RGB Dec List
        """
        return self.__backcolor

    @backcolor.setter
    def backcolor(self, value):
        with self.canvas.before:
            self.canvas.before.clear()
            self.fondocolor = Color(value)
            self.fondo = Rectangle(pos=[self.x, self.y], size=[self.width, self.height])
        self.__backcolor = value

        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        """
            Actualiza el borde y el fondo de el objeto cada vez que cambie de tamanio o lugar
        """
        if len(self.bordercolor) > 0:
            self.linecolor.rgb = self.bordercolor
            self.line.rectangle = [self.x, self.y, self.width, self.height]
        if len(self.backcolor) > 0:
            self.fondocolor.rgb = self.backcolor
            self.fondo.pos = self.pos
            self.fondo.size = [self.width, self.height]


    def textocolorrgb(self, value):
        """
            Funcion para convertir colores RGB de Hex a Dec List
        """
        return convertorgb(value)



class LabelProyecto(LabelPopup):
    """
        Texto derivado de LabelPopup para el uso del resto de la aplicacion
    """
    bgcolor = ListProperty([0, 0, 0])


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
    #rHeight = NumericProperty(30)
    columnas = NumericProperty()
    filas = NumericProperty()
    gfields = GridFields()
    __datasource = SQLData
    __rows = PGDatos()
    __rheight = NumericProperty(30)
    __gcells = ListProperty([])
    __ghdrs = ListProperty([])

    @property
    def rHeight(self):
        return self.__rheight

    @rHeight.setter
    def rHeight(self, value):
        self.__rheight = value
        self.bind(pos=self.updaterheight, size=self.updaterheight)

    def updaterheight(self, *args):
        #self.gHeader.height = self.height * .1
        self.gHeader.row_default_height = self.height * .1
        self.gBody.row_default_height = self.height * .1
        for cell in self.__gcells:
            cell.font_size = self.rHeight * .30
        for hdrs in self.__ghdrs:
            hdrs.font_size = self.rHeight * .30

    @property
    def datasource(self):
        return self.__rows

    @datasource.setter
    def datasource(self, value):
        self.__datasource = value
        self.delGridRow()
        self.__gcells = []
        for rowdic in self.__datasource:
            datarow = []
            for col in range(self.gfields.columns):
                datarow.append(rowdic[self.gfields.getfield(col).fldCol])
            self.addgridrow(datarow)


    def addcolumna(self, colheader, rowtype="txt", rowalign="center", colsize=200, coldisable=False, datafield=''):
        """Agrega una columna al grid"""
        self.gfields.add(GridField(fldheader=colheader, fldtype=rowtype, fldalign=rowalign, flddisabled=coldisable,
                                   fldwidth=colsize, flddata=datafield))
        self.columnas = self.gfields.columns

    def addheaders(self):
        """Funcion que crea todas las celdas para utilizarse como encabezado de los grids"""
        gHdr = self.gHeader
        self.filas += 1
        for col in range(self.columnas):
            hdr = GridHeader()
            hdr.id = "hdr_col{0}".format(col)
            hdr.size_hint_x = self.gfields.getfield(col).fldWidth
            hdr.text = '[color=ffffff]{0}[/color]'.format(self.gfields.getfield(col).fldHeader)
            hdr.halign = 'center'
            hdr.valign = 'middle'
            hdr.markup = True
            hdr.bgcolor= [.0509, .4275, .7137]
            hdr.font_size = self.rHeight * .30
            #hdr.text_size = hdr.size
            self.__ghdrs.append(hdr)
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

    def getcellchk(self, fila, columna, Activo, Disabled = False, Size=200.0, Tipo="chk"):
        """Funcion que devuelve una celda completa para manejo de checkbox"""
        cell = GridCCell()
        cell.id = "{0}_row{1}_col{2}".format(Tipo, fila, columna)
        cell.size_hint_x = Size
        #cell.width = Size
        cell.active = Activo
        cell.disabled = Disabled
        cell.background_checkbox_disabled_down = 'atlas://data/images/defaulttheme/checkbox_on'
        cell.text_size = cell.size
        if Tipo == "bor":
            cell.bind(active=self.borradoclick)
        return cell

    def getcelllabel(self, fila, columna, Texto, Halign='left', Disabled = False, Size=200.0, Tipo="txt", Valign='middle'):
        """Funcion que devuelve una celda completa para manejo de etiquitas"""
        cell = GridCell()
        cell.id = "{0}_row{0}_col{1}".format(Tipo, fila, columna)
        if Tipo == "key":
            cell.key = str(Texto)
        cell.size_hint_x = Size
        #cell.width = Size
        #cell.padding = [5,5]
        cell.text = '[color=000000]{0}[/color]'.format(Texto)
        cell.halign = Halign
        cell.valign = Valign
        cell.disabled = Disabled
        cell.markup = True
        cell.font_size = self.rHeight * .30
        self.__gcells.append(cell)
        #cell.text_size = cell.size
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


def convertorgb(color):
    """
        Funcion que convierte de codigo de colores de Hex a RGB decimal
    """
    __tmplist = []
    if len(color) == 6:
        __tmplist.append(float(int(color[0:2], 16)) / 255.0)
        __tmplist.append(float(int(color[2:4], 16)) / 255.0)
        __tmplist.append(float(int(color[4:6], 16)) / 255.0)
        return __tmplist
    else:
        return [0, 0, 0]




class LabelSPopup(LabelPopup):
    """
        Objeto derivado de LabelPopup
    """
    pass


class PopupParcial(Popup):
    """
        Objeto que cambia el fondo de los Popup en la aplicacion
    """
    pass


class PopupContent(FloatLayout):
    """
        Objeto de contenido de los Popup de la Aplicacion, agrega una imagen en conjunto de un Label con
        su fondo y bordes
    """
    mensaje = ObjectProperty(None)
    texto = StringProperty('')
    textocolor = StringProperty('FFFFFF')
    backcolor = ListProperty([])

    def __init__(self, **kwargs):
        """
            Sobre escribe constructor de la clase para agregar funcionalidad en caso de configurar algunas
            propiedades
        """
        if 'texto' in kwargs:
            self.texto = kwargs['texto']
        if 'textocolor' in kwargs:
            self.textocolor = kwargs['textocolor']
        if 'backcolor' in kwargs:
            self.backcolor = kwargs['backcolor']

        FloatLayout.__init__(self, **kwargs)
        self.mensaje.texto = self.texto
        self.mensaje.textocolor = self.textocolor
        self.mensaje.bordercolor = self.mensaje.textocolorrgb(self.textocolor)
        self.mensaje.backcolor = self.backcolor

def showmessagebox(Titulo, Mensaje, Tipo=1):
    """
        Funcion que despliega un Popup Window para mensajes de la aplicacion
    """
    label = ObjectProperty(None)
    if Tipo == 0:
        label = LabelPopup(texto=Mensaje)
    if Tipo == 1:
        label = PopupContent(texto=Mensaje, textocolor='006600', backcolor=[.6, 1, .6])
    if Tipo == 2:
        label = PopupContent(texto=Mensaje, textocolor='660000', backcolor=[1, .6, .6])
    popup = PopupParcial(title=Titulo, content=label, auto_dismiss=True, size_hint=(.9, .3))
    popup.open()


class ButtonDropDown(Button):
    """
        Objeto para el uso del dropdown, agrega funcionalidad de datos
    """
    data = ListProperty()

    def __init__(self, data , **kw):
        """
            Sobreescribe constructor para agregar propiedad data
        """
        self.data = data
        super(ButtonDropDown, self).__init__(**kw)


class DropParcial(Button):
    """
        Objeto que modifica un boton para agregarle funciones de dropdown y manejo de datos
    """
    __datasource = ListProperty()
    origen = StringProperty('')
    sector = StringProperty('')
    options = ListProperty()

    @property
    def datasource(self):
        """
            Propiedad datasource: obtiene datos de la fuente de datos y los agrega al dropdown utilizando
            botones
        """
        return self.__datasource

    @datasource.setter
    def datasource(self, value):
        for row in value:
            self.options.append(ButtonDropDown(data=row, text=str(row[1]), size_hint_y=None, height=self.height))
        self.__datasource = value

    def __init__(self, **kw):
        """
            Sobreescribe constructor y agrega un dropdown al boton principal
        """
        ddn = self.drop_down = DropDown()
        ddn.bind(on_select=self.on_select)
        super(DropParcial, self).__init__(**kw)

    def on_options(self, instance, value):
        """
            Evento que se acttiva al agregar opciones al dropdown
        """
        ddn = self.drop_down
        ddn.clear_widgets()
        for widg in value:
            widg.bind(on_release=lambda btn: ddn.select(btn.data))
            ddn.add_widget(widg)

    def on_select(self, *args):
        """
            Evento que se activa al seleccionar una opcion en el dropdown
        """
        self.text = args[1][1]
        self.origen = args[1][2]
        self.sector = args[1][3]

    def on_touch_up(self, touch):
        """
            Evento que despliega el dropdown al apretar el boton principal
        """
        if touch.grab_current == self:
            self.drop_down.open(self)
        return super(DropParcial, self).on_touch_up(touch)


class TextBoxProyecto(TextInput):
    """Clase derivada de TextInput para Insertar datos alfanumericos en mayuscula con espacios"""
    __is_numeric = BooleanProperty(False)
    __is_upper_case = BooleanProperty(False)
    __is_lower_case = BooleanProperty(False)
    __accept_spaces = BooleanProperty(True)
    __is_password = BooleanProperty(False)

    __pattern = '[^a-zA-Z0-9_/:. ]'

    def __init__(self, **kwargs):
        super(TextBoxProyecto, self).__init__(**kwargs)

    @property
    def is_password(self):
        return self.__is_password

    @is_password.setter
    def is_password(self, value):
        if value:
            self.__pattern = '[ ]'
        elif self.__is_numeric:
            self.__pattern = '[^0-9]'
        elif self.__accept_spaces:
            self.__pattern = '[^a-zA-Z0-9_/:. ]'
        else:
            self.__pattern = '[^a-zA-Z0-9_]'

        self.password = value
        self.__is_password = value

    @property
    def is_numeric(self):
        return self.__is_numeric

    @is_numeric.setter
    def is_numeric(self, value):
        if self.__is_password:
            self.__pattern = '[ ]'
            self.__accept_spaces = False
        elif value:
            self.__pattern = '[^0-9]'
            self.__accept_spaces = False
        elif self.__accept_spaces:
            self.__pattern = '[^a-zA-Z0-9_ ]'
        else:
            self.__pattern = '[^a-zA-Z0-9_]'
        self.__is_numeric = value

    @property
    def is_upper_case(self):
        return self.__is_upper_case

    @is_upper_case.setter
    def is_upper_case(self, value):
        self.__is_upper_case = value

    @property
    def is_lower_case(self):
        return self.__is_lower_case

    @is_lower_case.setter
    def is_lower_case(self, value):
        self.__is_lower_case = value

    @property
    def accept_spaces(self):
        return self.__accept_spaces

    @accept_spaces.setter
    def accept_spaces(self, value):
        if self.__is_password:
            self.__pattern = '[ ]'
            value = False
        elif self.__is_numeric:
            self.__pattern = '[^0-9]'
            value = False
        elif value:
            self.__pattern = '[^a-zA-Z0-9_ ]'
        else:
            self.__pattern = '[^a-zA-Z0-9_]'
        self.__is_numeric = value
        self.__accept_spaces = value

    def insert_text(self, substring, from_undo=False):
        """Reemplaza la funcion inicial y filtra los caracteres y los convierte en mayuscula"""
        pat = re.compile(self.__pattern)
        s = re.sub(pat, '', substring)
        if self.__is_upper_case and not self.__is_password:
            s = s.upper()
        elif self.__is_lower_case and not self.__is_password:
            s = s.lower()
        return super(TextBoxProyecto, self).insert_text(s, from_undo=from_undo)


class VentanaProyecto(FloatLayout):
    __bordercolor = ListProperty([])
    __backcolor = ListProperty([])
    __borderwidth = NumericProperty(1)

    otitle = ObjectProperty(None)
    obody = ObjectProperty(None)

    children = ListProperty([])

    def __init__(self, **kwargs):
        if 'title' in kwargs:
            self.title = kwargs['title']
        if 'backcolor' in kwargs:
            self.backcolor = kwargs['backcolor']
        if 'bordercolor' in kwargs:
            self.bordercolor = kwargs['bordercolor']
        if 'borde' in kwargs:
            self.borde = kwargs['borde']

        self.line = ObjectProperty(None)
        self.linecolor = ObjectProperty(None)
        self.fondo = ObjectProperty(None)
        self.fondocolor = ObjectProperty(None)

        super(VentanaProyecto,self).__init__(**kwargs)

    @property
    def title(self):
        return self.otitle.texto

    @title.setter
    def title(self, value):
        self.otitle.texto = value

    @property
    def titlecolor(self):
        return self.otitle.textocolor

    @titlecolor.setter
    def titlecolor(self, value):
        self.otitle.textocolor = value

    @property
    def titlebackcolor(self):
        return self.otitle.backcolor

    @titlebackcolor.setter
    def titlebackcolor(self, value):
        self.otitle.backcolor = value

    @property
    def body(self):
        return self.obody

    @body.setter
    def body(self, value):
        self.obody.clear_widgets(children=None)
        self.obody.add_widget(value)

    @property
    def bordercolor(self):
        """
            Propiedad bordercolor: contiene el color del borde en formato RGB Dec list
        """
        return self.__bordercolor

    @bordercolor.setter
    def bordercolor(self, value):
        with self.body.canvas.after:
            self.body.canvas.after.clear()
            self.linecolor = Color(value)
            self.line = Line(rectangle=[self.body.x + self.__borderwidth, self.body.y + self.__borderwidth, self.body.width - self.__borderwidth * 2, self.body.height - self.__borderwidth * 2], width=self.__borderwidth)
        self.__bordercolor = value

        self.body.bind(pos=self.update_canvas, size=self.update_canvas)

    @property
    def borde(self):
        """
            Propiedad bordercolor: contiene el color del borde en formato RGB Dec list
        """
        return self.__borderwidth

    @borde.setter
    def borde(self, value):
        with self.body.canvas.after:
            self.body.canvas.after.clear()
            self.linecolor = Color(self.__bordercolor)
            self.line = Line(rectangle=[self.body.x + self.__borderwidth, self.body.y + self.__borderwidth, self.body.width - self.__borderwidth * 2, self.body.height - self.__borderwidth * 2], width=value)
        self.__borderwidth = value

        self.body.bind(pos=self.update_canvas, size=self.update_canvas)

    @property
    def backcolor(self):
        """
            Propiedad backcolor: contiene el color del fondo en formato RGB Dec List
        """
        return self.__backcolor

    @backcolor.setter
    def backcolor(self, value):
        with self.body.canvas.before:
            self.body.canvas.before.clear()
            self.fondocolor = Color(value)
            self.fondo = Rectangle(pos=[self.body.x, self.body.y], size=[self.body.width, self.body.height])
        self.__backcolor = value

        self.body.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        """
            Actualiza el borde y el fondo de el objeto cada vez que cambie de tamanio o lugar
        """
        if len(self.bordercolor) > 0:
            self.linecolor.rgb = self.bordercolor
            self.line.rectangle = [self.body.x + self.__borderwidth, self.body.y + self.__borderwidth, self.body.width - self.__borderwidth * 2, self.body.height - self.__borderwidth * 2]
        if len(self.backcolor) > 0:
            self.fondocolor.rgb = self.backcolor
            self.fondo.pos = self.body.pos
            self.fondo.size = [self.body.width, self.body.height]
