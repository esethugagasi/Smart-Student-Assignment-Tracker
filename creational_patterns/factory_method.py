from creational_patterns.simple_factory import EmailNotification, SMSNotification

class NotificationCreator:
    def create(self):
        pass

class EmailCreator(NotificationCreator):
    def create(self):
        return EmailNotification()

class SMSCreator(NotificationCreator):
    def create(self):
        return SMSNotification()