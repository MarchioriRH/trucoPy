import random
from carta import Carta

class Mazo:
    palos =["Espada", "Basto", "Oro", "Copa"]
    numeros = [1,2,3,4,5,6,7,10,11,12]

    def __init__(self):
        self.cartas = [Carta(n, p) for p in self.palos for n in self.numeros]

    def mezclar(self):
        random.shuffle(self.cartas)
    
    def repartir(self, cantidad):
        return[self.cartas.pop() for _ in range(cantidad)]