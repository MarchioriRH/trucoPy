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
        mano = mano_tanteador = self.j1
        pie = pie_tanteador = self.j2
        ronda = 1

        while not self.tanteador.ganador():
            print(f"\n---------------------- Ronda Nº {ronda} -------------------------")
            print(f"Mano en esta ronda: {mano.nombre} (mano) vs {pie.nombre} (pie)")
            nueva_mano = Mano(mano, pie, self.tanteador)            
            nueva_mano.jugar_mano()            
            
            cambio_de_mano = mano
            mano = pie 
            pie = cambio_de_mano
            ronda += 1

            print("\nResultado parcial:")
            self.tanteador.mostrar(mano_tanteador, pie_tanteador)

        print("\nTanteador final: ")
        self.tanteador.mostrar(mano_tanteador, pie_tanteador)

        ganador = self.tanteador.ganador()
        print(f"Ganó {self.j1.nombre if ganador == 1 else self.j2.nombre} el partido")
