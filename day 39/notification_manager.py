from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.account_sid = 'example'
        self.auth_token = 'example'
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, price, destiny, departure, arrival):
        message = self.client.messages.create(
            body=f"Alerta de preço baixo! Voos para {destiny} por R${price}. Partida: {departure}, Retorno: {arrival}.",
            from_="+19034005347",
            to="+5531989056191"
        )
        print(f"SMS enviado: {message.sid}")