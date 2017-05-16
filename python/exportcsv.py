#Protrama Python para exportar documentos de MongoDB

from pymongo import MongoClient
import csv
import os

#Conector a MongoDB
db = MongoClient().convive



#Seleccion de todos los documentos de la coleccion AVISOS


cursor = db.resueltos2017.find({}, {'_id':0, 'TIPO_INCIDENCIA_ID': 0,'TIPO_INCIDENCIA': 1,'CANAL_DE_ENTRADA_ID': 0,
                                    'CANAL_DE_ENTRADA': 0,'FECHA_DE_RECEPCION': 0,'HORA_DE_RECEPCION': 0,
                                    'FECHA_DE_RESOLUCION': 0,'HORA_DE_RESOLUCION': 0,
                                    'ORGANISMO_TRASLADO_NIVEL_1_ID': 0,
                                    'ORGANISMO_TRASLADO_NIVEL_1': 0,'ORGANISMO_TRASLADO_NIVEL_2_ID': 0,
                                    'ORGANISMO_TRASLADO_NIVEL_2': 0,'ORGANISMO_TRASLADO_NIVEL_3_ID': 0,
                                    'ORGANISMO_TRASLADO_NIVEL_3': 0,'SECCION_ID': 0,'SECCION': 0,
                                    'ANOMALIA_ID': 0,'ANOMALIA': 0,'TIPO_DE_VIAL_ID': 0,
                                    'TIPO_DE_VIAL': 0,'NOMBRE_DE_VIAL': 0,'NUMERO': 0,'CALIFICADOR': 0,
                                    'DISTRITO_ID': 0,'DISTRITO': 1,'BARRIO_ID': 0,'BARRIO': 0,
                                    'CODIGO_POSTAL': 0,'COORDENADA_OFICIAL_X': 0,'COORDENADA_OFICIAL_Y': 0,
                                    'COORDENADA_REAL_X': 0,'COORDENADA_REAL_Y': 0
                                    })

#CSV a crear
with open('avisosP.csv', 'wt') as outfile:

    #primera fila cabecera
    fields = ['TIPO_INCIDENCIA', 'DISTRITO']
    writer = csv.DictWriter(outfile, fieldnames=fields)
    writer.writeheader()

    for x in cursor:
        #Codificacion UTF-8
        row = {k.encode('utf8'): v.encode('utf8') for k, v in x.items()}
        writer.writerow(row)

