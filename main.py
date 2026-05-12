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

se_canto_truco = False
se_canto_envido = False
no_quiero_truco = False
no_quiero_envido = False
j1_canto_flor = False
j2_canto_flor = False
hay_flor = False
parda = False

mazo = Mazo()
mazo.mezclar()

tanteador = Tanteador()


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

bazas_j1 = 0
bazas_j2 = 0

print(f"Mano J1: {j1.mano}")
print(f"Mano J2: {j2.mano}")

def jugar_carta_mano():
    global bazas_j1
    global bazas_j2
    global parda

    carta1_j1 = j1.jugar_carta()
    print(f"J1 juega: {carta1_j1}")
    
    carta1_j2 = j2.analizar_jugada(carta1_j1) 
    # carta1_j2 mata a carta1_j1
    if valor_truco(carta1_j2) > valor_truco(carta1_j1):
        print(f"J2 juega: {carta1_j2} mata a {carta1_j1}")
        carta2_j2 = j2.jugar_carta()
        # Juega la segunda carta
        print("J2 juega: ", carta2_j2)

        # J1 analiza la carta jugada por J2 y elige la carta a jugar
        carta2_j1 = j1.analizar_jugada(carta2_j2)
        # Si la carta de J1 mata a la carta de J2
        if valor_truco(carta2_j1) > valor_truco(carta2_j2):
            print(f"J1 juega: {carta2_j1} mata a {carta2_j2}")
            # J1 juega la tercera carta
            carta3_j1 = j1.jugar_carta()
            print("J1 juega: ", carta3_j1)

            # J2 analiza la carta jugada por J1 y elige la carta a jugar
            carta3_j2 = j2.analizar_jugada(carta3_j1)
            # Si la carta de J2 mata a la carta de J1
            if valor_truco(carta3_j2) > valor_truco(carta3_j1):
                print(f"J2 juega: {carta3_j2} mata a {carta3_j1}")
                # J2 gana la baza
                print("Gana J2 la baza")
                bazas_j1 += 1
                tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
            else:
                # J2 no mata a la carta de J1, gana J1 la baza
                print(f"J2 no mata a {carta3_j1}")
                print("Gana J1 la baza")
                bazas_j1 += 1
                tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())
        else:
            # J1 no mata a la carta de J2, gana J2 la baza
            print(f"J1 no mata a {carta2_j2}")
            print("Gana J2 la baza")
            bazas_j2 += 1
            tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
               
    elif valor_truco(carta1_j1) > valor_truco(carta1_j2):
        #carta1_j2 = j2.jugar_carta()
        print(f"J2 juega: {carta1_j2} no mata a {carta1_j1}")

        carta2_j1 = j1.analizar_jugada(carta1_j2)
        print(f"J1 juega: {carta2_j1}")

        carta2_j2 = j2.analizar_jugada(carta2_j1)
        if valor_truco(carta2_j2) > valor_truco(carta2_j1):
            print(f"J2 juega: {carta2_j2} mata a {carta2_j1}")
            carta3_j2 = j2.jugar_carta()
            print(f"J2 juega: {carta3_j2}")

            carta3_j1 = j1.jugar_carta()
            if valor_truco(carta3_j2) < valor_truco(carta3_j1):
                print(f"J2 juega: {carta3_j2} mata a {carta2_j1}")
                print("Gana J2 la baza")
                bazas_j2 += 1
                tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
            else:
                print(f"J2 no mata a {carta2_j1}")
                print("Gana J1 la baza")
                bazas_j1 += 1
                tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())



    
    elif valor_truco(carta1_j1) == valor_truco(carta1_j2):
        parda = True
        print("Parda")
        carta2_j1 = j1.jugar_carta()
        carta2_j2 = j2.jugar_carta()
        if valor_truco(carta2_j1) > valor_truco(carta2_j2):
            print(f"J1 juega: {carta2_j1} mata a {carta2_j2}")
            print("Gana J1 la baza")
            bazas_j1 += 1
            tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())
        elif valor_truco(carta2_j2) > valor_truco(carta2_j1):
            print(f"J2 juega: {carta2_j2} mata a {carta2_j1}")
            print("Gana J2 la baza")
            bazas_j2 += 1
            tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
        elif valor_truco(carta1_j1) == valor_truco(carta1_j2):
            print("2da Parda")
            carta3_j1 = j1.jugar_carta()
            carta3_j2 = j2.jugar_carta()
            if valor_truco(carta3_j1) > valor_truco(carta3_j2):
                print(f"J1 juega: {carta3_j1} mata a {carta3_j2}")
                print("Gana J1 la baza")
                bazas_j1 += 1
                tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())
            elif valor_truco(carta3_j2) > valor_truco(carta3_j1):
                print(f"J2 juega: {carta3_j2} mata a {carta3_j1}")
                print("Gana J2 la baza")
                bazas_j2 += 1
                tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
            else:    
                print("3era parda, nadie gana la baza")

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

def calcular_ganador_bazas():
    global bazas_j1, bazas_j2
    global parda
    if not parda:
        if bazas_j1 > bazas_j2:
            print("J1 gana la mano")
        elif bazas_j2 > bazas_j1:
            print("J2 gana la mano")
        else:
            print("Empate en la mano")
    else: 
        parda = False

def verificar_flor():    
    global bazas_j1
    global bazas_j2
    global parda

    flor_j1 = j1.verificar_flor()
    flor_j2 = j2.verificar_flor()

    if flor_j1 and not flor_j2:
        print("J1 tiene flor, gana la mano")
        bazas_j1 += 1
        j1_canto_flor = True
        tanteador.sumar_puntos(1, canto_envido.puntos_flor())
        hay_flor = True
    elif flor_j2 and not flor_j1:
        print("J2 tiene flor, gana la mano")
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
       

# for ronda in range(3):
# print(f"\n--- Baza {ronda+ 1} ---")
    
verificar_flor()

if not hay_flor:
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
                # return
            else:
                canto_envido.aceptar()
                print("Jugador 2 quiso")
                jugar_envido()

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
                # return
            else:
                canto_envido.aceptar()
                print("Jugador 1 quiso")
                jugar_envido()
        # se_canto_envido = True
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
            # return
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
            # return
        else:
            canto_truco.aceptar()
            print("Jugador 1 quiso")

    jugar_carta_mano()


if j1_canto_flor:
    print(f"Flor J1: {j1.mano}")
if j2_canto_flor:
    print(f"Flor J2: {j2.mano}")
if j1_canto_flor and j2_canto_flor: 
    print(f"Flor J1: {j1.mano}")
    print(f"Flor J2: {j2.mano}")

print("\nResultado final:")
print("Bazas J1:", bazas_j1)
print("Bazas J2:", bazas_j2)

calcular_ganador_bazas()

tanteador.mostrar()

print("\nTanteador final: ")
tanteador.mostrar()

if tanteador.ganador():
    print("Ganó el jugador", tanteador.ganador())