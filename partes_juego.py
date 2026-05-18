from jugador import Jugador
from reglas import valor_truco
from reglas import valor_envido
from truco import CantoTruco
from envido import CantoEnvido
from tanteador import Tanteador
from estado_partido import EstadoPartido


class JugarTruco:

    def __init__(self, j1, j2, canto_truco, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.tanteador = tanteador
        self.canto_truco = canto_truco
    
    def jugar_truco(self):
        no_quiero_truco = False
        se_canto_truco = False
        
        if self.j1.decidir_cantar_truco():
            self.jugador_canta_truco(1)
            se_canto_truco = True

            if not self.j2.aceptar_truco(self.j2.mano):
                no_quiero_truco = True
                self.jugador_no_quiso_truco(2)                
            else:
                self.jugador_quiso_truco(1)

        elif self.j2.decidir_cantar_truco():
            self.jugador_canta_truco(2)
            se_canto_truco = True

            if not self.j1.aceptar_truco(self.j1.mano):
                no_quiero_truco = True
                self.jugador_no_quiso_truco(1)
            
            else:
                self.jugador_quiso_truco(2)

        if not no_quiero_truco:
            self.jugar_carta_mano()
        else:
            print("No se quiso el truco, se procede a mostrar el self.tanteador")

    def jugador_canta_truco(self, jugador):
        self.canto_truco.cantar(self.j2)
        print(f"Jugador {jugador} canta Truco")

    def jugador_quiso_truco(self, jugador):
        self.canto_truco.aceptar()
        print(f"Jugador {jugador} quiso")

    def jugador_no_quiso_truco(self, jugador):
        self.canto_truco.rechazar(jugador)
        print(f"Jugador {jugador} no quiso")
        print(f"Jugador {3 - jugador} gana", self.canto_truco.puntos_por_rechazo())
        self.tanteador.sumar_puntos(3 - jugador, self.canto_truco.puntos_por_rechazo())

    def comparar_cartas(self, carta_j1, carta_j2):
        if valor_truco(carta_j1) > valor_truco(carta_j2):
            return 1
        elif valor_truco(carta_j2) > valor_truco(carta_j1):
            return 2
        else:
            return 0

    def determinar_ganador_mano(self, jugador_actual, otro_jugador, id_jugador_actual, id_otro_jugador, 
                               carta_en_juego, num_ronda=1):
        """
        Método recursivo que determina el ganador de una mano.
        El flujo es: quien no mata pierde, quien mata juega otra.
        
        Args:
            jugador_actual: Jugador que debe responder
            otro_jugador: Jugador que jugó la carta anterior
            id_jugador_actual: ID del jugador actual (1 o 2)
            id_otro_jugador: ID del otro jugador (1 o 2)
            carta_en_juego: Carta que debe responder
            num_ronda: Número de ronda (1-3)
        
        Returns:
            ID del jugador que ganó la mano
        """
        if num_ronda > 3:
            return id_otro_jugador
        
        print(f"\nRonda {num_ronda}: Jugador {id_jugador_actual} debe responder a {carta_en_juego}")
        carta_respuesta = jugador_actual.analizar_jugada(carta_en_juego)
        print(f"Jugador {id_jugador_actual} juega: {carta_respuesta}")
        
        resultado = self.comparar_cartas(carta_en_juego, carta_respuesta)
        
        if resultado == 1:
            print(f"Jugador {id_jugador_actual} no mata")
            return id_otro_jugador
        elif resultado == 2:
            print(f"Jugador {id_jugador_actual} mata con {carta_respuesta}")
            if num_ronda < 3:
                nueva_carta = otro_jugador.jugar_carta()
                print(f"Jugador {id_otro_jugador} juega: {nueva_carta}")
            return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                               id_jugador_actual, carta_respuesta, num_ronda + 1)
        else:
            print(f"Parda en ronda {num_ronda}")
            if num_ronda < 3:
                nueva_carta = jugador_actual.jugar_carta()
                print(f"Jugador {id_jugador_actual} juega: {nueva_carta}")
            return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                               id_jugador_actual, carta_respuesta, num_ronda + 1)

    def adjudicar_ganador_mano(self, id_ganador):
        """Suma los puntos al ganador de la mano"""
        puntos = self.canto_truco.puntos_en_juego()
        print(f"\n>>> Gana Jugador {id_ganador} la mano")
        print(f">>> Puntos en juego: {puntos}\n")
        self.tanteador.sumar_puntos(id_ganador, puntos)

    def jugar_carta_mano(self):
        carta1_j1 = self.j1.jugar_carta()
        print(f"Jugador 1 juega carta 1: {carta1_j1}")
        
        carta1_j2 = self.j2.analizar_jugada(carta1_j1)
        resultado_inicial = self.comparar_cartas(carta1_j1, carta1_j2)
        print(f"Jugador 2 juega: {carta1_j2}")
        print(f"Resultado: {resultado_inicial} (1: J1 gana, 2: J2 gana, 0: Parda)\n")
        
        if resultado_inicial == 2:
            print(f"Jugador 2 mata")
            id_ganador = self.determinar_ganador_mano(self.j1, self.j2, 1, 2, carta1_j2, 2)
        elif resultado_inicial == 1:
            print(f"Jugador 2 no mata")
            nueva_carta = self.j1.jugar_carta()
            print(f"Jugador 1 juega: {nueva_carta}")
            id_ganador = self.determinar_ganador_mano(self.j2, self.j1, 2, 1, nueva_carta, 2)
        else:
            print("Parda en ronda 1")
            nueva_carta = self.j2.jugar_carta()
            print(f"Jugador 2 juega: {nueva_carta}")
            id_ganador = self.determinar_ganador_mano(self.j1, self.j2, 1, 2, nueva_carta, 2)
        
        self.adjudicar_ganador_mano(id_ganador)