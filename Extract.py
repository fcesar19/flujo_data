import pandas as pd
import glob2
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

extracted_data = pd.DataFrame(columns=['Instalacion','Nombre gestor','Anterior Gestor','EXPEDIENTE','Nombre Instalacion','RAZON SOCIAL','Estado en SAP','FR','CCI','TIPO DE CCI','Estado OS','Departamento','Provincia','Distrito','Dirección Operativa','Dirección Cliente','Capacidad','NOMBRE DE CONTACTO','CORREO DE CONTACTO','NUMERO CONTACTO','CONTACTO LLAMADA','Comentarios','Cancelacion','RUC'])

#for para juntar los archivos con el mismo nombre mostrado
for csv in glob2.glob("reporte_*"):

    extracted_data = extracted_data._append(extract_from_csv(csv), ignore_index=True)

#duplicado del dataframe
dddf2=extracted_data

#eliminacion de columnas no necesarias
ddf2=dddf2.drop(columns=['Anterior Gestor','EXPEDIENTE','Nombre Instalacion','CCI','TIPO DE CCI','Departamento','Provincia','Distrito','Dirección Operativa','Dirección Cliente','Capacidad','NOMBRE DE CONTACTO','CORREO DE CONTACTO','NUMERO CONTACTO','CONTACTO LLAMADA','Comentarios','RUC'], inplace=True)

#eliminacion de filas con una condicion especifica
eliminar36=dddf2[dddf2['Estado en SAP'] == '3.6)Se solicito cancelar FR pero no tiene (fin)'].index
datoseliminados=dddf2.drop(eliminar36)

#verificar valores nulos
valoresnulostotal=datoseliminados.isnull().sum()

#eliminar valores nulos
dataframeLimpio=datoseliminados.dropna()

#guardar el dataframe en un archivo csv en la misma carpeta
dataframeLimpio.to_csv('data_limpia.csv',index=False,encoding="utf-8")