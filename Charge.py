import smtplib
import email.mime.multipart
import email.mime.base
from email.mime.text import MIMEText #enviar como texto el correo
#Crear la conexion SMTP
server = smtplib.SMTP('smtp.gmail.com',587)
correo = 'cesar.games.apps@gmail.com'
pas = 'bsrj iosp unvy utfs' #contraseña de aplicacion

#Inicia sesion en tu cuenta de GMAIL
server.starttls()
server.login(correo,pas)

#definir remitente y destinatario del correo electronico
enviado_por = "cesar.games.apps@gmail.com"
para = "flores.atahua.cesar@gmail.com"

#crear el mensaje del correo electronico
mensaje = email.mime.multipart.MIMEMultipart()
mensaje['From'] = enviado_por
mensaje['To'] = para
mensaje['Subject'] = "Reporte Gestores"

#añadir el cuerpo del mensaje
cuerpo = "Se adjunta el documento solicitado"
mensaje.attach(email.mime.text.MIMEText(cuerpo,'plain')) #tipo de texto plano

#añadir el documento
ruta_archivo = 'data_transformada.csv'
archivo = open(ruta_archivo,'rb')
adjunto = email.mime.base.MIMEBase('application','octect-stream')
adjunto.set_payload((archivo).read())
email.encoders.encode_base64(adjunto) #codificar a base 64
adjunto.add_header('Content-Disposition',"attachment; filename = %s" % ruta_archivo)
mensaje.attach(adjunto)

#convertir el mensaje a texto plano
texto = mensaje.as_string()

#enviar el correo
server.sendmail(enviado_por,para,texto)

#cerrar
server.quit()
