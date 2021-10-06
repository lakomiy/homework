from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started = False

    def __init__(self, weight=0, fuel=0, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not Vehicle.started:
            if self.fuel > 0:
                Vehicle.started = True
            else:
                raise exceptions.LowFuelError()
    def move(self):
        if self.weight / self.fuel_consumption <= self.fuel:
            self.fuel -= (self.weight / self.fuel_consumption)
        else:
            raise exceptions.NotEnoughFuel()







