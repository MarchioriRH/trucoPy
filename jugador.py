from reglas import valor_truco
from flor import JuegoFlor

class Jugador:
    def __init__(self, nombre = None, estrategia_cartas = None, estrategia_truco = None, estrategia_envido = None, estrategia_flor = None, estado = None):
        self.nombre = nombre
        self. mano = []
        self.estrategia_cartas = estrategia_cartas
        self.estrategia_truco = estrategia_truco
        self.estrategia_envido = estrategia_envido
        self.estrategia_flor = estrategia_flor
        self.juego_flor = JuegoFlor
        self.estado = estado

    def recibir_cartas(self, cartas):
        self.mano = cartas

    def jugar_carta(self):
        carta = self.estrategia_cartas.elegir_carta(self.mano)
        self.mano.remove(carta)
        return(carta)

    def validar_flor(self, mano):
        valor_flor = self.juego_flor.validar_flor(self, mano)
        return(valor_flor)

    # def calcular_flor(self):
    #     tanto = self.estrategia_flor.calcular_flor(self.mano)
    #     return(tanto)

    def decidir_cantar_contraflor(self):
        return self.estrategia_flor.decidir_cantar_contraflor(self, self.estado)

    def calcular_envido(self):
        tanto = self.estrategia_envido.calcular_envido(self.mano)
        return(tanto)

    def decidir_cantar_envido(self):
        return self.estrategia_envido.decidir_cantar(self.mano, self.estado)

    def decidir_re_envidar(self):
        return self.estrategia_envido.decidir_re_envidar(self.mano, self.estado)
    
    def decidir_aceptar_re_envido(self):
        return self.estrategia_envido.decidir_aceptar_re_envido(self.mano, self.estado)

    def decidir_cantar_real_envido(self):
        return self.estrategia_envido.decidir_cantar_real_envido(self.mano, self.estado)
    
    def decidir_aceptar_real_envido(self):
        return self.estrategia_envido.decidir_aceptar_real_envido(self.mano, self.estado)

    def decidir_cantar_falta_envido(self):
        return self.estrategia_envido.decidir_cantar_falta_envido(self.mano, self.estado)

    def decidir_aceptar_falta_envido(self):
        return self.estrategia_envido.decidir_aceptar_falta_envido(self.mano, self.estado)

    def decidir_aceptar_envido(self):
        return self.estrategia_envido.decidir_aceptar_envido(self.mano, self.estado)

    def decidir_cantar_truco(self):
        return self.estrategia_truco.decidir_cantar(self.mano, self.estado)

    def aceptar_truco(self, nivel):
        return self.estrategia_truco.aceptar(self.mano, nivel, self.estado)

    def decidir_cantar_retruco(self):
        return self.estrategia_truco.decidir_cantar_retruco(self.mano, self.estado)

    def aceptar_retruco(self, nivel):
        return self.estrategia_truco.aceptar_retruco(self.mano, nivel, self.estado)

    def decidir_cantar_vale_cuatro(self):
        return self.estrategia_truco.decidir_cantar_vale_cuatro(self.mano, self.estado)

    def aceptar_vale_cuatro(self, nivel):
        return self.estrategia_truco.aceptar_vale_cuatro(self.mano, nivel, self.estado)
    
    def decidir_empardar_jugada(self, carta_actual):
        return self.estrategia_truco.decidir_empardar_jugada(self.mano, carta_actual)
    
    def mostrar_mano(self):
        for i, carta in enumerate(self.mano):
            print(f"{i}: {carta}")

    def cambiar_estrategia_cartas(self, estrategia_cartas):
        self.estrategia_cartas = estrategia_cartas

    def cambiar_estrategia_truco(self, estrategia_truco):
        self.estrategia_truco = estrategia_truco

    def analizar_jugada(self, carta_jugada):
        mano_ordenada = sorted(self.mano, key=valor_truco)
        # print(f"Mano ordenada principio: {mano_ordenada}")
        for carta in mano_ordenada:
            if valor_truco(carta) > valor_truco(carta_jugada):
                carta_elegida = carta
                self.mano.remove(carta)
                return carta_elegida
        
        carta_elegida = mano_ordenada[0]
        self.mano.remove(carta_elegida)        
        # print(f"Mano ordenada final: {mano_ordenada}")
        return carta_elegida  # Si no tiene carta más alta, juega la primera carta

class humano:
     def __init__(self, nombre):
        self.nombre = nombre
        self. mano = []
        self.estado = estado   