class Employee:
    raise_amount = 1.04 # Class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

print("Ëmployees:")
print(emp_1.email)
print(emp_1.fullname()) 
print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
#Employee.set_raise_amount(1.05)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)

class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Alice', 'Johnson', 70000, 'Python')
dev_2 = Developer('Bob', 'Brown', 80000, 'Java')


print("Developers:")
print(dev_1.email)

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

Manager_1 = Manager('Sara', 'Connor', 90000, [dev_1, dev_2])

print("Manager:")
print(Manager_1.email)  
Manager_1.print_emps()