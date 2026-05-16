from jugador import Jugador
from reglas import valor_truco
from reglas import valor_envido
from truco import CantoTruco
from envido import CantoEnvido
from tanteador import Tanteador
from estado_partido import EstadoPartido
from partes_juego import JugarTruco
from carta import Carta

class JuegoFlor:
    def verificar_flor(self, j1, j2, canto_envido, tanteador):          
        ganador_flor = -1
        flor_j1 = j1.verificar_flor()
        flor_j2 = j2.verificar_flor()

        if flor_j1 and not flor_j2:
            ganador_flor = self.jugador_gano_flor(1, canto_envido, tanteador)
        elif flor_j2 and not flor_j1:
            ganador_flor = self.jugador_gano_flor(2, canto_envido, tanteador)
        elif flor_j1 and flor_j2:
            print("Ambos tienen flor, se comparan los tantos")
            comparacion_flor_j1 = j1.calcular_envido()
            comparacion_flor_j2 = j2.calcular_envido()
            if comparacion_flor_j1 > comparacion_flor_j2:
                ganador_flor = self.jugador_gano_flor(1, canto_envido, tanteador)
            elif comparacion_flor_j2 > comparacion_flor_j1:
                ganador_flor = self.jugador_gano_flor(2, canto_envido, tanteador)
            else:
                ganador_flor = self.jugador_gano_flor(1, canto_envido, tanteador)
        return ganador_flor

    def jugador_gano_flor(self, jugador, canto_envido, tanteador):
        self.mostrar_resultado_ganador_flor(jugador, canto_envido, tanteador)
        tanteador.sumar_puntos(jugador, canto_envido.puntos_flor())
        ganador_flor = jugador
        return ganador_flor

    def mostrar_resultado_ganador_flor(self, jugador, canto_envido, tanteador):
        if jugador == 0:
            print("Empate en la ronda, gana J1 por ser mano")
        else:
            print(f"Jugador {jugador} gana la flor")
        
        print(f"Puntos en juego: {canto_envido.puntos_flor()}")
        tanteador.sumar_puntos(1, canto_envido.puntos_flor())