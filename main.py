from mazo import Mazo
from estrategia_cartas import CartaMejor, CartaPeor, CartaRandom
from estrategia_truco import TrucoAgresivo, TrucoConservador, TrucoAdaptativo
from jugador import Jugador
from reglas import valor_truco
from truco import CantoTruco
from tanteador import Tanteador
from estado_partido import EstadoPartido

se_canto_truco = False
no_quiero_truco = False

mazo = Mazo()
mazo.mezclar()

tanteador = Tanteador()


mano1 = mazo.repartir(3)
mano2 = mazo.repartir(3)

estado = EstadoPartido(
    tanteador.puntos_jugador(1),
    tanteador.puntos_jugador(2)
)

j1 = Jugador("Jugador 1", CartaMejor(), TrucoAdaptativo(), estado)
j2 = Jugador("Jugador 2", CartaMejor(), TrucoAdaptativo(), estado)

j1.recibir_cartas(mazo.repartir(3))
j2.recibir_cartas(mazo.repartir(3))

canto = CantoTruco()

bazas_j1 = 0
bazas_j2 = 0


for ronda in range(3):
    print(f"\n--- Baza {ronda+ 1} ---")

    if not se_canto_truco:
        if j1.decidir_cantar_truco():
            canto.cantar(j1)
            print("Jugador 1 canta Truco")
            se_canto_truco = True

            if not j2.aceptar_truco(j2.mano):
                no_quiero_truco = True
                canto.rechazar(j2)
                print("Jugador 2 no quiso")
                print("Jugador 1 gana", canto.puntos_por_rechazo())
                tanteador.sumar_puntos(1, canto.puntos_por_rechazo())
                # return
            else:
                canto.aceptar()
                print("Jugador 2 quiso")

        if j2.decidir_cantar_truco():
            canto.cantar(j2)
            print("Jugador 2 canta Truco")
            se_canto_truco = True

            if not j1.aceptar_truco(j1.mano):
                no_quiero_truco = True
                canto.rechazar(j1)
                print("Jugador 1 no quiso")
                print("Jugador 2 gana", canto.puntos_por_rechazo())
                tanteador.sumar_puntos(2, canto.puntos_por_rechazo())
                # return
            else:
                canto.aceptar()
                print("Jugador 1 quiso")

        carta_j1 = j1.jugar_carta()
        carta_j2 = j2.jugar_carta()

        print(f"J1 juega: {carta_j1}")
        print(f"J2 juega: {carta_j2}")
       
        if valor_truco(carta_j1) > valor_truco(carta_j2):
            print("Gana J1 la baza")
            bazas_j1 += 1
            tanteador.sumar_puntos(1, canto.puntos_en_juego())

        elif valor_truco(carta_j1) < valor_truco(carta_j2):
            print("Gana J2 la baza")
            bazas_j2 += 1
            tanteador.sumar_puntos(2, canto.puntos_en_juego())
        
        else:
            print("Parda")
            

    print("\nResultado final:")
    print("Bazas J1:", bazas_j1)
    print("Bazas J2:", bazas_j2)

    if bazas_j1 > bazas_j2:
        print("J1 gana la mano")
    elif bazas_j2 > bazas_j1:
        print("J2 gana la mano")
    else:
        print("Empate en la mano")
    
    tanteador.mostrar()

print("\nTanteador final: ")
tanteador.mostrar()

if tanteador.ganador():
    print("Ganó el jugador", tanteador.ganador())