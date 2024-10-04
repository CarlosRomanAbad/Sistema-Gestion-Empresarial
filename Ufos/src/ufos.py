import csv 
from datetime import datetime
from math import sqrt
from collections import namedtuple




Avistamientos = namedtuple('Avistamiento','fechahora,ciudad,estado,forma,duracion,comentarios, latitud, longitud')

def lee_avistamientos(fichero):
        
    res = []
    with open (fichero , encoding='utf-8') as f :
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for linea in lector:
            fechahora = datetime.strptime(linea[0],'%m/%d/%Y %H:%M')
            ciudad = linea[1]
            estado = linea[2]
            forma = linea[3]
            duracion = linea[4]
            comentarios = linea[5]
            latitud = float(linea[6])
            longitud = float(linea[7])
            
            tupla = Avistamientos(fechahora,ciudad,estado,forma,duracion,comentarios,latitud,longitud)
            res.append(tupla)
            
        return res
    



    

