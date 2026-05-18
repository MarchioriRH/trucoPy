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

    # def jugador2_hace_primera(self, self.j1, self.j2, carta1_self.j1, carta1_self.j2, self.tanteador, self.canto_truco):
    #     global self.j1_hizo_primera
        
    #     print(f"self.j2 juega carta 1: {carta1_self.j2} mata a {carta1_self.j1}")
    #     self.j2_hizo_primera = True
    #     carta2_self.j2 = self.j2.jugar_carta()
    #     # Juega la segunda carta
    #     print(f"self.j2 juega carta 2: {carta2_self.j2}")

    #     # self.j1 analiza la carta jugada por self.j2 y elige la carta a jugar
    #     carta2_self.j1 = self.j1.analizar_jugada(carta2_self.j2)
    #     # Si la carta de self.j1 mata a la carta de self.j2
    #     valor_comparacion = self.comparar_cartas(carta2_self.j1, carta2_self.j2)
    #     if valor_comparacion == 1:
    #         print(f"self.j1 juega carta 2: {carta2_self.j1} mata a {carta2_self.j2}")
    #         # self.j1 juega la tercera carta
    #         carta3_self.j1 = self.j1.jugar_carta()
    #         print(f"self.j1 juega carta 3: {carta3_self.j1}")

    #         # self.j2 analiza la carta jugada por self.j1 y elige la carta a jugar
    #         carta3_self.j2 = self.j2.analizar_jugada(carta3_self.j1)
    #         # Si la carta de self.j2 mata a la carta de self.j1
    #         resultado_comparacion = self.comparar_cartas(carta3_self.j1, carta3_self.j2)
    #         if resultado_comparacion == 2:                
    #             self.jugador_mata_carta(carta3_self.j2, carta3_self.j1, self.canto_truco, self.tanteador, 2)
    #         elif resultado_comparacion == 1:               
    #             self.jugador_mata_carta(carta3_self.j1, carta3_self.j2, self.canto_truco, self.tanteador, 1)
    #         else:               
    #             self.jugador_gana_por_primera(carta3_self.j1, carta3_self.j2, self.canto_truco, self.tanteador, 2)  
    #     else:
    #         self.jugador_no_mata_carta(carta2_self.j1, carta2_self.j2, self.canto_truco, self.tanteador, 1)

    def jugador_mata_carta(self, carta_ganadora, carta_perdedora, jugador):
        print(f"Jugador {jugador} juega carta 3: {carta_ganadora} mata a {carta_perdedora}")
        print(f"Gana jugador {jugador} la baza")
        print(f"Puntos en juego: {self.canto_truco.puntos_en_juego()}")
        self.tanteador.sumar_puntos(jugador, self.canto_truco.puntos_en_juego())

    def jugador_no_mata_carta(self, carta_ganadora, carta_perdedora, jugador):
        print(f"Jugador {jugador} no mata a {carta_perdedora}")
        print(f"Gana jugador {jugador} la baza")
        print(f"Puntos en juego: {self.canto_truco.puntos_en_juego()}")
        self.tanteador.sumar_puntos(jugador, self.canto_truco.puntos_en_juego())

    def jugador_gana_por_primera(self, carta_ganadora, carta_perdedora, jugador):
        print(f"Gana jugador {jugador} por primera")
        print(f"Puntos en juego: {self.canto_truco.puntos_en_juego()}")
        self.tanteador.sumar_puntos(jugador, self.canto_truco.puntos_en_juego())

    # Ver como hacer para que no se mezclen las juagadas
    def jugador_hace_primera(self, jugador, ganador, perdedor, carta_ganadora, carta_perdedora):
        
        # global self.j2_hizo_primera
        #print(f"Jugador {jugador} juega carta 1: {carta_ganadora}")

        print(f"{perdedor.nombre} juega carta 1: {carta_perdedora} no mata a {carta_ganadora}")

        carta2_ganador = ganador.analizar_jugada(carta_perdedora)
        # self.j1_hizo_primera = True
        print(f"{ganador.nombre} juega carta 2: {carta2_ganador}")

        carta2_perdedor = perdedor.analizar_jugada(carta2_ganador)
        resultado_comparacion = self.comparar_cartas(carta2_ganador, carta2_perdedor)
        
        if resultado_comparacion == 2:
            print(f"{perdedor.nombre} juega carta 2: {carta2_perdedor} mata a {carta2_ganador}")
            carta3_perdedor = perdedor.jugar_carta()
            print(f"{perdedor.nombre} juega carta 3: {carta3_perdedor}")

            carta3_ganador = ganador.jugar_carta()
            print(f"{ganador.nombre} juega carta 3: {carta3_ganador}")

            resultado_comparacion = self.comparar_cartas(carta3_ganador, carta3_perdedor)
            if resultado_comparacion == 1:
                self.jugador_mata_carta(carta3_perdedor, carta3_ganador, 1)
            elif resultado_comparacion == 2:
                self.jugador_mata_carta(carta3_ganador, carta3_perdedor, 2)
            else:
                self.jugador_gana_por_primera(carta3_ganador, carta3_perdedor, 1)
        else:
            self.jugador_no_mata_carta(carta2_perdedor, carta2_ganador, 2)

    # def mano_parda(self, self.j1, self.j2, carta1_j1, carta1_.j2):
        
    #     print(f"J2 juega carta 1: {carta1_j2}")
    #     parda = True
    #     print("Parda")
    #     carta2_self.j1 = self.j1.jugar_carta()
    #     print(f"self.j1 juega carta 2: {carta2_self.j1}")
    #     carta2_self.j2 = self.j2.jugar_carta()
    #     print(f"self.j2 juega carta 2: {carta2_self.j2}")
    #     resultado_comparacion = self.comparar_cartas(carta2_self.j1, carta2_self.j2)
    #     if resultado_comparacion == 1:
    #         print(f"self.j1 juega carta 2: {carta2_self.j1} mata a {carta2_self.j2}")
    #         print("Gana self.j1 la baza")
    #         self.tanteador.sumar_puntos(1, self.canto_truco.puntos_en_juego())
    #     elif resultado_comparacion == 2:
    #         print(f"self.j2 juega carta 2: {carta2_self.j2} mata a {carta2_self.j1}")
    #         print("Gana self.j2 la baza")
    #         self.tanteador.sumar_puntos(2, self.canto_truco.puntos_en_juego())
    #     elif resultado_comparacion == 0:
    #         print("2da Parda")
    #         carta3_self.j1 = self.j1.jugar_carta()
    #         print(f"self.j1 juega carta 3: {carta3_self.j1}")
    #         carta3_self.j2 = self.j2.jugar_carta()
    #         print(f"self.j2 juega carta 3: {carta3_self.j2}")
    #         resultado_comparacion = self.comparar_cartas(carta3_self.j1, carta3_self.j2)
    #         if resultado_comparacion == 1:
    #             print(f"self.j1 juega carta 3: {carta3_self.j1} mata a {carta3_self.j2}")
    #             print("Gana self.j1 la baza")
    #             self.tanteador.sumar_puntos(1, self.canto_truco.puntos_en_juego())
    #         elif resultado_comparacion == 2:
    #             print(f"self.j2 juega carta 3: {carta3_self.j2} mata a {carta3_self.j1}")
    #             print("Gana self.j2 la baza")
    #             self.tanteador.sumar_puntos(2, self.canto_truco.puntos_en_juego())
    #         else:    
    #             print("3era parda, nadie gana la baza")

    def jugar_carta_mano(self):    
        parda = False

        carta1_j1 = self.j1.jugar_carta()
        print(f"Jugador 1 juega carta 1: {carta1_self.j1}")
        
        carta1_j2 = self.j2.analizar_jugada(carta1_j1) 
        resultado_comparacion = self.comparar_cartas(carta1_j1, carta1_j2)
        print(f"Resultado comparación carta 1: {resultado_comparacion} (1: j1 gana, 2: j2 gana, 0: Parda)")
        # self.j2 hace primera
        
        if resultado_comparacion == 2:
            self.jugador_hace_primera(2, self.j2, self.j1, carta1_j2, carta1_j1)       
        # self.j1 hace primera           
        elif resultado_comparacion == 1:
            self.jugador_hace_primera(1, self.j1, self.j2, carta1_j1, carta1_j2)
        # Parda    
        elif resultado_comparacion == 0:
            self.mano_parda(self.j1, self.j2, carta1_j1, carta1_j2)
       