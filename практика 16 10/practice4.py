"""Симулятор космического корабля

Корабль, члены экипажа и миссия. Миссия запускает события,
а каждое событие меняет корабль или экипаж
"""


class SpaceShip:
    """корабль с топливом, корпусом и скоростью"""

    def __init__(self, name, fuel, hull_integrity, speed=0):
        """название, топливо, целостность корпуса и скорость"""
        self.name = name
        self.fuel = fuel
        self.hull_integrity = hull_integrity
        self.speed = speed

    def accelerate(self, amount):
        """разгон, тратит топливо. если топлива мало, будет ошибка"""
        fuel_needed = amount
        if fuel_needed > self.fuel:
            raise ValueError("Недостаточно топлива для разгона")
        self.fuel -= fuel_needed
        self.speed += amount

    def __str__(self):
        """строка с состоянием корабля"""
        return (f"{self.name}: топливо {self.fuel}, корпус {self.hull_integrity}%, "
                f"скорость {self.speed}")


class CrewMember:
    """член экипажа"""

    def __init__(self, name, role, skills, health=100):
        """имя, роль, навыки и здоровье"""
        self.name = name
        self.role = role  # например: пилот, инженер
        self.skills = skills
        self.health = health

    def take_damage(self, amount):
        """уменьшает здоровье, но не ниже нуля"""
        self.health = max(0, self.health - amount)

    def is_alive(self):
        """True, если здоровье больше нуля"""
        return self.health > 0

    def __str__(self):
        """строка с данными члена экипажа"""
        return f"{self.name} ({self.role}), здоровье: {self.health}, навыки: {', '.join(self.skills)}"


class Mission:
    """миссия с целями, ресурсами и событиями"""

    def __init__(self, name, goals, resources):
        """название, цели и ресурсы, событий пока нет"""
        self.name = name
        self.goals = goals
        self.resources = resources  # например: {"топливо": 100}
        self.events = []

    def add_event(self, description, effect):
        """добавляет событие: текст и функцию, которая его применяет"""
        # effect — функция, которая меняет корабль или экипаж
        self.events.append((description, effect))

    def run(self, ship, crew):
        """запускает миссию, по очереди печатает события и применяет их"""
        print(f"Миссия «{self.name}» началась")
        for description, effect in self.events:
            print(f"Событие: {description}")
            effect(ship, crew)
        print("Миссия завершена")


if __name__ == "__main__":
    ship = SpaceShip("Орёл", fuel=100, hull_integrity=100)
    crew = [
        CrewMember("Анна", "пилот", ["навигация", "управление"]),
        CrewMember("Сергей", "инженер", ["ремонт", "электроника"]),
    ]

    ship.accelerate(30)

    mission = Mission(
        "Исследование пояса астероидов",
        goals=["Добраться до астероида", "Собрать образцы"],
        resources={"топливо": 100},
    )
    mission.add_event(
        "Встреча с астероидом, корпус повреждён",
        lambda s, c: setattr(s, "hull_integrity", s.hull_integrity - 20),
    )
    mission.add_event(
        "Авария в отсеке, пилот ранен",
        lambda s, c: c[0].take_damage(30),
    )

    mission.run(ship, crew)
    print(ship)
    for member in crew:
        print(member)
