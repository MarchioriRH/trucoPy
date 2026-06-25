from canto_truco import CantoTruco
from reglas import valor_truco, REGLAS_TRUCO
from tanteador import Tanteador
import random
from arbitro_truco import ArbitroTruco, EstadoTruco
from estrategia_truco_humana import TrucoHumanoAdaptativo



class JuegoTruco:
    def __init__(self, j1, j2, canto_truco, tanteador, estado):
        self.j1 = j1
        self.j2 = j2
        self.tanteador = tanteador
        self.canto_truco = canto_truco
        self.estado = estado
     
        self.truco_humano = TrucoHumanoAdaptativo()
        self.arbitro = ArbitroTruco(self.j1, self.j2)
        self.turno_actual = "Humano"  # Quién tiene el turno para jugar/cantar
        self.mano_finalizada = False

    def jugar_truco(self):
        while not self.mano_finalizada:
            # 1. Verificar si hay apuestas pendientes que resolver
            print(f"Estado actual inicial: {self.arbitro.estado_actual}")
            if self.arbitro.estado_actual in [EstadoTruco.TRUCO_PENDIENTE, 
                                            EstadoTruco.RETRUCO_PENDIENTE, 
                                            EstadoTruco.VALE_4_PENDIENTE]:
                print(f"ENTRO A RESOLVER APUESTA")
                self.resolver_apuesta_pendiente()
                continue  # RECOMENDADO: Reinicia el bucle para evaluar el nuevo estado consolidado

            # 2. Si no hay apuestas pendientes, se juegan cartas o se canta
            if self.turno_actual == "Humano":
                # Condición extra: Solo canta si el estado actual permite cantar Truco (VALE_1)
                if self.arbitro.estado_actual == EstadoTruco.VALE_1 and self.truco_humano.decidir_cantar(self.j1.mano, self.estado):
                    self.arbitro.cantar_truco(self.j1)
                    continue # Volvemos al inicio del while para que el if de "PENDIENTE" lo capture inmediatamente
                
                print(f"Estado actual antes de jugar carta: {self.arbitro.estado_actual}")
                carta = self.j1.jugar_carta()
                # IMPORTANTE: Aquí debes cambiar el turno o romper el bucle temporalmente 
                # para que no sea un while infinito de la misma acción.
                self.turno_actual = "Computadora" 
            else:
                self.turno_computadora(carta)
                self.turno_actual = "Humano"

    def turno_computadora(self, carta):
        if self.arbitro.estado_actual == EstadoTruco.TRUCO:
            if self.j2.decidir_cantar_retruco():
                self.arbitro.cantar_retruco(self.j2)
                return True
            else:
                carta_respuesta = self.j2.analizar_jugada(carta)
                respuesta = self.comparar_cartas(carta, carta_respuesta)
                print(f"{self.j2.nombre} jugo {carta_respuesta}")

                if respuesta == 2:
                    carta_respuesta = self.j2.jugar_carta()
                    print(f"{self.j2.nombre} jugo {carta_respuesta}")
                elif respuesta == 1:
                    return False
                return True

        
    def resolver_apuesta_pendiente(self):
        respondedor_str = "Computadora" if self.turno_actual == "Humano" else "Humano"
        jugador_respondedor = self.j2 if respondedor_str == "Computadora" else self.j1
        jugador_rival = self.j1 if respondedor_str == "Computadora" else self.j2
        
        print(f"\n--- INTERRUPCIÓN: {respondedor_str} debe responder a la apuesta ---")
        
        if respondedor_str == "Computadora":
            decision = self.j2.estrategia_truco.aceptar(self.j2.mano, self.canto_truco.nivel_truco, self.estado)
            if decision == "QUIERO":
                # Deja que el árbitro se encargue de todo el cambio de estado y puntos
                self.arbitro.responder_quiero(self.j2) 
                print(f"Estado truco despues quiero: {self.arbitro.estado_actual}")
            else:
                self.arbitro.responder_no_quiero(self.j2)
                jugador_rival.puntos += self.arbitro.puntos_en_juego
                self.mano_finalizada = True
        else:
            print("1. Quiero\n2. No quiero\n3. Retruco (si corresponde)")
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                self.arbitro.responder_quiero(self.j1)
            elif opcion == "2":
                self.arbitro.responder_no_quiero(self.j1)
                jugador_rival.puntos += self.arbitro.puntos_en_juego
                self.mano_finalizada = True






    def nombre_jugador(self, jugador):
        return self.j1.nombre if jugador == 1 else self.j2.nombre

    def jugador_quiso(self):
        pass

    def jugador_canta_truco(self, jugador):
        self.canto_truco.cantar(jugador)
        print(f"{self.nombre_jugador(jugador)} canta Truco")

    def jugador_quiso_truco(self, numero):

        jugador = self.j1 if numero == 1 else self.j2
        rival = self.j2 if jugador == self.j1 else self.j1

        print(f"{jugador.nombre} quiso el truco")

        if not jugador.decidir_cantar_retruco():
            self.canto_truco.aceptar()
            return False

        self.canto_truco.cantar_retruco(jugador)
        print(f"{jugador.nombre} canta Retruco")

        if not rival.aceptar_retruco(rival.mano):
            self.jugador_no_quiso(
                self.numero_jugador(jugador),
                self.numero_jugador(rival)
            )
            return True

        print(f"{rival.nombre} quiso el Retruco")

        if not rival.decidir_cantar_vale_cuatro():
            self.canto_truco.aceptar()
            return False

        self.canto_truco.cantar_vale_cuatro(rival)
        print(f"{rival.nombre} canta Vale Cuatro")

        if not jugador.aceptar_vale_cuatro(jugador.mano):
            self.jugador_no_quiso(
                self.numero_jugador(rival),
                self.numero_jugador(jugador)
            )
            return True

        print(f"{jugador.nombre} quiso el Vale Cuatro")
        self.canto_truco.aceptar()

        return False

    def numero_jugador(jugador):
        return 1 if jugador == self.j1 else 2

    def jugador_no_quiso(self, ganador, perdedor):
        parte_truco = "Truco" if self.canto_truco.nivel_truco == 2 else "Retruco" if self.canto_truco.nivel_truco == 3 else "Vale Cuatro"
        self.canto_truco.rechazar(perdedor)
        puntos = self.canto_truco.puntos_por_rechazo()
        print(f"{self.nombre_jugador(perdedor)} no quiso el {parte_truco}")
        print(f"{self.nombre_jugador(ganador)} gana {puntos} puntos por el rechazo del {parte_truco}")
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
        
        if (len(jugador_actual.mano) == 0 and len(otro_jugador.mano) == 0 and num_ronda == 3) or (len(jugador_actual.mano) == 0 and num_ronda > 1):
            return self.definir_ganador_parda_ultima_mano(id_jugador_actual, id_otro_jugador, carta_en_juego, carta_jugada, primera)
        if jugador_actual == 2:            
            carta_respuesta = jugador_actual.analizar_jugada(carta_en_juego)
        else:
            carta_respuesta = jugador_actual.jugar_carta()

        print(f"{jugador_actual.nombre} juega: {carta_respuesta}")
        
        resultado = self.comparar_cartas(carta_en_juego, carta_respuesta)
        # print(f"Comparando {carta_en_juego} vs {carta_respuesta}, resultado: {resultado}")
        
        if resultado == 1: # quien jugó la carta anterior no mata
            print(f"{jugador_actual.nombre} no mata")
            return id_otro_jugador
        elif resultado == 2: # quien jugó la carta anterior mata
            print(f"{jugador_actual.nombre} mata con {carta_respuesta}")
            nueva_carta = jugador_actual.jugar_carta()
            carta_jugada = nueva_carta
            print(f"{jugador_actual.nombre} juega: {nueva_carta}")
            if len(otro_jugador.mano) > 0: # Si no es la última ronda, el otro jugador debe responder
                nueva_carta = otro_jugador.jugar_carta()
                print(f"{otro_jugador.nombre} juega: {nueva_carta}")
                carta_respuesta = nueva_carta
                # return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                            #    id_jugador_actual, carta_respuesta, carta_jugada, primera, num_ronda + 1)
            return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                            id_jugador_actual, carta_respuesta, carta_jugada, primera, num_ronda + 1)
        else:
            print(f"Parda en ronda {num_ronda}")
            if len(jugador_actual.mano) < 0:
                nueva_carta = jugador_actual.jugar_carta()
                print(f"{jugador_actual.nombre} juega: {nueva_carta}")
                # return self.determinar_ganador_mano(otro_jugador, jugador_actual, id_otro_jugador, 
                                            #    id_jugador_actual, carta_respuesta, carta_jugada, primera, num_ronda + 1)

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
                print(f"Parda en la última ronda, gana {self.j1.nombre} por primera")
                return 1
            else:
                print(f"Parda en la última ronda, gana {self.j2.nombre} por primera")
                return 2
        elif resutado == 1:
            print(f"{self.nombre_jugador(id_jugador_actual)} gana por última carta")
            return id_jugador_actual
        else:
            print(f"{self.nombre_jugador(id_otro_jugador)} gana por última carta")
            return id_otro_jugador

    def adjudicar_ganador_mano(self, id_ganador, se_canto_truco):
        id_perdedor = 1 if id_ganador == 2 else 2
        # if self.ronda < 3:
        #     print(f"{self.nombre_jugador(id_perdedor)} no mata.")
        """Suma los puntos al ganador de la mano"""
        puntos = 1 if not se_canto_truco else self.canto_truco.puntos_en_juego()
        print(f"\n>>> Gana {self.nombre_jugador(id_ganador)} la mano")
        print(f">>> Puntos en juego: {puntos}\n")
        self.tanteador.sumar_puntos(id_ganador, puntos)

    def jugar_carta_mano(self, se_canto_truco):
        carta1_j1 = self.j1.jugar_carta()
        print(f"{self.j1.nombre} juega: {carta1_j1}")
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
        print(f"{self.j2.nombre} juega: {carta1_j2}")
        
        if resultado_inicial == 2:
            print(f"{self.j2.nombre} mata")
            nueva_carta = self.j2.jugar_carta()
            print(f"{self.j2.nombre} juega: {nueva_carta}")
            id_ganador = self.determinar_ganador_mano(self.j1, self.j2, 1, 2, nueva_carta, carta1_j2, 2, 2)
        elif resultado_inicial == 1:
            print(f"{self.j2.nombre} no mata")
            nueva_carta = self.j1.jugar_carta()
            print(f"{self.j1.nombre} juega: {nueva_carta}")
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
        print(f"{self.j1.nombre} juega: {nueva_carta}")
        carta_otro_jugador = otro_jugador.analizar_jugada(nueva_carta)
        print(f"{self.j2.nombre} juega: {carta_otro_jugador}")
        resultado = self.comparar_cartas(nueva_carta, carta_otro_jugador)

        if resultado == 1: # quien jugó la carta anterior no mata
            print(f"{self.j2.nombre} no mata")
            return 1
        elif resultado == 2: # quien jugó la carta anterior mata
            print(f"{self.j2.nombre} mata con {carta_otro_jugador}")
            return 2 
        else:
            print(f"Parda en ronda {num_ronda}")
            if num_ronda == 3:
                print(f"Parda en la última ronda, gana {self.j1.nombre} por ser mano")
                return 1
            return self.definir_ganador_parda_primera_mano(jugador_actual, otro_jugador, mano, num_ronda + 1)
