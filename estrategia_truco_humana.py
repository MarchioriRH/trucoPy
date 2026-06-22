from reglas import valor_truco

class EstrategiaHumanaTruco:
    def decidir_cantar(self, mano, estado):
        return False

    def aceptar(self, mano, nivel, estado):
        return True

class TrucoHumanoAdaptativo(EstrategiaHumanaTruco):
    def decidir_cantar(self, mano, estado):
        respuesta = input(
                "¿Queres cantar truco (S / N): "
            ).upper()

        return respuesta == "S"

    def decidir_aceptar(self, mano, nivel, estado):
        respuesta = input(
                "¿Queres aceptar el truco (S / N): "
            ).upper()

        return respuesta == "S"

    def decidir_cantar_retruco(self, mano, estado):
        respuesta = input(
                "¿Queres cantar re truco (S / N): "
            ).upper()

        return respuesta == "S"

    def decidir_aceptar_retruco(self, mano, nivel, estado):
        respuesta = input(
                "¿Queres aceptar truco (S / N): "
            ).upper()

        return respuesta == "S"

    def decidir_cantar_vale_cuatro(self, mano, estado):
        respuesta = input(
                "¿Queres cantar vale cuatro (S / N): "
            ).upper()

        return respuesta == "S"

    def decidir_aceptar_vale_cuatro(self, mano, nivel, estado):
        respuesta = input(
                "¿Queres aceptar el vale cuatro (S / N): "
            ).upper()

        return respuesta == "S"

    