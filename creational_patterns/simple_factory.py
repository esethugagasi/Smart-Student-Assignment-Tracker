class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return "Email sent"

class SMSNotification(Notification):
    def send(self):
        return "SMS sent"

class NotificationFactory:
    @staticmethod
    def create_notification(type):
        if type == "email":
            return EmailNotification()
        elif type == "sms":
            return SMSNotification()