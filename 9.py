import os
os.system('cls')

class Employe:
    def __init__(self, name, position):
        self.name = name 
        self.position = position
class Stud(Employe):
    def __init__(self, name, position, team_size):
        super().__init__(name, position)
        self.team_size = team_size
    
c1 = Stud("Sardor", "Manager", "one_pc")
print(c1.name)
print(c1.position)
print(c1.team_size)