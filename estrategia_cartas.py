from reglas import valor_truco, valor_envido
import random

class EstrategiaCartas:
    def elegir_carta(self, mano):
        raise NotImplementedError


class CartaMejor(EstrategiaCartas):
    def elegir_carta(self, mano):
        return max(mano, key=valor_truco)


class CartaPeor(EstrategiaCartas):
    def elegir_carta(self, mano):
        return min(mano, key=valor_truco)


class CartaRandom(EstrategiaCartas):
    def elegir_carta(self, mano):
        return random.choice(mano)

class EstrategiaEnvido:
    def calcular_envido(mano):
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
