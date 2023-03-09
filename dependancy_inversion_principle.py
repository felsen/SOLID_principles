"""
High level module should not depend on the low level modules, both should depend on the abstractions.

Abstraction should not depend on details, Details should depend on the abstractions.
"""


from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulp(Switchable):

    def turn_on(self):
        print("Bulp is turned on")

    def turn_off(self):
        print("Bulp is turned off")


class PowerSwitch:

    def __init__(self, client):
        self.client = client
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


class Fan(Switchable):

    def turn_on(self):
        print("Fan: Turn On")

    def turn_off(self):
        print("Fan: Turn Off")

