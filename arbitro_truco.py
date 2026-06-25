from enum import Enum, auto

class EstadoTruco(Enum):
    VALE_1 = auto()
    TRUCO_PENDIENTE = auto()
    TRUCO = auto()
    RETRUCO_PENDIENTE = auto()
    RETRUCO = auto()
    VALE_4_PENDIENTE = auto()
    VALE_4 = auto()
    FINALIZADO = auto()

class ArbitroTruco:
    def __init__(self, j1, j2):
        self.estado_actual = EstadoTruco.VALE_1
        self.puntos_en_juego = 1
        # Quién tiene el derecho a revirar (cantar el siguiente nivel)
        self.propietario_del_quiero = None 
        self.j1 = j1
        self.j2 = j2

    def cantar_truco(self, jugador):
        if self.estado_actual == EstadoTruco.VALE_1:
            self.estado_actual = EstadoTruco.TRUCO_PENDIENTE
            print(f"{jugador.nombre} cantó Truco. Esperando respuesta...")
            return True
        return False

    def responder_quiero(self, jugador_que_responde):
        if self.estado_actual == EstadoTruco.TRUCO_PENDIENTE:
            print("Entra truco pendiente")
            self.estado_actual = EstadoTruco.TRUCO
            self.puntos_en_juego = 2
            print(f"DEBUG: el estado actual es {self.estado_actual}")
        elif self.estado_actual == EstadoTruco.RETRUCO_PENDIENTE:
            self.estado_actual = EstadoTruco.RETRUCO
            self.puntos_en_juego = 3
        elif self.estado_actual == EstadoTruco.VALE_4_PENDIENTE:
            self.estado_actual = EstadoTruco.VALE_4
            self.puntos_en_juego = 4
        else:
            print(f"DEBUG: Error de estado. El estado actual es '{self.estado_actual}' (Tipo: {type(self.estado_actual)})")
            return False
        
        # El que aceptó, ahora le da el "quiero" al rival para revirar
        self.propietario_del_quiero = jugador_que_responde
        print(f"¡Quiero! La mano ahora vale {self.puntos_en_juego} puntos.")
        return True

    def responder_no_quiero(self, jugador_que_responde):
        # El rival gana los puntos del estado consolidado anterior
        valores_anteriores = {
            EstadoTruco.TRUCO_PENDIENTE: 1,
            EstadoTruco.RETRUCO_PENDIENTE: 2,
            EstadoTruco.VALE_4_PENDIENTE: 3
        }
        
        if self.estado_actual in valores_anteriores:
            self.puntos_en_juego = valores_anteriores[self.estado_actual]
            self.estado_actual = EstadoTruco.FINALIZADO
            print(f"No quiero. Fin de la ronda. Puntos otorgados: {self.puntos_en_juego}")
            return True
        return False

    def cantar_retruco(self, jugador):
        if self.estado_actual == EstadoTruco.TRUCO and jugador == self.propietario_del_quiero:
            self.estado_actual = EstadoTruco.RETRUCO_PENDIENTE
            print(f"{jugador.nombre} cantó Retruco. Esperando respuesta...")
            return True
        return False

    def cantar_vale_cuatro(self, jugador):
        if self.estado_actual == EstadoTruco.RETRUCO and jugador == self.propietario_del_quiero:
            self.estado_actual = EstadoTruco.VALE_CUATRO_PENDIENTE
            print(f"{jugador.nombre} cantó Vale Cuatro. Esperando respuesta...")
            return True
        return False
    
