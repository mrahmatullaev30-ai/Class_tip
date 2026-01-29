import os
os.system('cls')

class Food:
    def __init__(self, name):
        self.name = name

class Fruit(Food):
    def __init__(self, name, vitamin):
        super().__init__(self, name)
        self.vitamin = vitamin

my_phone = Fruit("Mansur, D3")

print(my_phone.name)
print(my_phone.vitamin)