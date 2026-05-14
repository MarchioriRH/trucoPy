from mazo import Mazo
from estrategia_cartas import CartaMejor, CartaPeor, CartaRandom
from estrategia_truco import TrucoAgresivo, TrucoConservador, TrucoAdaptativo
from estrategia_envido import EnvidoAgresivo, EnvidoConservador, EnvidoAdaptativo
from jugador import Jugador
from reglas import valor_truco
from reglas import valor_envido
from truco import CantoTruco
from envido import CantoEnvido
from tanteador import Tanteador
from estado_partido import EstadoPartido
from partes_juego import JugarTruco

se_canto_truco = False
se_canto_envido = False
no_quiero_truco = False
no_quiero_envido = False
j1_canto_flor = False
j2_canto_flor = False
j1_hizo_primera = False
j2_hizo_primera = False
hay_flor = False
parda = False
ganador_flor = None

mazo = Mazo()
mazo.mezclar()

tanteador = Tanteador()
juego = JugarTruco()


mano1 = mazo.repartir(3)
mano2 = mazo.repartir(3)

estado = EstadoPartido(
    tanteador.puntos_jugador(1),
    tanteador.puntos_jugador(2)
)

j1 = Jugador("Jugador 1", CartaMejor(), TrucoAdaptativo(), EnvidoAdaptativo(), estado)
j2 = Jugador("Jugador 2", CartaMejor(), TrucoAdaptativo(), EnvidoAdaptativo(), estado)

j1.recibir_cartas(mazo.repartir(3))
j2.recibir_cartas(mazo.repartir(3))

canto_truco = CantoTruco()
canto_envido = CantoEnvido()


print(f"Mano J1: {j1.mano}")
print(f"Mano J2: {j2.mano}")

def jugar_carta_mano():
    
    global parda

    carta1_j1 = j1.jugar_carta()
    print(f"J1 juega carta 1: {carta1_j1}")
    
    carta1_j2 = j2.analizar_jugada(carta1_j1) 
    resultado_comparacion = juego.comparar_cartas(carta1_j1, carta1_j2)
    if resultado_comparacion == 2:
        juego.jugador2_hace_primera(j1, j2, carta1_j1, carta1_j2, tanteador, canto_truco)
       
               
    elif resultado_comparacion == 1:
        juego.jugador1_hace_primera(j1, j2, carta1_j1, carta1_j2, tanteador, canto_truco)
        
    elif resultado_comparacion == 0:
        parda = True
        print("Parda")
        carta2_j1 = j1.jugar_carta()
        carta2_j2 = j2.jugar_carta()
        resultado_comparacion = juego.comparar_cartas(carta2_j1, carta2_j2)
        if resultado_comparacion == 1:
            print(f"J1 juega carta 2: {carta2_j1} mata a {carta2_j2}")
            print("Gana J1 la baza")
            tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())
        elif resultado_comparacion == 2:
            print(f"J2 juega carta 2: {carta2_j2} mata a {carta2_j1}")
            print("Gana J2 la baza")
            tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
        elif resultado_comparacion == 0:
            print("2da Parda")
            carta3_j1 = j1.jugar_carta()
            carta3_j2 = j2.jugar_carta()
            resultado_comparacion = juego.comparar_cartas(carta3_j1, carta3_j2)
            if resultado_comparacion == 1:
                print(f"J1 juega carta 3: {carta3_j1} mata a {carta3_j2}")
                print("Gana J1 la baza")
                tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())
            elif resultado_comparacion == 2:
                print(f"J2 juega carta 3: {carta3_j2} mata a {carta3_j1}")
                print("Gana J2 la baza")
                tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
            else:    
                print("3era parda, nadie gana la baza")
    

ganador_flor = juego.verificar_flor(j1, j2, canto_envido, tanteador)

if ganador_flor > 0:
    print("Ningún jugador tiene flor, se procede con el envido")
   
    if not se_canto_envido: 
        
        if j1.decidir_cantar_envido():
            canto_envido.cantar(j1)
            print("Jugador 1 canta Envido")
            se_canto_envido = True
            
            if not j2.aceptar_envido(j2.mano):
                no_quiero_envido = True
                canto_envido.rechazar(j2)
                print("Jugador 2 no quiso")
                print("Jugador 1 gana", canto_envido.puntos_por_rechazo())
                tanteador.sumar_puntos(1, canto_envido.puntos_por_rechazo())
                
            else:
                canto_envido.aceptar()
                print("Jugador 2 quiso")
                juego.jugar_envido(j1, j2, canto_envido, tanteador)

        elif j2.decidir_cantar_envido():
            canto_envido.cantar(j2)
            print("Jugador 2 canta Envido")
            se_canto_envido = True

            if not j1.aceptar_envido(j1.mano):
                no_quiero_envido = True
                canto_envido.rechazar(j1)
                print("Jugador 1 no quiso")
                print("Jugador 2 gana", canto_envido.puntos_por_rechazo())
                tanteador.sumar_puntos(2, canto_envido.puntos_por_rechazo())
                
            else:
                canto_envido.aceptar()
                print("Jugador 1 quiso")
                juego.jugar_envido(j1, j2, canto_envido, tanteador)
        
        hay_flor = True
        if no_quiero_envido:
            print("No se quiso el envido, se procede al truco")
        if not se_canto_envido:
            print("No se canto el envido, se procede al truco")
            se_canto_envido = True

if not se_canto_truco:
    if j1.decidir_cantar_truco():
        canto_truco.cantar(j1)
        print("Jugador 1 canta Truco")
        se_canto_truco = True

        if not j2.aceptar_truco(j2.mano):
            no_quiero_truco = True
            canto_truco.rechazar(j2)
            print("Jugador 2 no quiso")
            print("Jugador 1 gana", canto_truco.puntos_por_rechazo())
            tanteador.sumar_puntos(1, canto_truco.puntos_por_rechazo())
            
        else:
            canto_truco.aceptar()
            print("Jugador 2 quiso")

    elif j2.decidir_cantar_truco():
        canto_truco.cantar(j2)
        print("Jugador 2 canta Truco")
        se_canto_truco = True

        if not j1.aceptar_truco(j1.mano):
            no_quiero_truco = True
            canto_truco.rechazar(j1)
            print("Jugador 1 no quiso")
            print("Jugador 2 gana", canto_truco.puntos_por_rechazo())
            tanteador.sumar_puntos(2, canto_truco.puntos_por_rechazo())
           
        else:
            canto_truco.aceptar()
            print("Jugador 1 quiso")

    if not no_quiero_truco:
        jugar_carta_mano()
    else:
        print("No se quiso el truco, se procede a mostrar el tanteador")

if ganador_flor == 1:
    print(f"Flor J1: {j1.mano}")
elif ganador_flor == 2:
    print(f"Flor J2: {j2.mano}")

print("\nResultado final:")

tanteador.mostrar()

print("\nTanteador final: ")
tanteador.mostrar()

if tanteador.ganador():
    print("Ganó el jugador", tanteador.ganador())