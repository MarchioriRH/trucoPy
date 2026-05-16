class CantoEnvido:
    def __init__(self):
        self.nivel = 1
        self.ultimo_cantor = None
        self.activo = False
        self.terminado = False
        self.ganador = None

    def puede_cantar(self):
        return self.nivel < 4 and not self.terminado

    def cantar(self, jugador):
        if not self.puede_cantar():
            return False

        self.nivel += 1
        self.ultimo_cantor = jugador
        self.activo = True
        return True

    def aceptar(self):
        self.activo = False

    def rechazar(self, jugador_que_rechaza):
        self.terminado = True
        self.ganador = self.ultimo_cantor

    def puntos_en_juego(self):
        return self.nivel

    def puntos_por_rechazo(self):
        return self.nivel - 1

    def puntos_flor(self):
        return 3

class JuegoEnvido:
    def comparar_tantos(self, j1, j2, canto_envido, tanteador):
        global parda

        tanto_j1 = j1.calcular_envido()
        tanto_j2 = j2.calcular_envido()

        print(f"J1 canta: {tanto_j1}")
        print(f"J2 canta: {tanto_j2}")
        
        #Ver porque suma todos los puntos. Ordenar main.
        if tanto_j1 > tanto_j2:
            self.mostrar_ganador_envido(1, canto_envido, tanteador)
        elif tanto_j1 < tanto_j2:
            self.mostrar_ganador_envido(2, canto_envido, tanteador)        
        else:
            parda = True
            self.mostrar_ganador_envido(1, canto_envido, tanteador)

    def mostrar_ganador_envido(self, ganador, canto_envido, tanteador):
        if ganador == 0:
            print("Parde en el envido, gana J1 por ser mano")
        else:
            print(f"Jugador {ganador} gana el envido")
        
        print(f"Puntos en juego: {canto_envido.puntos_en_juego()}")
        tanteador.sumar_puntos(ganador, canto_envido.puntos_en_juego())

    def jugar_envido(self, j1, j2, canto_envido, tanteador): 
        no_quiero_envido = False
        se_canto_envido = False
        
        if j1.decidir_cantar_envido():
            self.jugador_canto_envido(1, j1, canto_envido)
            se_canto_envido = True
            
            if not j2.aceptar_envido(j2.mano):
                no_quiero_envido = True
                self.jugador_no_quiso_envido(2, canto_envido, tanteador)
                                
            else:
                self.jugador_quiso_envido(1, j1, j2, canto_envido, tanteador)
               
        elif j2.decidir_cantar_envido():
            self.jugador_canto_envido(2, j2, canto_envido)
            se_canto_envido = True

            if not j1.aceptar_envido(j1.mano):
                no_quiero_envido = True
                self.jugador_no_quiso_envido(1, canto_envido, tanteador)
                               
            else:
                self.jugador_quiso_envido(2, j1, j2, canto_envido, tanteador)
               
        if no_quiero_envido:
            print("No se quiso el envido, se procede al truco")
        if not se_canto_envido:
            print("No se canto el envido, se procede al truco")
            se_canto_envido = True

    def jugador_canto_envido(self, jugador, j2, canto_envido):
        canto_envido.cantar(j2)
        print(f"Jugador {jugador} canta Envido")
    
    def jugador_quiso_envido(self, jugador, j1, j2, canto_envido, tanteador):
        canto_envido.aceptar()
        print(f"Jugador {jugador} quiso")
        self.comparar_tantos(j1, j2, canto_envido, tanteador)
    
    def jugador_no_quiso_envido(self, jugador, canto_envido, tanteador):
        canto_envido.rechazar(jugador)
        print(f"Jugador {jugador} no quiso")
        print(f"Jugador {jugador} gana", canto_envido.puntos_por_rechazo())
        tanteador.sumar_puntos(jugador, canto_envido.puntos_por_rechazo())