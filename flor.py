from jugador import Jugador
from reglas import valor_truco
from truco import CantoTruco
from envido import CantoEnvido
from tanteador import Tanteador
from estado_partido import EstadoPartido
# from partes_juego import JugarTruco
from carta import Carta

class JuegoFlor:
    def __init__(self, j1, j2, canto_envido, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.canto_envido = canto_envido
        self.tanteador = tanteador

    def verificar_flor(self):          
        ganador_flor = -1
        flor_j1 = self.j1.verificar_flor()
        flor_j2 = self.j2.verificar_flor()

        if flor_j1 and not flor_j2:
            ganador_flor = self.jugador_gano_flor(1)
        elif flor_j2 and not flor_j1:
            ganador_flor = self.jugador_gano_flor(2)
        elif flor_j1 and flor_j2:
            print("Ambos tienen flor, se comparan los tantos")
            comparacion_flor_j1 = self.j1.calcular_envido()
            comparacion_flor_j2 = self.j2.calcular_envido()
            if comparacion_flor_j1 > comparacion_flor_j2:
                ganador_flor = self.jugador_gano_flor(1)
            elif comparacion_flor_j2 > comparacion_flor_j1:
                ganador_flor = self.jugador_gano_flor(2)
            else:
                ganador_flor = self.jugador_gano_flor(1)
        return ganador_flor

    def jugador_gano_flor(self, jugador):
        self.mostrar_resultado_ganador_flor(jugador)
        self.tanteador.sumar_puntos(jugador, self.canto_envido.puntos_flor())
        ganador_flor = jugador
        return ganador_flor

    def mostrar_resultado_ganador_flor(self, jugador):
        if jugador == 0:
            print("Empate en la ronda, gana J1 por ser mano")
        else:
            print(f"Jugador {jugador} gana la flor")
        
        print(f"Puntos en juego: {self.canto_envido.puntos_flor()}")
        self.tanteador.sumar_puntos(1, self.canto_envido.puntos_flor())