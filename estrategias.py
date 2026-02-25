from reglas import valor_truco
import random

class Estrategia:
    def elegir_carta(self, mano):
        pass


class EstrategiaMejor(Estrategia):
    def elegir_carta(self, mano):
        mejor = max(mano, key=valor_truco)
        return mejor


class EstrategiaPeor(Estrategia):
    def elegir_carta(self, mano):
        peor = min(mano, key=valor_truco)
        return peor


class EstrategiaRandom(Estrategia):
    def elegir_carta(self, mano):
        return random.choice(mano)

class EstrategiaAgresiva(Estrategia):
    def decidir_cantar_truco(self, mano):
        from reglas import valor_truco
        mejor = max(mano, key=valor_truco)
        return valor_truco(mejor) > 10  

def decidir_cantar_truco(self, mano):
    return False

def aceptar_truco(self, mano, nivel):
    return True