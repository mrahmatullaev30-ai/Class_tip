
class Worker:
    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.full_name}, Salary: {self.salary}")

class Programmer(Worker):
    def __init__(self, full_name, salary, language):
        super().__init__(full_name, salary)  
        self.language = language

    def show_info(self):
    
        super().show_info()
        print(f"Programming Language: {self.language}")

prog1 = Programmer("Ali Karimov", 1500, "Python")
prog2 = Programmer("Laylo Xasanova", 1800, "JavaScript")
prog3 = Programmer("Jasur Qodirov", 2000, "Java")

prog1.show_info()
prog2.show_info()
prog3.show_info()
