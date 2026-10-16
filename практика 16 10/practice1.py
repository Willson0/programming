class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f"{self.name}: {self.calculate_salary()} руб."


class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        # Надбавка 5000 руб. за каждого подчинённого
        return self.base_salary + 5000 * self.team_size


class Developer(Employee):
    def __init__(self, name, base_salary, completed_tasks):
        super().__init__(name, base_salary)
        self.completed_tasks = completed_tasks

    def calculate_salary(self):
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
