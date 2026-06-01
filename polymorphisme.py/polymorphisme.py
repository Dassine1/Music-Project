import numpy as np

class Cercle:
    def __init__(self, rayon:int):
        self.rayon = rayon
    def aire(self):
        return(self.rayon**2 * np.pi)
    
class Triangle:
     def __init__(self, base:int, hauteur:int):
        self.base = base
        self.hauteur = hauteur

     def aire(self):
        return (self.base * self.hauteur)/2

class Carre:
     def __init__(self, cote:int):
        self.cote = cote

     def aire(self):
        return(self.cote **2)


forme = [Cercle(25),Triangle(base:5,hauteur:7), Carre(6)]
for formes in forme:
    print(formes.aire())
    

