from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 0
    fuel = 0
    fuel_consumption = 0
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError()
    def move(self, number):
        if self.fuel - (self.fuel_consumption * number) >= 0:
            self.fuel -= (number * self.fuel_consumption)
        else:
            raise exceptions.NotEnoughFuel()