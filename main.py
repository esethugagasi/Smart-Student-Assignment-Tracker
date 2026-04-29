from creational_patterns.abstract_factory import ConcreteFactory

factory = ConcreteFactory()

email = factory.create_email()
sms = factory.create_sms()

print(email.send())
print(sms.send())