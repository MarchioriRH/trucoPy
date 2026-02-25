from mazo import Mazo
from estrategias import EstrategiaMejor, EstrategiaPeor, EstrategiaRandom
from jugador import Jugador
from reglas import valor_truco
from truco import CantoTruco

mazo = Mazo()
mazo.mezclar()

mano1 = mazo.repartir(3)
mano2 = mazo.repartir(3)

j1 = Jugador("Jugador 1", EstrategiaMejor())
j2 = Jugador("Jugador 2", EstrategiaRandom())

j1.recibir_cartas(mazo.repartir(3))
j2.recibir_cartas(mazo.repartir(3))

canto = CantoTruco()

bazas_j1 = 0
bazas_j2 = 0

for ronda in range(3):
    print(f"\n--- Baza {ronda+ 1} ---")

    if j1.estrategia.decidir_cantar_truco(j1.mano):
        canto.cantar(j1)
        print("Jugador 1 canta Truco")

        if not j2.estrategia.aceptar_truco(j2.mano, canto.nivel):
            canto.rechazar(j2)
            print("Jugador 2 no quiso")
            print("Jugador 1 gana", canto.puntos_por_rechazo())
            return
        else:
            canto.aceptar()
            print("Jugador 2 quiso")

    carta_j1 = j1.jugar_carta()
    carta_j2 = j2.jugar_carta()

    print(f"J1 juega: {carta_j1}")
    print(f"J2 juega: {carta_j2}")

    if valor_truco(carta_j1) > valor_truco(carta_j2):
        print("Gana J1 la baza")
        bazas_j1 += 1

    elif valor_truco(carta_j1) < valor_truco(carta_j2):
        print("Gana J2 la baza")
        bazas_j2 += 1
    
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