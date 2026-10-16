"""Сотрудники и зарплата

Три класса: Employee, а от него наследуются Manager и Developer
"""


class Employee:
    """обычный сотрудник, зарплата равна ставке"""

    def __init__(self, name, base_salary):
        """имя и базовая ставка"""
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        """возвращает зарплату"""
        return self.base_salary

    def __str__(self):
        """строка для print"""
        return f"{self.name}: {self.calculate_salary()} руб."


class Manager(Employee):
    """менеджер, зарплата зависит от команды"""

    def __init__(self, name, base_salary, team_size):
        """добавляем размер команды"""
        super().__init__(name, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        """ставка + 5000 за каждого подчинённого"""
        # Надбавка 5000 руб. за каждого подчинённого
        return self.base_salary + 5000 * self.team_size


class Developer(Employee):
    """разработчик, премия за выполненные задачи"""

    def __init__(self, name, base_salary, completed_tasks):
        """добавляем количество задач"""
        super().__init__(name, base_salary)
        self.completed_tasks = completed_tasks

    def calculate_salary(self):
        """ставка + 2000 за каждую задачу"""
        # Премия 2000 руб. за каждую выполненную задачу
        return self.base_salary + 2000 * self.completed_tasks


if __name__ == "__main__":
    employees = [
        Employee("Иван", 50000),
        Manager("Анна", 80000, team_size=4),
        Developer("Пётр", 70000, completed_tasks=6),
    ]
    for employee in employees:
        print(employee)
