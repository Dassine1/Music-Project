class Animal:
    def __init__(self, nom:str,age:int):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je suis {self.nom} et j'ai {self.age} ans")

class Chien(Animal):
    def __init__(self, nom, age,race:str):
        super().__init__(nom, age)
        self.race = race


    def aboyer():
        print(f"Wouf wouf")

a = Chien("blablabla",12,"berger allemand")
print(a)