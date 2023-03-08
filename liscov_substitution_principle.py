"""
Child class objects replaces the parent class object without breaking the integrity of the application.
"""

from abc import ABC, abstractmethod


class Contact:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Notificaton(ABC):

    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):

    @abstractmehod
    def notify(self, message, email):
        print(f"Sending {message} to {email}")


class SMS(Notification):

    @abstractmethod
    def notify(self, message, phone):
        print(f"Sending {message} to {phone}")


class NotificationManager:

    def __init__(self, notification, contact):
        self.notification = notification
        self.contact = contact

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, self.contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, self.contact.phone)
        else:
            raise Exception(f"Unsupported notification format-{message}")


