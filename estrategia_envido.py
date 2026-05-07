from reglas import valor_envido

class EstrategiaEnvido:
    def decidir_cantar(self, mano, estado):
        return False

    def aceptar(self, mano, nivel, estado):
        return True


class EnvidoAgresivo(EstrategiaEnvido):
    def decidir_cantar(self, mano):        
        return valor_envido(mejor) > 30


class EnvidoConservador(EstrategiaEnvido):
    def decidir_cantar(self, mano):
        return False

class EnvidoAdaptativo(EstrategiaEnvido):
    def decidir_cantar(self, mano, estado):
        mejor = max(mano, key=valor_envido)

        ventaja = estado.puntos_j1 - estado.puntos_j2

        # Si voy perdiendo fuerte, arriesgo más
        if ventaja < -5:
            return valor_envido(mejor) > 24

        # Si voy ganando cómodo, arriesgo menos
        if ventaja > 5:
            return valor_envido(mejor) > 30

        # Partido parejo
        return valor_envido(mejor) > 27

    def aceptar(self, mano, nivel, estado):
        mejor = max(mano, key=valor_envido)
        riesgo = nivel

        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return True  # necesito remontar

        if ventaja > 8 and riesgo >= 3:
            return False  # no regalo puntos

        return valor_envido(mejor) > 6