from notificator_email import NotificatorEmail
from notificator_sms import NotificatorSMS
from notificator_interface import NotificatorInterface


# class ClientService:
#     def __init__(self, notificator: NotificatorEmail) -> None:
#         self.notificator = notificator

#     def send(self, message: str) -> None:
#         self.notificator.send_notification(message)


# class ClientService:
#     def __init__(self, notificator: NotificatorSMS) -> None:
#         self.notificator = notificator

#     def send(self, message: str) -> None:
#         self.notificator.send_notification(message)


class ClientService:
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator

    def send(self, message: str) -> None:
        self.notificator.send_notification(message)


notificatorEmail = NotificatorEmail()
notificatorSMS = NotificatorSMS()

clienteService1 = ClientService(notificatorEmail)
clienteService1.send('Hello, World!')  # Sending Email: Hello, World!

clienteService2 = ClientService(notificatorSMS)
clienteService2.send('Hello, World!')  # Sending SMS: Hello, World!
