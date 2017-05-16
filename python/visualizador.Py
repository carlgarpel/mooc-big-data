from math import pi

from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper, LogColorMapper
from bokeh.plotting import figure
from bokeh.sampledata.unemployment1948 import data 
from bokeh.palettes import BrBG9
    
import sys
import csv
import numpy as np 

year = ["2017"]
district =[]
year = []
rate = []

'''
Gestión de datos para una columna
en caso de tener varias columnas YEARS se transforma en
una matriz
'''
for line in sys.stdin:
    data_csv = line.strip().split("\t")
    if len(data_csv) == 2:
        distrito, avisos_tot = data_csv
        district.append(distrito)
        rate.append("2017")

# Mapeador color-valor
mapper = LinearColorMapper(palette="BrBG9",  low=float(0), high = float(70000))

# Configuración del gráfico para una columna
source = ColumnDataSource( data=dict(district=district, year=year, rate=rate))

# Configuración de la paleta de herramientas Bokeh
TOOLS = "hover, save, pan, box_zoom, wheel_zoom"

# Configuración del gráfico de barras coloreadas
p = figure(title="Avisos emitidos y resueltos Madris (2017)",
            x_range=year, y_range=list(reversed(district)),
            x_axis_location="above", plot_width=900, plot_height=400,
            tools=TOOLS)
p.grid.grid_line_color = ''
p.axis.axis_line_color = ''
p.axis.major_tick_line_color = ''
p.axis.major_label_text_font_size = "5pt"
p.axis.major_label_standoff = 0
p.axis.major_label_orientation = pi / 3

p.rect(x="year", y="district", width=1, height=1,
        source=source,
        fill_color={'field': 'rate', 'transform': mapper},
        line_color=None)

p.select_one(HoverTool).tooltips = [
    ('district', '@district'),
    ('rate', '@rate')
]

# Mostrar el gráfico
show(p)

