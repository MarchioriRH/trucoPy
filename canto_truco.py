from jugador import Jugador
from reglas import valor_truco
from tanteador import Tanteador
from estado_partido import EstadoPartido

class CantoTruco:
    def __init__(self):
        self.nivel_truco = 1
        self.ultimo_cantor = None
        self.activo = False
        self.terminado = False
        self.ganador = None

    def puede_cantar(self):
        return self.nivel_truco < 4 and not self.terminado

    def cantar(self, jugador):
        if not self.puede_cantar():
            return False

        self.nivel_truco += 1
        self.ultimo_cantor = jugador
        self.activo = True
        return True

    def cantar_retruco(self, jugador):
        if self.nivel_truco != 2 or self.terminado:
            return False

        self.nivel_truco += 1
        self.ultimo_cantor = jugador
        self.activo = True
        return True

    def aceptar(self):
        self.activo = False
    
    def cantar_vale_cuatro(self, jugador):
        if self.nivel_truco != 3 or self.terminado:
            return False

        self.nivel_truco += 1
        self.ultimo_cantor = jugador
        self.activo = True
        return True

    def rechazar(self, jugador_que_rechaza):
        self.terminado = True
        self.ganador = self.ultimo_cantor

    def puntos_en_juego(self):
        return self.nivel_truco

    def puntos_por_rechazo(self):
        return self.nivel_truco - 1

