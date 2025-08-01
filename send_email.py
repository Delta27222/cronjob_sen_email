import yagmail
import os

# Es recomendable usar variables de entorno para las credenciales
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

try:
    yag = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASS)
    yag.send(
        to='destinatario@ejemplo.com',
        subject='Correo automático de mi cron job',
        contents='Hola, este es un correo de prueba desde Python.'
    )
    print("Correo enviado exitosamente.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")