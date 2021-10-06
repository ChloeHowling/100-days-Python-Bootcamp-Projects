from twilio.rest import Client
import smtplib, ssl

OWM_END = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "9d4bcb2365a27f5ce070ac4e85e4ff97"

TWILIO_SID = "AC4db021befdfdeb7a7d313888254eaefe"
TWILIO_AUTH_TOKEN = "e5878590c03c07a478f1331a71846819"
TWILIO_VIRTUAL_NUMBER = "+19514325275"
TWILIO_VERIFIED_NUMBER = "+18015778961"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email_address, message):
        port = 465
        password = "Jilljill6"
        context = ssl.create_default_context()
        send_email = "elizabethwangwang@gmail.com"

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(send_email, password)
            server.sendmail(
                from_addr=send_email,
                to_addrs=email_address,
                msg=message
            )
