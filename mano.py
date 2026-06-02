from jugador import Jugador
from canto_truco import CantoTruco
from truco import JuegoTruco
from canto_envido import CantoEnvido
from envido import JuegoEnvido
from flor import JuegoFlor
from canto_flor import CantoFlor
from mazo import Mazo

class Mano:
    def __init__(self, j1, j2, tanteador):
        self.j1 = j1
        self.j2 = j2
        self.tanteador = tanteador

        self.canto_truco = CantoTruco()
        self.canto_envido = CantoEnvido()
        self.canto_flor = CantoFlor()

        self.juego_flor = JuegoFlor(self.j1, self.j2, self.canto_flor, self.tanteador)
        self.juego_truco = JuegoTruco(self.j1, self.j2, self.canto_truco, self.tanteador)
        self.juego_envido = JuegoEnvido(self.j1, self.j2, self.canto_envido, self.tanteador)



    def jugar_mano(self):
        se_canto_truco = False
        se_canto_envido = False
        ganador_flor = -1
        flor_ganadora = []

        mazo = Mazo()
        mazo.mezclar()

        self.j1.recibir_cartas(mazo.repartir(3))
        self.j2.recibir_cartas(mazo.repartir(3))

        print(f"\nMano: {self.j1.mano}")
        print(f"Pie: {self.j2.mano}")

        flor_ganadora, ganador_flor = self.juego_flor.jugar_flor()

        if ganador_flor < 0:
            print("Se procede con el envido")
        
            if not se_canto_envido: 
                self.juego_envido.jugar_envido()        

        if not se_canto_truco:
            self.juego_truco.jugar_truco()
            
        if flor_ganadora != []:
            print(f"Flor ganadora Jugador {ganador_flor}: {flor_ganadora}")

        print("\nResultado parcial:")

        self.tanteador.mostrar()

    