from jugador import Jugador
from truco import CantoTruco, JuegoTruco
from envido import CantoEnvido, JuegoEnvido
from flor import JuegoFlor
from mazo import Mazo


class Mano:
    def __init__(self, j1, j2, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.tanteador = tanteador

        self.canto_truco = CantoTruco()
        self.canto_envido = CantoEnvido()

    def jugar_mano(self):
        se_canto_truco = False
        se_canto_envido = False
        ganador_flor = -1

        juego_truco = JuegoTruco(self.j1, self.j2, self.canto_truco, self.tanteador)
        juego_flor = JuegoFlor(self.j1, self.j2, self.canto_envido, self.tanteador)
        juego_envido = JuegoEnvido(self.j1, self.j2, self.canto_envido, self.tanteador)

        flor_ganadora_1 = []
        flor_ganadora_2 = []
        mazo = Mazo()
        mazo.mezclar()
        self.j1.recibir_cartas(mazo.repartir(3))
        self.j2.recibir_cartas(mazo.repartir(3))


        print(f"\nMano: {self.j1.mano}")
        print(f"Pie: {self.j2.mano}")

        ganador_flor = juego_flor.verificar_flor()
        if ganador_flor == 1:
            flor_ganadora_1 = self.j1.mano[:]
        elif ganador_flor == 2:
            flor_ganadora_2 = self.j2.mano[:]

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

        self.tanteador.mostrar()

    