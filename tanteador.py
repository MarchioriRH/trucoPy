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

    def calcular_puntos_restantes(self, jugador):
        return max(0, self.LIMITE - self.puntos[jugador])

    def calcular_puntos_restantes_al_partido(self):
        ganando = max(self.puntos[1], self.puntos[2])
        return max(0, self.LIMITE - ganando)

    def mostrar(self, j1, j2):
        print(f">>> {j1.nombre}: {self.puntos[1]} puntos")
        print(f">>> {j2.nombre}: {self.puntos[2]} puntos")