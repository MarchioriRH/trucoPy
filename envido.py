class JuegoEnvido:
    def __init__(self, j1, j2, canto_envido, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.tanteador = tanteador
        self.canto_envido = canto_envido

    def comparar_tantos(self):
        global parda

        tanto_j1 = self.j1.calcular_envido()
        tanto_j2 = self.j2.calcular_envido()

        print(f"J1 canta: {tanto_j1}")
        print(f"J2 canta: {tanto_j2}")
        
        #Ver porque suma todos los puntos. Ordenar main.
        if tanto_j1 > tanto_j2:
            self.mostrar_ganador_envido(1)
        elif tanto_j1 < tanto_j2:
            self.mostrar_ganador_envido(2)        
        else:
            parda = True
            self.mostrar_ganador_envido(1)

    def mostrar_ganador_envido(self, ganador):
        if ganador == 0:
            print("Parde en el envido, gana J1 por ser mano")
        else:
            print(f"Jugador {ganador} gana el envido")
        
        print(f"Puntos en juego: {self.canto_envido.puntos_en_juego()}")
        self.tanteador.sumar_puntos(ganador, self.canto_envido.puntos_en_juego())

    def jugar_envido(self): 
        no_quiero_envido = False
        se_canto_envido = False
        
        if self.j1.decidir_cantar_envido():
            self.jugador_canto_envido(1)
            se_canto_envido = True
            
            if not self.j2.aceptar_envido(self.j2.mano):
                no_quiero_envido = True
                self.jugador_no_quiso_envido(2)
                                
            else:
                self.jugador_quiso_envido(2)
               
        elif self.j2.decidir_cantar_envido():
            self.jugador_canto_envido(2)
            se_canto_envido = True

            if not self.j1.aceptar_envido(self.j1.mano):
                no_quiero_envido = True
                self.jugador_no_quiso_envido(1)
                               
            else:
                self.jugador_quiso_envido(1)
               
        if no_quiero_envido:
            print("No se quiso el envido, se procede al truco")
        if not se_canto_envido:
            print("No se canto el envido, se procede al truco")
            se_canto_envido = True

    def jugador_canto_envido(self, jugador):
        self.canto_envido.cantar(jugador)
        print(f"Jugador {jugador} canta Envido")
    
    def jugador_quiso_envido(self, jugador):
        self.canto_envido.aceptar()
        print(f"Jugador {jugador} quiso")
        self.comparar_tantos()
    
    def jugador_no_quiso_envido(self, jugador):
        self.canto_envido.rechazar(jugador)
        print(f"Jugador {jugador} no quiso")
        print(f"Jugador {jugador} gana", self.canto_envido.puntos_por_rechazo())
        self.tanteador.sumar_puntos(jugador, self.canto_envido.puntos_por_rechazo())