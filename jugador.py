from reglas import valor_truco, valor_envido

class Jugador:
    def __init__(self, nombre, estrategia_cartas, estrategia_truco, estrategia_envido, estado):
        self.nombre = nombre
        self. mano = []
        self.estrategia_cartas = estrategia_cartas
        self.estrategia_truco = estrategia_truco
        self.estrategia_envido = estrategia_envido
        self.estado = estado

    def recibir_cartas(self, cartas):
        self.mano = cartas

    def jugar_carta(self):
        carta = self.estrategia_cartas.elegir_carta(self.mano)
        self.mano.remove(carta)
        return(carta)

    def verificar_flor(self):
        flor = self.estrategia_envido.verificar_flor(self.mano)
        return(flor)

    def calcular_envido(self):
        tanto = self.estrategia_envido.calcular_envido(self.mano)
        return(tanto)

    def decidir_cantar_envido(self):
        return self.estrategia_envido.decidir_cantar(self.mano, self.estado)

    def aceptar_envido(self, nivel):
        return self.estrategia_envido.aceptar(self.mano, nivel, self.estado)

    def decidir_cantar_truco(self):
        return self.estrategia_truco.decidir_cantar(self.mano, self.estado)

    def aceptar_truco(self, nivel):
        return self.estrategia_truco.aceptar(self.mano, nivel, self.estado)
    
    def mostrar_mano(self):
        for i, carta in enumerate(self.mano):
            print(f"{i}: {carta}")

    def cambiar_estrategia_cartas(self, estrategia_cartas):
        self.estrategia_cartas = estrategia_cartas

    def cambiar_estrategia_truco(self, estrategia_truco):
        self.estrategia_truco = estrategia_truco

    def analizar_jugada(self, carta_jugada):
        mano_ordenada = sorted(self.mano, key=valor_truco)
        for carta in mano_ordenada:
            if valor_truco(carta) > valor_truco(carta_jugada):
                carta_elegida = carta
                self.mano.remove(carta)
                return carta_elegida
        
        print(f"Mano ordenada: {mano_ordenada}")
        carta_elegida = mano_ordenada[0]
        self.mano.remove(carta_elegida)        
        return carta_elegida  # Si no tiene carta más alta, juega la primera carta

    