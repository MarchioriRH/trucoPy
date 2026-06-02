from canto_envido import CantoEnvido
from canto_flor import CantoFlor

class JuegoFlor:
    def __init__(self, j1, j2, canto_flor, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.canto_flor = canto_flor
        self.tanteador = tanteador

    def validar_flor(self, mano):
        palos = {}
        for carta in mano:
            if carta.palo not in palos:
                palos[carta.palo] = []
            palos[carta.palo].append(carta)

        for cartas in palos.values():
            if len(cartas) >= 3:
                return sum(carta.numero for carta in cartas[:3]) + 20
        return 0      

    def verificar_flor(self, jugador):
        if self.validar_flor(jugador.mano) > 0:
            print(f"Jugador {jugador.nombre} canta flor")
            return True
        return False
    
    def jugar_flor(self):
        flor_ganadora = []
        ganador_flor = -1
        if self.verificar_flor(self.j1) and self.verificar_flor(self.j2):
            print("Ambos tienen flor, se comparan los tantos")
            self.canto_flor.cantar(self.j1)
            self.canto_flor.cantar(self.j2)
            ganador_flor = self.definir_ganador()
        elif self.verificar_flor(self.j1):
            self.canto_flor.cantar(self.j1)
            ganador_flor = 1
        elif self.verificar_flor(self.j2):
            self.canto_flor.cantar(self.j2)
            ganador_flor = 2

        if ganador_flor == 1:
            self.jugador_gano_flor(1)
            flor_ganadora = self.j1.mano[:]
        elif ganador_flor == 2:
            self.jugador_gano_flor(2)
            flor_ganadora = self.j2.mano[:]  

        if ganador_flor == -1:
            print("Ningún jugador tiene flor")        

        return flor_ganadora, ganador_flor

    def definir_ganador(self):
        resultado_comparacion_flor = self.comparar_flor()
        
        if resultado_comparacion_flor == 1:
            ganador_flor = 1
        elif resultado_comparacion_flor == 2:
            ganador_flor = 2
        else:
            ganador_flor = 1

        return ganador_flor

    def comparar_flor(self):
        flor_j1 = self.calcular_flor(self.j1.mano)
        flor_j2 = self.calcular_flor(self.j2.mano)

        if flor_j1 > flor_j2:
            return 1
        elif flor_j2 > flor_j1:
            return 2        
        else:
            return 0

    def jugador_gano_flor(self, jugador):
        self.mostrar_resultado_ganador_flor(jugador)
        self.tanteador.sumar_puntos(jugador, self.canto_flor.puntos_flor())
        ganador_flor = jugador
        return ganador_flor

    def mostrar_resultado_ganador_flor(self, jugador):
        if jugador == 0:
            print("Empate en la ronda, gana J1 por ser mano")
        else:
            print(f"Jugador {jugador} gana la flor")
        
        print(f"Puntos en juego: {self.canto_flor.puntos_flor()}")
        self.tanteador.sumar_puntos(1, self.canto_flor.puntos_flor())