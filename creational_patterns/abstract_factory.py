from creational_patterns.simple_factory import EmailNotification, SMSNotification

class NotificationFactoryAbstract:
    def create_email(self):
        pass

    def create_sms(self):
        pass

class ConcreteFactory(NotificationFactoryAbstract):
    def create_email(self):
        return EmailNotification()

    def create_sms(self):
        return SMSNotification()