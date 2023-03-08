"""
The interface segregation principle.
"""


from abc import ABC, abstractmethod



class Movable(ABC):

    @abstractmethod
    def go(self):
        pass


class Flyable(ABC):

    @abstractmethod
    def fly(self):
        pass


class Aircraft(Flyable):

    def fly(self):
        print("Flyable")


class Car(Movable):

    def go(self):
        print("Movable")

