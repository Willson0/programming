"""Транспорт и полиморфизм

У всех классов есть метод describe, но каждый возвращает свою строку
"""


class Vehicle:
    """общий класс транспорта"""

    def __init__(self, name, wheels):
        """название и количество колёс"""
        self.name = name
        self.wheels = wheels

    def describe(self):
        """общее описание"""
        return f"Транспортное средство {self.name} с {self.wheels} колёсами"


class Car(Vehicle):
    """легковая машина, 4 колеса"""

    def __init__(self, name, seats):
        """колёса всегда 4, запоминаем места"""
        super().__init__(name, wheels=4)
        self.seats = seats

    def describe(self):
        """описание машины"""
        return f"Легковой автомобиль {self.name}, мест: {self.seats}"


class Truck(Vehicle):
    """грузовик, 6 колёс"""

    def __init__(self, name, load_capacity):
        """колёса всегда 6, запоминаем грузоподъёмность"""
        super().__init__(name, wheels=6)
        self.load_capacity = load_capacity

    def describe(self):
        """описание грузовика"""
        return f"Грузовик {self.name}, грузоподъёмность: {self.load_capacity} т"


class Motorcycle(Vehicle):
    """мотоцикл, 2 колеса"""

    def __init__(self, name, engine_cc):
        """колёса всегда 2, запоминаем объём двигателя"""
        super().__init__(name, wheels=2)
        self.engine_cc = engine_cc

    def describe(self):
        """описание мотоцикла"""
        return f"Мотоцикл {self.name}, объём двигателя: {self.engine_cc} см³"


if __name__ == "__main__":
    vehicles = [
        Car("Lada Vesta", seats=5),
        Truck("KAMAZ", load_capacity=20),
        Motorcycle("Ural", engine_cc=750),
    ]
    for vehicle in vehicles:
        print(vehicle.describe())
