import os
os.system('cls')

class Device:
    def __init__(self, brand):
        self.brand = brand


class Phone(Device):
    def __init__(self, brand, ram):
        super().__init__(brand)  
        self.ram = ram

my_phone = Phone("Samsung", "8GB")

print("Brand:", my_phone.brand)
print("RAM:", my_phone.ram)