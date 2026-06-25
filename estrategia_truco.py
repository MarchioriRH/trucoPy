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
        # print(f"Mano J2: {mano}")
        mejor = max(mano, key=valor_truco)
        riesgo = nivel

        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return True  # necesito remontar

        if ventaja > 8 and riesgo >= 3:
            return False  # no regalo puntos

        return "QUIERO" if valor_truco(mejor) > 6 else "NO QUIERO"

    def decidir_cantar_retruco(self, mano, estado):
        mejor = max(mano, key=valor_truco)
        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return valor_truco(mejor) > 7

        if ventaja > 5:
            return valor_truco(mejor) > 12

        return valor_truco(mejor) > 9

    def aceptar_retruco(self, mano, nivel, estado):
        mejor = max(mano, key=valor_truco)
        riesgo = nivel

        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return True  # necesito remontar

        if ventaja > 8 and riesgo >= 3:
            return False  # no regalo puntos

        return valor_truco(mejor) > 6

    def decidir_cantar_vale_cuatro(self, mano, estado):
        mejor = max(mano, key=valor_truco)
        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return valor_truco(mejor) > 7

        if ventaja > 5:
            return valor_truco(mejor) > 12

        return valor_truco(mejor) > 9

    def aceptar_vale_cuatro(self, mano, nivel, estado):
        mejor = max(mano, key=valor_truco)
        riesgo = nivel

        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return True  # necesito remontar

        if ventaja > 8 and riesgo >= 3:
            return False  # no regalo puntos

        return valor_truco(mejor) > 6

    def decidir_empardar_jugada(self, mano, carta_actual):

        especiales = {
            (1, "Espada"),
            (1, "Basto"),
            (7, "Espada"),
            (7, "Oro"),
        }
        
        mejor = max(mano, key=valor_truco)

        if valor_truco(mejor) > 11 and carta_actual not in especiales:
            for carta in enumerate(mano):
                if carta.numero == carta_actual.numero: # El número esta en la mano
                    return True
            return False