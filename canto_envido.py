class CantoEnvido:
    def __init__(self):
        self.nivel = 1
        self.ultimo_cantor = None
        self.activo = False
        self.terminado = False
        self.ganador = None

    def puede_cantar(self):
        return self.nivel < 4 and not self.terminado

    def cantar(self, jugador):
        if not self.puede_cantar():
            return False
        print(f"Nivel envido: {self.nivel}, puntos en juego: {self.puntos_en_juego()}")
        self.nivel += 1
        self.ultimo_cantor = jugador
        self.activo = True
        return True

    def aceptar(self):
        self.activo = False

    def rechazar(self, jugador_que_rechaza):
        self.terminado = True
        self.ganador = self.ultimo_cantor

    def puntos_en_juego(self):
        return self.nivel

    def puntos_por_rechazo(self):
        return self.nivel - 1