from mazo import Mazo
from estrategia_cartas import CartaMejor, CartaPeor, CartaRandom
from estrategia_truco import TrucoAgresivo, TrucoConservador, TrucoAdaptativo
from estrategia_envido import EnvidoAgresivo, EnvidoConservador, EnvidoAdaptativo
from jugador import Jugador
from reglas import valor_truco
from truco import CantoTruco, JuegoTruco
from envido import CantoEnvido
from envido import JuegoEnvido
from tanteador import Tanteador
from estado_partido import EstadoPartido
# from partes_juego import JugarTruco
from flor import JuegoFlor

from carta import Carta

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
ganador_flor = -1

canto_truco = CantoTruco()
canto_envido = CantoEnvido()
tanteador = Tanteador()

estado = EstadoPartido(
    tanteador.puntos_jugador(1),
    tanteador.puntos_jugador(2)
)

j1 = Jugador("Jugador 1", CartaMejor(), TrucoAdaptativo(), EnvidoAdaptativo(), estado)
j2 = Jugador("Jugador 2", CartaMejor(), TrucoAdaptativo(), EnvidoAdaptativo(), estado)

juego_truco = JuegoTruco(j1, j2, canto_truco, tanteador)
juego_flor = JuegoFlor(j1, j2, canto_envido, tanteador)
juego_envido = JuegoEnvido(j1, j2, canto_envido, tanteador)



# cartas_j1 = [Carta(1, "Espada"), Carta(4, "Espada"), Carta(11, "Espada")]
# cartas_j2 = [Carta(10, "Oro"), Carta(3, "Basto"), Carta(5, "Basto")]

# j1.mano = cartas_j1
# j2.mano = cartas_j2
while not tanteador.ganador():
    flor_ganadora_1 = []
    flor_ganadora_2 = []
    mazo = Mazo()
    mazo.mezclar()
    j1.recibir_cartas(mazo.repartir(3))
    j2.recibir_cartas(mazo.repartir(3))


    print(f"\nMano J1: {j1.mano}")
    print(f"Mano J2: {j2.mano}")

    ganador_flor = juego_flor.verificar_flor()
    if ganador_flor == 1:
        flor_ganadora_1 = j1.mano[:]
    elif ganador_flor == 2:
        flor_ganadora_2 = j2.mano[:]

    if ganador_flor < 0:
        print("Ningún jugador tiene flor, se procede con el envido")
    
        if not se_canto_envido: 
            juego_envido.jugar_envido()        

    if not se_canto_truco:
        juego_truco.jugar_truco()
        
    if flor_ganadora_1 != []:
        print(f"Flor ganadora Jugador 1: {flor_ganadora_1}")
    if flor_ganadora_2 != []:
        print(f"Flor ganadora Jugador 2: {flor_ganadora_2}")    

    print("\nResultado parcial:")

    tanteador.mostrar()

print("\nTanteador final: ")
tanteador.mostrar()

if tanteador.ganador():
    print("Ganó el jugador", tanteador.ganador())