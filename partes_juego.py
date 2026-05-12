class JugarTruco:
    def jugar_envido():
        global bazas_j1
        global bazas_j2
        global parda

        tanto_j1 = j1.calcular_envido()
        tanto_j2 = j2.calcular_envido()

        print(f"J1 canta: {tanto_j1}")
        print(f"J2 canta: {tanto_j2}")
        
        #Ver porque suma todos los puntos. Ordenar main.
        if tanto_j1 > tanto_j2:
            print("Gana J1 el envido")
            bazas_j1 += 1
            tanteador.sumar_puntos(1, canto_envido.puntos_en_juego())

        elif tanto_j1 < tanto_j2:
            print("Gana J2 el envido")
            bazas_j2 += 1
            tanteador.sumar_puntos(2, canto_envido.puntos_en_juego())
        
        else:
            print("Parda, gana J1")
            bazas_j1 += 1
            tanteador.sumar_puntos(1, canto_envido.puntos_en_juego())

    def verificar_flor(self, j1, j2):    
        global bazas_j1
        global bazas_j2
        global parda
        global j1_canto_flor
        global j2_canto_flor
        global hay_flor

        flor_j1 = j1.verificar_flor()
        flor_j2 = j2.verificar_flor()

        if flor_j1 and not flor_j2:
            print("J1 canta flor")
            bazas_j1 += 1
            j1_canto_flor = True
            tanteador.sumar_puntos(1, canto_envido.puntos_flor())
            hay_flor = True
        elif flor_j2 and not flor_j1:
            print("J2 canta flor")
            bazas_j2 += 1
            j2_canto_flor = True
            tanteador.sumar_puntos(2, canto_envido.puntos_flor())
            hay_flor = True
        elif flor_j1 and flor_j2:
            print("Ambos tienen flor, se comparan los tantos")
            j1_canto_flor = True
            j2_canto_flor = True
            comparacion_flor_j1 = j1.calcular_envido()
            comparacion_flor_j2 = j2.calcular_envido()
            if comparacion_flor_j1 > comparacion_flor_j2:
                print("J1 gana la flor")
                bazas_j1 += 1
                tanteador.sumar_puntos(1, canto_envido.puntos_flor())
            elif comparacion_flor_j2 > comparacion_flor_j1:
                print("J2 gana la flor")
                bazas_j2 += 1
                tanteador.sumar_puntos(2, canto_envido.puntos_flor())
            else:
                print("Empate en la flor, gana J1")
                bazas_j1 += 1
                tanteador.sumar_puntos(1, canto_envido.puntos_flor())
            hay_flor = True 
        # return hay_flor