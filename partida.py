from estrategia_cartas import CartaMejor, CartaPeor, CartaRandom
from estrategia_truco import TrucoAgresivo, TrucoConservador, TrucoAdaptativo
from estrategia_envido import EnvidoAgresivo, EnvidoConservador, EnvidoAdaptativo
from estrategia_flor import FlorAdaptativa
from jugador import Jugador
from tanteador import Tanteador
from estado_partido import EstadoPartido
from mano import Mano

class Partida:
    def __init__(self):
        self.tanteador = Tanteador()
        self.estado = EstadoPartido(
                            self.tanteador.puntos_jugador(1),
                            self.tanteador.puntos_jugador(2)
                        )
        self.j1 = Jugador("Pedro", CartaMejor(), TrucoAdaptativo(), EnvidoAdaptativo(), FlorAdaptativa(), self.estado)
        self.j2 = Jugador("Mario", CartaMejor(), TrucoAdaptativo(), EnvidoAdaptativo(), FlorAdaptativa(), self.estado)

    def jugar_partida(self):
        mano = self.j1
        pie = self.j2

        while not self.tanteador.ganador():
            nueva_mano = Mano(mano, pie, self.tanteador)            
            nueva_mano.jugar_mano()            
            
            cambio_de_mano = mano
            mano = pie 
            pie = cambio_de_mano

        print("\nTanteador final: ")
        self.tanteador.mostrar(self.j1, self.j2)

        if self.tanteador.ganador():
            ganador = self.tanteador.ganador()
            print(f"Ganó {self.j1.nombre if ganador == 1 else self.j2.nombre} el partido")
