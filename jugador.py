from reglas import valor_truco

class Jugador:
    def __init__(self, nombre, estrategia_cartas, estrategia_truco, estado):
        self.nombre = nombre
        self. mano = []
        self.estrategia_cartas = estrategia_cartas
        self.estrategia_truco = estrategia_truco
        self.estado = estado

    def recibir_cartas(self, cartas):
        self.mano = cartas

    def jugar_carta(self):
        carta = self.estrategia_cartas.elegir_carta(self.mano)
        self.mano.remove(carta)
        return(carta)

    def decidir_cantar_truco(self):
        return self.estrategia_truco.decidir_cantar(self.mano, self.estado)

    def aceptar_truco(self, nivel):
        return self.estrategia_truco.aceptar(self.mano, nivel, self.estado)
    
    def mostrar_mano(self):
        for i, carta in enumerate(self.mano):
            print(f"{i}: {carta}")

    