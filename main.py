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

def jugar_carta_mano():
    global bazas_j1
    global bazas_j2
    global parda

    carta_j1 = j1.jugar_carta()
    carta_j2 = j2.jugar_carta()

    print(f"J1 juega: {carta_j1}")
    print(f"J2 juega: {carta_j2}")
    
    #Ver porque suma todos los puntos. Ordenar main.
    if valor_truco(carta_j1) > valor_truco(carta_j2):
        print("Gana J1 la baza")
        bazas_j1 += 1
        tanteador.sumar_puntos(1, canto_truco.puntos_en_juego())

    elif valor_truco(carta_j1) < valor_truco(carta_j2):
        print("Gana J2 la baza")
        bazas_j2 += 1
        tanteador.sumar_puntos(2, canto_truco.puntos_en_juego())
    
    else:
        parda = True
        print("Parda")

def jugar_envido():
    global bazas_j1
    global bazas_j2
    global parda

    tanto_j1 = j1.calcular_tanto()
    tanto_j2 = j2.calcular_tanto()

    print(f"J1 canta: {tanto_j1}")
    print(f"J2 juega: {tanto_j2}")
    
    #Ver porque suma todos los puntos. Ordenar main.
    if tanto_j1 > tanto_j2:
        print("Gana J1 la baza")
        bazas_j1 += 1
        tanteador.sumar_puntos(1, canto_envido.puntos_en_juego())

    elif tanto_j1 < tanto_j2:
        print("Gana J2 la baza")
        bazas_j2 += 1
        tanteador.sumar_puntos(2, canto_envido.puntos_en_juego())
    
    else:
        parda = True
        print("Parda, gana J1")
        bazas_j2 += 1
        tanteador.sumar_puntos(2, canto_envido.puntos_en_juego())

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

for ronda in range(3):
    print(f"\n--- Baza {ronda+ 1} ---")
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
    else:
        jugar_envido()


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
    else:
        jugar_carta_mano()

    print("\nResultado final:")
    print("Bazas J1:", bazas_j1)
    print("Bazas J2:", bazas_j2)

    calcular_ganador_bazas()
    
    tanteador.mostrar()

print("\nTanteador final: ")
tanteador.mostrar()

if tanteador.ganador():
    print("Ganó el jugador", tanteador.ganador())