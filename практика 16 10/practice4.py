class SpaceShip:
    def __init__(self, name, fuel, hull_integrity, speed=0):
        self.name = name
        self.fuel = fuel
        self.hull_integrity = hull_integrity
        self.speed = speed

    def accelerate(self, amount):
        fuel_needed = amount
        if fuel_needed > self.fuel:
            raise ValueError("Недостаточно топлива для разгона")
        self.fuel -= fuel_needed
        self.speed += amount

    def __str__(self):
        return (f"{self.name}: топливо {self.fuel}, корпус {self.hull_integrity}%, "
                f"скорость {self.speed}")


class CrewMember:
    def __init__(self, name, role, skills, health=100):
        self.name = name
        self.role = role  # например: пилот, инженер
        self.skills = skills
        self.health = health

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} ({self.role}), здоровье: {self.health}, навыки: {', '.join(self.skills)}"


class Mission:
    def __init__(self, name, goals, resources):
        self.name = name
        self.goals = goals
        self.resources = resources  # например: {"топливо": 100}
        self.events = []

    def add_event(self, description, effect):
        # effect — функция, которая меняет корабль или экипаж
        self.events.append((description, effect))

    def run(self, ship, crew):
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
