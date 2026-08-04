# 23. Notification System

# Abstract:

# Notification

# Derived:

# EmailNotification
# SMSNotification
# PushNotification

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def sendNotification(self):
        pass


class EmailNotification(Notification):
    def sendNotification(self):
        print("Email notification sent")


class SMSNotification(Notification):
    def sendNotification(self):
        print("SMS notification sent")


class PushNotification(Notification):
    def sendNotification(self):
        print("Push notification sent")


e = EmailNotification()
e.sendNotification()

s = SMSNotification()
s.sendNotification()

p = PushNotification()
p.sendNotification()