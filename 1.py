import os
os.system('cls')

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  
        self.sound = "Woof"    

my_dog = Dog("Buddy")

print(f"Itning nomi: {my_dog.name}")
print(f"Itning tovushi: {my_dog.sound}")