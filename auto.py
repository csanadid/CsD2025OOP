from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, licence_plate, type, date, price):
        self._licence_plate = licence_plate
        self._price = price
        self._type = type
        self._date = date
        self._is_leased = False

    @abstractmethod
    def lease_car(self):
        pass

    @abstractmethod
    def unlease_car(self):
        pass