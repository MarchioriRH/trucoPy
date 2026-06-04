class EstrategiaFlor:
    def decidir_cantar(self, mano, estado):
        return False

    def aceptar(self, mano, nivel, estado):
        return True

class FlorAdaptativa(EstrategiaFlor):
    def decidir_cantar_contra_flor(self, jugador, estado):
        if 28 <= jugador.validar_flor(jugador.mano) <= 30:
            return 1

        if 31 <= jugador.validar_flor(jugador.mano) <= 38:
            return 2 

        return 0

    def decidir_aceptar_contraflor_al_resto(self, jugador, estado):
        if 28 <= jugador.validar_flor(jugador.mano) <= 30:
            return True

        if 31 <= jugador.validar_flor(jugador.mano) <= 38:
            return True 

        return False

    def decidir_aceptar_contraflor_al_partido(self, jugador, estado):
        if 28 <= jugador.validar_flor(jugador.mano) <= 30:
            return True

        if 31 <= jugador.validar_flor(jugador.mano) <= 38:
            return True 

        return False

    

    