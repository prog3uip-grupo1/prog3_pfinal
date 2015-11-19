from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, ListProperty, BooleanProperty


class GridProyecto(GridLayout):
    """Inicializa la clase derivada de GridLayout para el manejo de grids"""
    rHeight = 30
    columnas = NumericProperty()
    filas = NumericProperty()
    colHeaders = ListProperty()
    rowTypes = ListProperty()
    rowAlign = ListProperty()
    colDisabled = ListProperty()
    colSizes = ListProperty()

    def addcolumna(self, colheader, rowtype="txt", rowalign="center", colsize=200, coldisable=False):
        """Agrega una columna al grid"""
        self.colHeaders.append(colheader)
        self.rowTypes.append(rowtype)
        self.rowAlign.append(rowalign)
        self.colDisabled.append(coldisable)
        self.colSizes.append(colsize)
        self.columnas += 1

    def addheaders(self):
        """Funcion que crea todas las celdas para utilizarse como encabezado de los grids"""
        self.bind(minimum_height=self.setter('height'), minimum_width=self.setter('width'))
        self.filas += 1
        for col in range(self.columnas):
            hdr = GridHeader()
            hdr.id = "hdr_col{0}".format(col)
            hdr.width = self.colSizes[col]
            clabel = Label()
            clabel.padding = [5, 5]
            clabel.text = '[color=ffffff][b][size=16]{0}[/size][/b][/color]'.format(self.colHeaders[col])
            clabel.halign = 'center'
            clabel.valign = 'middle'
            clabel.markup = True
            clabel.text_size = hdr.size
            hdr.add_widget(clabel)
            self.add_widget(hdr)


class GridHeader(BoxLayout):
    """Inicializa la clase derivada de BoxLayout como base del encabezado de los grids"""
    height = NumericProperty(40)
    bgcolor = ListProperty([0.4, 0.4, 0.4])


class GridRow(BoxLayout):
    """Inicializa la clase derivada de BoxLayout como base de las celdas de datos del grid"""
    key = StringProperty("")
    borrado = BooleanProperty(False)
    height = NumericProperty(30)
    bgcolor = ListProperty([0.7, 0.7, 0.7])
