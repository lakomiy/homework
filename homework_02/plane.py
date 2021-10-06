"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo
    def load_cargo(self, number):
        if number + Plane.cargo <= self.max_cargo:
            self.cargo += number
        else:
            raise CargoOverload()
    def remove_all_cargo(self):
        tmp_cargo = self.cargo
        self.cargo = 0
        return tmp_cargo

