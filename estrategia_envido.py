

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
        # calcular_envido = CalcularEnvido()
        tanto = self.calcular_envido(mano)

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
        # calcular_envido = CalcularEnvido()
        tanto = self.calcular_envido(mano)
        riesgo = nivel

        ventaja = estado.puntos_j1 - estado.puntos_j2

        if ventaja < -5:
            return True  # necesito remontar

        if ventaja > 8 and riesgo >= 3:
            return False  # no regalo puntos

        return tanto > 7

    def verificar_flor(self, mano):
        palos = {}
        for carta in mano:
            if carta.palo not in palos:
                palos[carta.palo] = []
            palos[carta.palo].append(carta)

        for cartas in palos.values():
            if len(cartas) >= 3:
                return True      
        return False
   
    def calcular_envido(self, mano):
        # 1. Normalizar valores: las figuras valen 0 para el envido
        def valor_envido(carta):
            return carta.numero if carta.numero < 10 else 0

        # 2. Agrupar cartas por palo
        palos = {}
        for carta in mano:
            if carta.palo not in palos:
                palos[carta.palo] = []
            palos[carta.palo].append(valor_envido(carta))

        max_tanto = 0

        # 3. Calcular el tanto por cada palo
        for valores in palos.values():
            if len(valores) >= 2:
                # Hay dos o tres cartas del mismo palo
                valores.sort(reverse=True)
                # Se suman las dos más altas + 20
                tanto = 20 + valores[0] + valores[1]
            else:
                # Solo una carta de este palo (o ninguna coincidencia)
                tanto = valores[0]

            if tanto > max_tanto:
                max_tanto = tanto

        return max_tanto
