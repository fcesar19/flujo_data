import pandas as pd
import numpy as np

#extraer el dataframe del archivo limpio
nueva_extraccion = pd.read_csv("data_limpia.csv")

#print(nueva_extraccion)

#crear una columna calculada donde se muestre los 2 ultimos digitos
nueva_extraccion['caracter'] = nueva_extraccion['FR'].str[-2:]

#crear una columna calculada donde se muestre los 4 primeros digitos
nueva_extraccion['Codigo_OSI']=nueva_extraccion['FR'].str[0:4]

#lista de condiciones
condiciones = [
    (nueva_extraccion['caracter']=='01'),(nueva_extraccion['caracter']=='02'),
    (nueva_extraccion['caracter']=='03'),(nueva_extraccion['caracter']=='04'),
    (nueva_extraccion['caracter']=='05'),(nueva_extraccion['caracter']=='06'),
    (nueva_extraccion['caracter']=='07'),(nueva_extraccion['caracter']=='08'),
    (nueva_extraccion['caracter']=='09'),(nueva_extraccion['caracter']=='10'),
    (nueva_extraccion['caracter']=='11'),(nueva_extraccion['caracter']=='12'),
    (nueva_extraccion['caracter']=='13'),(nueva_extraccion['caracter']=='14'),
    (nueva_extraccion['caracter']=='15'),(nueva_extraccion['caracter']=='16'),
    (nueva_extraccion['caracter']=='17'),(nueva_extraccion['caracter']=='18'),
    (nueva_extraccion['caracter']=='19'),(nueva_extraccion['caracter']=='20'),
    (nueva_extraccion['caracter']=='21'),(nueva_extraccion['caracter']=='22'),
    (nueva_extraccion['caracter']=='23'),(nueva_extraccion['caracter']=='24'),
]
#resultado de las condiciones
resultados=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]

#columna creada mediante condiciones especificas
nueva_extraccion['añio_emitida'] = np.select(condiciones,resultados)

print(nueva_extraccion)

#guardar la data transformada en un archivo
nueva_extraccion.to_csv('data_transformada.csv',index=False,encoding="utf-8")

