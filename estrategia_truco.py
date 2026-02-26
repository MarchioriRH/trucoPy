from reglas import valor_truco

class EstrategiaTruco:
    def decidir_cantar(self, mano, estado):
        return False

    def aceptar(self, mano, nivel, estado):
        return True


class TrucoAgresivo(EstrategiaTruco):
    def decidir_cantar(self, mano):
        mejor = max(mano, key=valor_truco)
        return valor_truco(mejor) > 10


class TrucoConservador(EstrategiaTruco):
    def decidir_cantar(self, mano):
        return False

class TrucoAdaptativo(EstrategiaTruco):
    def decidir_cantar(self, mano, estado):
        mejor = max(mano, key=valor_truco)

        ventaja = estado.puntos_j1 - estado.puntos_j2

        # Si voy perdiendo fuerte, arriesgo más
        if ventaja < -5:
            return valor_truco(mejor) > 7

        # Si voy ganando cómodo, arriesgo menos
        if ventaja > 5:
            return valor_truco(mejor) > 12

        # Partido parejo
        return valor_truco(mejor) > 9

    def aceptar(self, mano, nivel, estado):
        mejor = max(mano, key=valor_truco)
        riesgo = nivel

        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return True  # necesito remontar

        if ventaja > 8 and riesgo >= 3:
            return False  # no regalo puntos

        return valor_truco(mejor) > 6