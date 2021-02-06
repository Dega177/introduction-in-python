class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        return sum(self._income.values())


employee_1 = Position('John', 'Dow', 'Sales manager', 10000, 3400)
employee_2 = Position('Frank', 'Shelton ', 'Clerk', 8000, 500)

employee_1.get_full_name()
employee_2.get_full_name()

print(employee_1.get_total_income())
print(employee_2.get_total_income())

print(employee_1.name)
print(employee_1.position)

print(employee_2.name)
print(employee_2.position)
