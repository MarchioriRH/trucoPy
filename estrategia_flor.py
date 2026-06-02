class EstrategiaFlor:
    def decidir_cantar(self, mano, estado):
        return False

    def aceptar(self, mano, nivel, estado):
        return True

class FlorAdaptativa(EstrategiaFlor):
    def __init__(self):
        pass

    