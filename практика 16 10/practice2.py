class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def describe(self):
        return f"Транспортное средство {self.name} с {self.wheels} колёсами"


class Car(Vehicle):
    def __init__(self, name, seats):
        super().__init__(name, wheels=4)
        self.seats = seats

    def describe(self):
        return f"Легковой автомобиль {self.name}, мест: {self.seats}"


class Truck(Vehicle):
    def __init__(self, name, load_capacity):
        super().__init__(name, wheels=6)
        self.load_capacity = load_capacity

    def describe(self):
        return f"Грузовик {self.name}, грузоподъёмность: {self.load_capacity} т"


class Motorcycle(Vehicle):
    def __init__(self, name, engine_cc):
        super().__init__(name, wheels=2)
        self.engine_cc = engine_cc

    def describe(self):
        return f"Мотоцикл {self.name}, объём двигателя: {self.engine_cc} см³"


if __name__ == "__main__":
    vehicles = [
        Car("Lada Vesta", seats=5),
        Truck("KAMAZ", load_capacity=20),
        Motorcycle("Ural", engine_cc=750),
    ]
    for vehicle in vehicles:
        print(vehicle.describe())
