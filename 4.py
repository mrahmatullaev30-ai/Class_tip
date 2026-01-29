class Building:
    def __init__(self, address):
        self.address = address

class School(Building):
    def __init__(self, address, student_count):
        super().__init__(address)  
        self.student_count = student_count

my_school = School("Toshkent, Amir Temur ko'chasi 10", 500)

print("Manzil:", my_school.address)
print("O'quvchilar soni:", my_school.student_count)