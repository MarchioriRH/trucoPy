class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def _repr__(self):
        return f"{self.numero} de {self.palo}"