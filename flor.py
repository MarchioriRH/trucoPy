from canto_envido import CantoEnvido
from canto_flor import CantoFlor

class JuegoFlor:
    def __init__(self, j1, j2, canto_flor, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.canto_flor = canto_flor
        self.tanteador = tanteador

    def validar_flor(self, mano):
        palos = {}
        for carta in mano:
            if carta.palo not in palos:
                palos[carta.palo] = []
            palos[carta.palo].append(carta)

        for cartas in palos.values():
            if len(cartas) >= 3:
                return sum(carta.numero for carta in cartas[:3]) + 20
        return 0      

    def verificar_flor(self, jugador):
        if self.validar_flor(jugador.mano) > 0:
            # print(f"Jugador {jugador.nombre} canta flor")
            return True
        return False
    
    def jugar_flor(self):
        flor_ganadora = []
        ganador_flor = -1     
        if self.verificar_flor(self.j1) and self.verificar_flor(self.j2):
            print(f"Jugador 1 canta flor")
            self.canto_flor.cantar(self.j1)        
            self.canto_flor.cantar(self.j2)      
            contra_flor1 = self.j2.estrategia_flor.decidir_cantar_contra_flor(self.j2, self.j2.estado)
            if contra_flor1 > 0:
                if contra_flor1 == 1:
                    print("Jugador 2 canta contra flor al resto.")
                    if self.j1.estrategia_flor.decidir_aceptar_contraflor_al_resto(self.j1, self.j1.estado):
                        print("Jugador 1 quiere.")
                        ganador_flor = self.definir_ganador()
                        if self.tanteador.esta_en_buenas(ganador_flor):                            
                            self.tanteador.sumar_puntos(ganador_flor, self.tanteador.calcular_puntos_restantes(1))
                        else:
                            self.tanteador.sumar_puntos(ganador_flor, 15 - self.tanteador.puntos_jugador(ganador_flor))
                        flor_ganadora = self.j1.mano[:] if ganador_flor == 1 else self.j2.mano[:]
                        self.canto_flor.terminado = True
                        return flor_ganadora, ganador_flor
                    else:
                        print("Jugador 1 no quiere.")
                        self.canto_flor.rechazar(self.j1)
                        ganador_flor = 2            
                        self.tanteador.sumar_puntos(ganador_flor, self.canto_flor.puntos_por_rechazo())
                        flor_ganadora = []
                        print(f"Puntos en juego: {self.canto_flor.puntos_por_rechazo()}")
                        return flor_ganadora, ganador_flor
                elif contra_flor1 == 2:
                    print("Jugador 2 canta contra flor al partido.")
                    if self.j1.estrategia_flor.decidir_aceptar_contraflor_al_partido(self.j1, self.j1.estado):
                        print("Jugador 1 quiere.")
                        ganador_flor = self.definir_ganador()
                        self.tanteador.sumar_puntos(ganador_flor, self.tanteador.calcular_puntos_restantes())
                        flor_ganadora = self.j1.mano[:] if ganador_flor == 1 else self.j2.mano[:]
                        self.canto_flor.terminado = True
                        return flor_ganadora, ganador_flor
                    else:
                        print("Jugador 1 no quiere.")
                        self.canto_flor.rechazar(self.j1)
                        ganador_flor = 2            
                        self.tanteador.sumar_puntos(ganador_flor, self.canto_flor.puntos_por_rechazo())
                        flor_ganadora = []
                        print(f"Puntos en juego: {self.canto_flor.puntos_por_rechazo()}")
                        return flor_ganadora, ganador_flor
                    
            else:            
                print(f"Jugador {j1.nombre} canta flor")
                print(f"Jugador {j2.nombre} canta flor")
                ganador_flor = self.definir_ganador()

        elif self.verificar_flor(self.j1):
            self.canto_flor.cantar(self.j1)
            ganador_flor = 1
        elif self.verificar_flor(self.j2):
            self.canto_flor.cantar(self.j2)
            ganador_flor = 2

        if ganador_flor == 1:
            self.jugador_gano_flor(1)
            flor_ganadora = self.j1.mano[:]
        elif ganador_flor == 2:
            self.jugador_gano_flor(2)
            flor_ganadora = self.j2.mano[:]
        else:
            self.jugador_gano_flor(0)  
            flor_ganadora = self.j1.mano[:]

        if ganador_flor == -1:
            print("Ningún jugador tiene flor")        

        return flor_ganadora, ganador_flor

    def definir_ganador(self):
        res = self.comparar_flor()        
        return 1 if res == 1 else 2 if res == 2 else 0

    def comparar_flor(self):
        f1 = self.validar_flor(self.j1.mano)
        print(f"Valor flor J1: {f1}")
        f2 = self.validar_flor(self.j2.mano)
        print(f"Valor flor J2: {f2}")
        return 1 if f1 > f2 else 2 if f2 > f1 else 0

    def jugador_gano_flor(self, jugador):
        self.mostrar_resultado_ganador_flor(jugador)
        # self.tanteador.sumar_puntos(jugador, self.canto_flor.puntos_flor())
        ganador_flor = jugador
        return ganador_flor

    def mostrar_resultado_ganador_flor(self, jugador):
        if jugador == 0:
            print("Empate en la ronda, gana J1 por ser mano")
        else:
            print(f"Jugador {jugador} gana la flor")
        
        print(f"Puntos en juego: {self.canto_flor.puntos_flor()}")
        self.tanteador.sumar_puntos(1, self.canto_flor.puntos_flor())