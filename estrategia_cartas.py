from reglas import valor_truco
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



