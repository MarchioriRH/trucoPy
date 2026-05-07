from estrategia_cartas import EstrategiaEnvido

class EstrategiaEnvido:
    def decidir_cantar(self, mano, estado):
        return False

    def aceptar(self, mano, nivel, estado):
        return True


class EnvidoAgresivo(EstrategiaEnvido):
    def decidir_cantar(self, mano):        
        return calcular_envido(mano) > 30


class EnvidoConservador(EstrategiaEnvido):
    def decidir_cantar(self, mano):
        return False

class EnvidoAdaptativo(EstrategiaEnvido):   
    def decidir_cantar(self, mano, estado):
        tanto = EstrategiaEnvido.calcular_envido(mano)

        ventaja = estado.puntos_j1 - estado.puntos_j2

        # Si voy perdiendo fuerte, arriesgo más
        if ventaja < -5:
            return tanto > 24

        # Si voy ganando cómodo, arriesgo menos
        if ventaja > 5:
            return tanto > 30

        # Partido parejo
        return tanto > 27

    def aceptar(self, mano, nivel, estado):
        tanto = calcular_envido(mano)
        riesgo = nivel

        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return True  # necesito remontar

        if ventaja > 8 and riesgo >= 3:
            return False  # no regalo puntos

        return tanto > 7