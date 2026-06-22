from reglas import REGLAS_TANTO

class JuegoEnvido:
    def __init__(self, j1, j2, canto_envido, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.tanteador = tanteador
        self.canto_envido = canto_envido    
    
    def jugar_envido(self, mano):
        estado_actual = "NADA"
        puntos_acumulados_quiero = 0
        puntos_acumulados_no_quiero = 1 # El mínimo por no querer nada es 1
        
        # Definimos quién arranca (ej: jugador 1)
        jugadores_que_pasaron = 0
        turno = mano 
        
        while True:
            jugador_actual = self.j1 if turno == 1 else self.j2
            rival = self.j2 if turno == 1 else self.j1
            
            # 1. Le pedimos a la estrategia del jugador su decisión basada en las opciones válidas
            opciones_validas = REGLAS_TANTO[estado_actual]["opciones"]
            
            # El jugador decide la mejora estrategia
            decision = self.consultar_estrategia(jugador_actual, estado_actual, opciones_validas)
            
            print(f"Jugador {turno} ({jugador_actual.nombre}) decide: {decision} en estado {estado_actual}")

            # --- MANEJO ESPECIAL DEL PASO ---
            if decision == "PASO":
                jugadores_que_pasaron += 1
                if jugadores_que_pasaron == 2:
                    print("Ningún jugador cantó el tanto. Se procede al truco.")
                    break # Rompe el bucle, nadie suma puntos de envido
                
                # Si solo pasó el primero, le damos la palabra al segundo
                turno = 2 if turno == 1 else 1
                continue # Salta al inicio del bucle 'while' sin ejecutar el código de abajo
            
            # Si alguien canta algo después de un PASO, reseteamos el contador
            jugadores_que_pasaron = 0

            # 2. Procesamos la decisión
            if decision == "QUIERO":
                print(f"Puntos acumulados: {puntos_acumulados_quiero}")
                self.jugador_quiso(turno, puntos_acumulados_quiero)
                #print(f"Se aceptó el tanto. Puntos en juego: {puntos_acumulados_quiero}")
                break
                
            elif decision == "NO_QUIERO":
                # self.jugador_no_quiso_envido(turno)
                self.tanteador.sumar_puntos(ganador, puntos_acumulados_no_quiero)  
                ganador_puntos = 2 if turno == 1 else 1
                print(f"No se quiso. Jugador {ganador_puntos} gana {puntos_acumulados_no_quiero} punto(s).")
                break
                
            else:
                # Si no es Quiero/No Quiero, es un canto (ENVIDO, REAL_ENVIDO, etc.)
                print(f"Jugador {turno} cantó: {decision}")
                
                # Actualizamos el arrastre de puntos según la historia del canto
                nuevo_estado = decision if (estado_actual != "ENVIDO" or decision != "ENVIDO") else "ENVIDO_ENVIDO"
                
                # Lógica de acumulación del Envido:
                puntos_acumulados_no_quiero = REGLAS_TANTO[estado_actual]["puntos_quiero"] if estado_actual != "NADA" else 1
                
                if nuevo_estado == "ENVIDO_ENVIDO":
                    puntos_acumulados_quiero = 4
                elif nuevo_estado == "REAL_ENVIDO":
                    # Si ya venía de un envido, se suman los puntos (2 + 3 = 5)
                    puntos_acumulados_quiero = puntos_acumulados_quiero + 3 if puntos_acumulados_quiero > 0 else 3
                elif nuevo_estado == "FALTA_ENVIDO":
                    puntos_acumulados_quiero = self.tanteador.calcular_puntos_restantes_al_partido()
                else:
                    puntos_acumulados_quiero = REGLAS_TANTO[nuevo_estado]["puntos_quiero"]
                
                # Cambiamos el estado del tablero y pasamos el turno al rival
                estado_actual = nuevo_estado
                turno = 2 if turno == 1 else 1

    def consultar_estrategia(self, jugador, estado_actual, opciones_validas):
        # Si el juego recién arranca, evalúa si quiere cantar
        if estado_actual == "NADA":
            if jugador.decidir_cantar_envido(): return "ENVIDO"
            if jugador.decidir_cantar_real_envido(): return "REAL_ENVIDO"
            if jugador.decidir_cantar_falta_envido(): return "FALTA_ENVIDO"
            return "PASO" # Si no quiere cantar nada, pasa el turno implícitamente
            
        # Si el rival cantó Envido
        if estado_actual == "ENVIDO":
            if jugador.decidir_re_envidar(): return "ENVIDO"
            if jugador.decidir_cantar_real_envido(): return "REAL_ENVIDO"
            if jugador.decidir_cantar_falta_envido(): return "FALTA_ENVIDO"
            if jugador.decidir_aceptar_envido(): return "QUIERO"
            if jugador.decidir_aceptar_re_envido(): return "QUIERO"
            if jugador.decidir_aceptar_real_envido(): return "QUIERO"
            if jugador.decidir_aceptar_falta_envido(): return "QUIERO"
            return "NO_QUIERO"
            
        # Si el rival cantó Real Envido
        if estado_actual == "REAL_ENVIDO":
            if jugador.decidir_cantar_falta_envido(): return "FALTA_ENVIDO"
            if jugador.decidir_aceptar_real_envido(): return "QUIERO"
            if jugador.decidir_aceptar_real_envido(): return "QUIERO"
            if jugador.decidir_aceptar_falta_envido(): return "QUIERO"
            return "NO_QUIERO"

        # Si el rival cantó Falta Envido
        if estado_actual == "FALTA_ENVIDO":
            if jugador.decidir_aceptar_falta_envido(): return "QUIERO"
            return "NO_QUIERO"  
            
        # Para cualquier otro estado por defecto
        return "QUIERO" if jugador.decidir_aceptar_envido() else "NO_QUIERO"


    def comparar_tantos(self, puntos_acumulados):
        global parda
        # Se obtiene el valor de envido de cada judada
        tanto_j1 = self.j1.calcular_envido()
        tanto_j2 = self.j2.calcular_envido()

        print(f"{self.j1.nombre} canta: {tanto_j1}")
        print(f"{self.j2.nombre} canta: {tanto_j2}")
        
        # Se comparan los valores obtenidos para saber el ganador.
        if tanto_j1 > tanto_j2:
            self.mostrar_ganador_envido(1, puntos_acumulados)
        elif tanto_j1 < tanto_j2:
            self.mostrar_ganador_envido(2, puntos_acumulados)        
        else:
            print(f"Parda en el envido, gana {self.j1.nombre} por ser mano")
            self.mostrar_ganador_envido(1, puntos_acumulados)  # En caso de parda, gana el que es mano (jugador 1)

    def nombre_jugador(self, id_jugador):
        return self.j1.nombre if id_jugador == 1 else self.j2.nombre
   
    def mostrar_ganador_envido(self, ganador, puntos_acumulados):
        print(f"Jugador {self.nombre_jugador(ganador)} gana el envido")
        print(f"Ganador: {ganador}")
        print(f"Puntos en juego: {puntos_acumulados}")
        print(f"Tantos ganador {self.nombre_jugador(ganador)} antes: {self.tanteador.puntos_jugador(ganador)}")
        self.tanteador.sumar_puntos(ganador, int(puntos_acumulados))        
        print(f"Tantos ganador {self.nombre_jugador(ganador)} despues: {self.tanteador.puntos_jugador(ganador)}")
        print(f"Tantos perdedor {self.nombre_jugador(2 if ganador == 1 else 1)}: {self.tanteador.puntos_jugador(2 if ganador == 1 else 1)}")

   
    
    def jugador_quiso(self, jugador, puntos_acumulados):
        self.canto_envido.aceptar()
        print(f"{self.nombre_jugador(jugador)} quiso")
        self.comparar_tantos(puntos_acumulados)
   