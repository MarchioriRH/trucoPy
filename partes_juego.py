from jugador import Jugador
from reglas import valor_truco
from reglas import valor_envido
from truco import CantoTruco
from envido import CantoEnvido
from tanteador import Tanteador
from estado_partido import EstadoPartido


class JugarTruco:
    def jugar_envido(self, j1, j2, canto_envido, tanteador):
        global parda

        tanto_j1 = j1.calcular_envido()
        tanto_j2 = j2.calcular_envido()

        print(f"J1 canta: {tanto_j1}")
        print(f"J2 canta: {tanto_j2}")
        
        #Ver porque suma todos los puntos. Ordenar main.
        if tanto_j1 > tanto_j2:
            print("Gana J1 el envido")
            print(f"Puntos en juego: {canto_envido.puntos_en_juego()}")           
            tanteador.sumar_puntos(1, canto_envido.puntos_en_juego())

        elif tanto_j1 < tanto_j2:
            print("Gana J2 el envido")
            print(f"Puntos en juego: {canto_envido.puntos_en_juego()}")
            tanteador.sumar_puntos(2, canto_envido.puntos_en_juego())
        
        else:
            print("Parda, gana J1")
            print(f"Puntos en juego: {canto_envido.puntos_en_juego()}")
            tanteador.sumar_puntos(1, canto_envido.puntos_en_juego())

        
    def verificar_flor(self, j1, j2, canto_envido, tanteador):  
        
        ganador_flor = -1
        flor_j1 = j1.verificar_flor()
        flor_j2 = j2.verificar_flor()

        if flor_j1 and not flor_j2:
            print("J1 canta flor")
            print(f"Puntos en juego: {canto_envido.puntos_flor()}")
            tanteador.sumar_puntos(1, canto_envido.puntos_flor())
            ganador_flor = 1
        elif flor_j2 and not flor_j1:
            print("J2 canta flor")
            print(f"Puntos en juego: {canto_envido.puntos_flor()}")
            j2_canto_flor = True
            tanteador.sumar_puntos(2, canto_envido.puntos_flor())
            ganador_flor = 2
        elif flor_j1 and flor_j2:
            print("Ambos tienen flor, se comparan los tantos")
            # j1_canto_flor = True
            # j2_canto_flor = True
            comparacion_flor_j1 = j1.calcular_envido()
            comparacion_flor_j2 = j2.calcular_envido()
            if comparacion_flor_j1 > comparacion_flor_j2:
                print("J1 gana la flor")
                print(f"Puntos en juego: {canto_envido.puntos_flor()}")
                tanteador.sumar_puntos(1, canto_envido.puntos_flor())
                ganador_flor = 1
            elif comparacion_flor_j2 > comparacion_flor_j1:
                print("J2 gana la flor")
                print(f"Puntos en juego: {canto_envido.puntos_flor()}")
                tanteador.sumar_puntos(2, canto_envido.puntos_flor())
                ganador_flor = 2
            else:
                print("Empate en la flor, gana J1")
                print(f"Puntos en juego: {canto_envido.puntos_flor()}")
                tanteador.sumar_puntos(1, canto_envido.puntos_flor())
                ganador_flor = 1
        return ganador_flor

    def comparar_cartas(self, carta_j1, carta_j2):
        if valor_truco(carta_j1) > valor_truco(carta_j2):
            return 1
        elif valor_truco(carta_j2) > valor_truco(carta_j1):
            return 2
        else:
            return 0

    def jugador2_hace_primera(self, j1, j2, carta1_j1, carta1_j2, tanteador, canto_truco):
        global j1_hizo_primera
        
        print(f"J2 juega carta 1: {carta1_j2} mata a {carta1_j1}")
        j2_hizo_primera = True
        carta2_j2 = j2.jugar_carta()
        # Juega la segunda carta
        print(f"J2 juega carta 2: {carta2_j2}")

        # J1 analiza la carta jugada por J2 y elige la carta a jugar
        carta2_j1 = j1.analizar_jugada(carta2_j2)
        # Si la carta de J1 mata a la carta de J2
        valor_comparacion = self.comparar_cartas(carta2_j1, carta2_j2)
        if valor_comparacion == 1:
            print(f"J1 juega carta 2: {carta2_j1} mata a {carta2_j2}")
            # J1 juega la tercera carta
            carta3_j1 = j1.jugar_carta()
            print(f"J1 juega carta 3: {carta3_j1}")

            # J2 analiza la carta jugada por J1 y elige la carta a jugar
            carta3_j2 = j2.analizar_jugada(carta3_j1)
            # Si la carta de J2 mata a la carta de J1
            resultado_comparacion = self.comparar_cartas(carta3_j1, carta3_j2)
            if resultado_comparacion == 2:
                print(f"J2 juega carta 3: {carta3_j2} mata a {carta3_j1}")
                print("Gana J2 la baza")
                print(f"Puntos en juego: {canto_truco.puntos_en_juego()}")
                tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
            elif resultado_comparacion == 1:
                # J2 no mata a la carta de J1, gana J1 la baza
                print(f"J2 no mata a {carta3_j1}")
                print("Gana J1 la baza")
                print(f"Puntos en juego: {canto_truco.puntos_en_juego()}")
                tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())
            else:
                print("Gana J2 por primera")
                print(f"Puntos en juego: {canto_truco.puntos_en_juego()}")
                tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())    
        else:
            # J1 no mata a la carta de J2, gana J2 la baza
            print(f"J1 no mata a {carta2_j2}")
            print("Gana J2 la baza")
            print(f"Puntos en juego: {canto_truco.puntos_en_juego()}")
            tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
               
    def jugador1_hace_primera(self, j1, j2, carta1_j1, carta1_j2, tanteador, canto_truco):
        global j2_hizo_primera

        print(f"J2 juega carta 1: {carta1_j2} no mata a {carta1_j1}")

        carta2_j1 = j1.analizar_jugada(carta1_j2)
        j1_hizo_primera = True
        print(f"J1 juega carta 2: {carta2_j1}")

        carta2_j2 = j2.analizar_jugada(carta2_j1)
        resultado_comparacion = self.comparar_cartas(carta2_j1, carta2_j2)
        if resultado_comparacion == 2:
            print(f"J2 juega carta 2: {carta2_j2} mata a {carta2_j1}")
            carta3_j2 = j2.jugar_carta()
            print(f"J2 juega carta 3: {carta3_j2}")

            carta3_j1 = j1.jugar_carta()
            resultado_comparacion = self.comparar_cartas(carta3_j1, carta3_j2)
            if resultado_comparacion == 1:
                print(f"J1 juega carta 3: {carta3_j1} mata a {carta3_j2}")
                print("Gana J1 la baza")
                print(f"Puntos en juego: {canto_truco.puntos_en_juego()}")
                tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())
            elif resultado_comparacion == 2:
                print(f"J1 no mata a {carta3_j2}")
                print("Gana J2 la baza")
                print(f"Puntos en juego: {canto_truco.puntos_en_juego()}")
                tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
            else:
                print("Gana J1 por primera")
                print(f"Puntos en juego: {canto_truco.puntos_en_juego()}")
                tanteador.sumar_puntos(1, canto_truco.puntos_en_juego()) 
        else:
            print(f"J2 no mata a {carta2_j1}")
            print("Gana J1 la baza")
            print(f"Puntos en juego: {canto_truco.puntos_en_juego()}")
            tanteador.sumar_puntos(1, canto_truco.puntos_en_juego()) 