class Tanteador:
    LIMITE = 30

    def __init__(self):
        self.puntos = {
            1: 0,
            2: 0
        }

    def sumar_puntos(self, jugador, cantidad):
        self.puntos[jugador] += cantidad

    def puntos_jugador(self, jugador):
        return self.puntos[jugador]

    def esta_en_buenas(self, jugador):
        return self.puntos[jugador] >= 15

    def ganador(self):
        for jugador, puntos in self.puntos.items():
            if puntos >= self.LIMITE:
                return jugador
        return None

    def mostrar(self):
        print(f"Jugador 1: {self.puntos[1]} puntos")
        print(f"Jugador 2: {self.puntos[2]} puntos")