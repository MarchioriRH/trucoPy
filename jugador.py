from reglas import valor_truco

class Jugador:
    def __init__(self, nombre, estrategia):
        self.nombre = nombre
        self. mano = []
        self.estrategia = estrategia

    def recibir_cartas(self, cartas):
        self.mano = cartas

    def jugar_carta(self):
        carta = self.estrategia.elegir_carta(self.mano)
        self.mano.remove(carta)
        return(carta)
    
    def mostrar_mano(self):
        for i, carta in enumerate(self.mano):
            print(f"{i}: {carta}")

    