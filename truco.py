from jugador import Jugador
from reglas import valor_truco
from tanteador import Tanteador
from estado_partido import EstadoPartido

class CantoTruco:
    def __init__(self):
        self.nivel_truco = 1
        self.ultimo_cantor = None
        self.activo = False
        self.terminado = False
        self.ganador = None

    def puede_cantar(self):
        return self.nivel_truco < 4 and not self.terminado

    def cantar(self, jugador):
        print(f"Nivel: {self.nivel_truco}")
        print(f"¿Terminado?: {self.terminado}")
        if not self.puede_cantar():
            return False

        self.nivel_truco += 1
        print(f"Nivel: {self.nivel_truco}")
        self.ultimo_cantor = jugador
        self.activo = True
        return True

    def cantar_retruco(self, jugador):
        print(f"Nivel: {self.nivel_truco}")
        print(f"¿Terminado?: {self.terminado}")
        if self.nivel_truco != 2 or self.terminado:
            return False

        self.nivel_truco += 1
        print(f"Nivel: {self.nivel_truco}")
        self.ultimo_cantor = jugador
        self.activo = True
        return True

    def aceptar(self):
        self.activo = False
    
    def cantar_vale_cuatro(self, jugador):
        print(f"Nivel: {self.nivel_truco}")
        print(f"¿Terminado?: {self.terminado}")
        if self.nivel_truco != 3 or self.terminado:
            return False

        self.nivel_truco += 1
        print(f"Nivel: {self.nivel_truco}")
        self.ultimo_cantor = jugador
        self.activo = True
        return True

    def rechazar(self, jugador_que_rechaza):
        self.terminado = True
        self.ganador = self.ultimo_cantor

    def puntos_en_juego(self):
        return self.nivel_truco

    def puntos_por_rechazo(self):
        return self.nivel_truco - 1

class JuegoTruco:
    def __init__(self, j1, j2, canto_truco, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.tanteador = tanteador
        self.canto_truco = canto_truco
    
    def jugar_truco(self):
        """
        Lógica para jugar una mano de truco, incluyendo el canto de truco 
        y la comparación de cartas.
        """
        no_quiero_truco = True
        se_canto_truco = False
        
        if self.j1.decidir_cantar_truco():
            self.jugador_canta_truco(1)
            se_canto_truco = True

            if not self.j2.aceptar_truco(self.j2.mano):
                no_quiero_truco = True
                self.jugador_no_quiso(1, 2)                
            else:
                no_quiero_truco = self.jugador_quiso_truco(2)
                
        elif self.j2.decidir_cantar_truco():
            self.jugador_canta_truco(2)
            se_canto_truco = True

            if not self.j1.aceptar_truco(self.j1.mano):
                no_quiero_truco = True
                self.jugador_no_quiso(2, 1)            
            else:
                no_quiero_truco = self.jugador_quiso_truco(1)

        elif not se_canto_truco:
            print("No se cantó truco, se procede a jugar la mano sin truco")            
            self.jugar_carta_mano(se_canto_truco)

        if not no_quiero_truco:
            self.jugar_carta_mano(se_canto_truco)
        else:        
            print("No se quiso el truco, se procede a mostrar el tanteador")

    def jugador_canta_truco(self, jugador):
        self.canto_truco.cantar(jugador)
        print(f"Jugador {jugador} canta Truco")

    def jugador_quiso_truco(self, numero):
    
        jugador = self.j1 if numero == 1 else self.j2
        rival = self.j2 if jugador == self.j1 else self.j1

        print(f"Jugador {jugador.nombre} quiso el truco")

        if not jugador.decidir_cantar_retruco():
            self.canto_truco.aceptar()
            return False

        self.canto_truco.cantar_retruco(jugador)
        print(f"Jugador {jugador.nombre} canta Retruco")
        print(f"Nivel: {self.canto_truco.nivel_truco}")

        if not rival.aceptar_retruco(rival.mano):
            self.jugador_no_quiso(
                self.numero_jugador(jugador),
                self.numero_jugador(rival)
            )
            return True

        print(f"Jugador {rival.nombre} quiso el Retruco")

        if not rival.decidir_cantar_vale_cuatro():
            self.canto_truco.aceptar()
            return False

        self.canto_truco.cantar_vale_cuatro(rival)
        print(f"Jugador {rival.nombre} canta Vale Cuatro")
        print(f"Nivel: {self.canto_truco.nivel_truco}")

        if not jugador.aceptar_vale_cuatro(jugador.mano):
            self.jugador_no_quiso(
                self.numero_jugador(rival),
                self.numero_jugador(jugador)
            )
            return True

        print(f"Jugador {jugador.nombre} quiso el Vale Cuatro")
        self.canto_truco.aceptar()

        return False

    def numero_jugador(jugador):
        return 1 if jugador == self.j1 else 2

    # def jugador_quiso_truco(self, jugador):
    #     jugador = self.j1 if jugador == 1 else self.j2
    #     otro_jugador = self.j2 if jugador == self.j1 else self.j1
    #     no_quiero = False

    #     print(f"Jugador {jugador.nombre} quiso el truco")   
        
    #     if jugador.decidir_cantar_retruco():
    #         self.canto_truco.cantar_retruco(jugador)
    #         print(f"Jugador {jugador.nombre} canta Retruco")
    #         self.canto_truco.nivel_truco = 3

    #         if otro_jugador.aceptar_retruco(otro_jugador.mano):
    #             self.canto_truco.aceptar()
    #             print(f"Jugador {otro_jugador.nombre} quiso el Retruco")

    #             if otro_jugador.decidir_cantar_vale_cuatro():
    #                 self.canto_truco.cantar_vale_cuatro(otro_jugador)
    #                 print(f"Jugador {otro_jugador.nombre} canta Vale Cuatro")                    
    #                 self.canto_truco.nivel_truco = 4

    #                 if jugador.aceptar_vale_cuatro(jugador.mano):
    #                     self.canto_truco.aceptar() 
    #                     print(f"Jugador {jugador.nombre} quiso el Vale Cuatro")
    #                 else:
    #                     no_quiero = True
    #                     self.jugador_no_quiso(1 if otro_jugador == self.j1 else 2, 1 if jugador == self.j1 else 2, 3)
    #             else:
    #                 self.canto_truco.aceptar()
    #                 print(f"Jugador {otro_jugador.nombre} quiso el retruco")  
    #         else:
    #             no_quiero = True
    #             self.jugador_no_quiso(1 if jugador == self.j1 else 2, 1 if otro_jugador == self.j1 else 2, 2)
    #     else:
    #         self.canto_truco.aceptar()

    #     return no_quiero

    def jugador_no_quiso(self, ganador, perdedor):
        parte_truco = "Truco" if self.canto_truco.nivel_truco == 2 else "Retruco" if self.canto_truco.nivel_truco == 3 else "Vale Cuatro"
        self.canto_truco.rechazar(perdedor)
        puntos = self.canto_truco.puntos_por_rechazo()
        print(f"Jugador {perdedor} no quiso el {parte_truco}")
        print(f"Jugador {ganador} gana {puntos} puntos por el rechazo del {parte_truco}")
        self.tanteador.sumar_puntos(ganador, puntos)

    def comparar_cartas(self, carta_j1, carta_j2):
        """
        Compara dos cartas y determina cuál es mayor.
        Retorna:
            1 si carta_j1 es mayor
            2 si carta_j2 es mayor
            0 si son iguales (parda)
        """        
        if valor_truco(carta_j1) > valor_truco(carta_j2):
            return 1
        elif valor_truco(carta_j2) > valor_truco(carta_j1):
            return 2
        else:
            return 0

    def determinar_ganador_mano(self, jugador_actual, otro_jugador, id_jugador_actual, id_otro_jugador, 
                               carta_en_juego, carta_jugada, primera, num_ronda):
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
            primera: ID del jugador que gano la primera ronda (1 o 2), 0 si fue parda
        
        Returns:
            ID del jugador que ganó la mano
        """
        carta_jugada = carta_en_juego if num_ronda == 1 else carta_jugada
        
        # print(f"Carta en juego: {carta_en_juego}, carta_jugada: {carta_jugada}")
        # print(f"Primera: {primera}, num_ronda: {num_ronda}")
        # print(f"Jugador actual: {id_jugador_actual}, lenght mano: {len(jugador_actual.mano)}")
        # print(f"Otro jugador: {id_otro_jugador}, lenght mano: {len(otro_jugador.mano)}")
        
        if (len(jugador_actual.mano) == 0 and len(otro_jugador.mano) == 0 and num_ronda == 3) or (len(jugador_actual.mano) == 0 and num_ronda > 1):
            return self.definir_ganador_parda_ultima_mano(id_jugador_actual, id_otro_jugador, carta_en_juego, carta_jugada, primera)
                    
        carta_respuesta = jugador_actual.analizar_jugada(carta_en_juego)
        print(f"Jugador {id_jugador_actual} juega: {carta_respuesta}")
        
        resultado = self.comparar_cartas(carta_en_juego, carta_respuesta)
        # print(f"Comparando {carta_en_juego} vs {carta_respuesta}, resultado: {resultado}")
        
        if resultado == 1: # quien jugó la carta anterior no mata
            print(f"Jugador {id_jugador_actual} no mata")
            return id_otro_jugador
        elif resultado == 2: # quien jugó la carta anterior mata
            print(f"Jugador {id_jugador_actual} mata con {carta_respuesta}")
            nueva_carta = jugador_actual.jugar_carta()
            carta_jugada = nueva_carta
            print(f"Jugador {id_jugador_actual} juega: {nueva_carta}")
            if len(otro_jugador.mano) > 0: # Si no es la última ronda, el otro jugador debe responder
                nueva_carta = otro_jugador.jugar_carta()
                print(f"Jugador {id_otro_jugador} juega: {nueva_carta}")
                carta_respuesta = nueva_carta
                return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                               id_jugador_actual, carta_respuesta, carta_jugada, primera, num_ronda + 1)
            return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                               id_jugador_actual, carta_respuesta, carta_jugada, primera, num_ronda + 1)
        else:
            print(f"Parda en ronda {num_ronda}")
            if len(jugador_actual.mano) < 0:
                nueva_carta = jugador_actual.jugar_carta()
                print(f"Jugador {id_jugador_actual} juega: {nueva_carta}")
                return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                               id_jugador_actual, carta_respuesta, carta_jugada, primera, num_ronda + 1)

            return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                               id_jugador_actual, carta_respuesta, carta_jugada, primera, num_ronda + 1)

    def definir_ganador_parda_ultima_mano(self, id_jugador_actual, id_otro_jugador, carta_en_juego, carta_jugada, primera):
        """
        Método que determina el ganador de la parda en la ultima mano.
        El flujo es: quien no mata pierde.
        
        Args:
            id_jugador_actual: ID del jugador actual (1 o 2)
            id_otro_jugador: ID del otro jugador (1 o 2)
            carta_en_juego: Carta que debe responder
            carta_jugada: Carta que ya esta en la mesa
            primera: ID del jugador que gano la primera ronda (1 o 2), 0 si fue parda
        
        Returns:
            ID del jugador que ganó la mano
        """
        
        resutado = self.comparar_cartas(carta_en_juego, carta_jugada)  # Comparamos la última carta con sí misma para determinar si es parda
        if resutado == 0:  # Si es parda, gana el que hizo la primera jugada
            if primera == 1:
                print("Parda en la última ronda, gana J1 por primera")
                return 1
            else:
                print("Parda en la última ronda, gana J2 por primera")
                return 2
        elif resutado == 1:
            print(f"Jugador {id_jugador_actual} gana por última carta")
            return id_jugador_actual
        else:
            print(f"Jugador {id_otro_jugador} gana por última carta")
            return id_otro_jugador

    def adjudicar_ganador_mano(self, id_ganador, se_canto_truco):
        id_perdedor = 1 if id_ganador == 2 else 2
        print(f"Jugador {id_perdedor} no mata.")
        """Suma los puntos al ganador de la mano"""
        puntos = 1 if not se_canto_truco else self.canto_truco.puntos_en_juego()
        print(f"\n>>> Gana Jugador {id_ganador} la mano")
        print(f">>> Puntos en juego: {puntos}\n")
        self.tanteador.sumar_puntos(id_ganador, puntos)

    def jugar_carta_mano(self, se_canto_truco):
        carta1_j1 = self.j1.jugar_carta()
        print(f"Jugador 1 juega: {carta1_j1}")
        if self.j2.decidir_empardar_jugada(carta1_j1):
            numero_buscado = carta1_j1.numero
            baraja = self.j2.mano
            for indice, carta in enumerate(baraja):
                if carta.numero == numero_buscado: # La carta es la buscada
                    carta_extraida = baraja.pop(indice)
                    break
            carta1_j2 = carta_extraida
            self.j2.mano = baraja
        else:
            carta1_j2 = self.j2.analizar_jugada(carta1_j1)
        resultado_inicial = self.comparar_cartas(carta1_j1, carta1_j2)
        print(f"Jugador 2 juega: {carta1_j2}")
        
        if resultado_inicial == 2:
            print(f"Jugador 2 mata")
            nueva_carta = self.j2.jugar_carta()
            print(f"Jugador 2 juega: {nueva_carta}")
            id_ganador = self.determinar_ganador_mano(self.j1, self.j2, 1, 2, nueva_carta, carta1_j2, 2, 2)
        elif resultado_inicial == 1:
            print(f"Jugador 2 no mata")
            nueva_carta = self.j1.jugar_carta()
            print(f"Jugador 1 juega: {nueva_carta}")
            id_ganador = self.determinar_ganador_mano(self.j2, self.j1, 2, 1, nueva_carta, carta1_j2, 1, 2)
        else:
            print("Parda en ronda 1")
            id_ganador = self.definir_ganador_parda_primera_mano(self.j1, self.j2, 1, 2)
        
        self.adjudicar_ganador_mano(id_ganador, se_canto_truco)
    
    def definir_ganador_parda_primera_mano(self, jugador_actual, otro_jugador, mano, num_ronda=1):
        """
        Método recursivo que determina el ganador de una mano en caso de parda.
        El flujo es: quien no mata pierde, o se puede seguir empardando, en caso de
        empardar tambien la ultima mano, gana el jugador que es mano.
        
        Args:
            jugador_actual: Jugador que debe responder
            otro_jugador: Jugador que jugó la carta anterior
            num_ronda: Número de ronda (1-3)
            primera: ID del jugador que gano la primera ronda (1 o 2), 0 si fue parda
        
        Returns:
            ID del jugador que ganó la mano
        """

        nueva_carta = jugador_actual.jugar_carta()
        print(f"Jugador 1 juega: {nueva_carta}")
        carta_otro_jugador = otro_jugador.analizar_jugada(nueva_carta)
        print(f"Jugador 2 juega: {carta_otro_jugador}")
        resultado = self.comparar_cartas(nueva_carta, carta_otro_jugador)

        if resultado == 1: # quien jugó la carta anterior no mata
            print(f"Jugador 2 no mata")
            return 1
        elif resultado == 2: # quien jugó la carta anterior mata
            print(f"Jugador 2 mata con {carta_otro_jugador}")
            return 2 
        else:
            print(f"Parda en ronda {num_ronda}")
            if num_ronda == 3:
                print("Parda en la última ronda, gana J1 por ser mano")
                return 1
            return self.determinar_ganador_parda(jugador_actual, otro_jugador, mano, num_ronda + 1)
