import os
os.system("cls")

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)  
        self.type = type  

bike1 = Bike("Trek", 25, "mountain")
bike2 = Bike("Giant", 30, "road")
bike3 = Bike("Specialized", 28, "hybrid")

bikes = [bike1, bike2, bike3]

for bike in bikes:
    print(f"Brand: {bike.brand}, Speed: {bike.speed}, Type: {bike.type}")