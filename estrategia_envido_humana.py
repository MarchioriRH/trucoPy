from canto_envido import CantoEnvido

class EstrategiaEnvidoHumana:
    def decidir_cantar(self, mano, estado):
        return False

    def aceptar(self, mano, nivel, estado):
        return True

class EnvidoAdaptativoHumano(EstrategiaEnvidoHumana): 

    def __init__(self):
        self.canto_envido = CantoEnvido()
        self.nivel = self.canto_envido.nivel

    def decidir_cantar(self, mano, estado):
        respuesta = input(
            "¿Querés cantar envido? (S/N): "
        ).upper()

        return respuesta == "S"

    def decidir_aceptar_envido(self, mano, estado):
        respuesta = input(
            "¿Querés aceptar el envido? (S/N): "
        ).upper()

        return respuesta == "S"
   
    def decidir_re_envidar(self, mano, estado):
        respuesta = input(
            "¿Querés re envidar? (S/N): "
        ).upper()

        return respuesta == "S"

    def decidir_aceptar_re_envido(self, mano, estado):
        respuesta = input(
            "¿Querés aceptar el re envido? (S/N): "
        ).upper()

        return respuesta == "S"

    def decidir_cantar_real_envido(self, mano, estado):
        respuesta = input(
            "¿Querés cantar real envido? (S/N): "
        ).upper()
    
        return respuesta == "S"

    def decidir_aceptar_real_envido(self, mano, estado):
        respuesta = input(
            "¿Querés aceptar el real envido? (S/N): "
        ).upper()

        return respuesta == "S"

    def decidir_cantar_falta_envido(self, mano, estado):
        respuesta = input(
            "¿Querés cantar falta envido? (S/N): "
        ).upper()

        return respuesta == "S"

    def decidir_aceptar_falta_envido(self, mano, estado):
        respuesta = input(
            "¿Querés aceptar la falta envido? (S/N): "
        ).upper()

        return respuesta == "S"

    def calcular_envido(self, mano):
        respuesta = input(
            "¿Cuantos tantos tenes?: "
        )

        return int(respuesta)
