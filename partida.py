from estrategia_cartas import CartaMejor, CartaPeor, CartaRandom
from estrategia_truco import TrucoAgresivo, TrucoConservador, TrucoAdaptativo
from estrategia_envido import EnvidoAgresivo, EnvidoConservador, EnvidoAdaptativo
from estrategia_flor import FlorAdaptativa
from estrategia_cartas_humana import EstrategiaCartasHumana
from estrategia_envido_humana import EnvidoAdaptativoHumano
from estrategia_truco_humana import TrucoHumanoAdaptativo
from jugador import Jugador
from tanteador import Tanteador
from estado_partido import EstadoPartido
from mano import Mano
from interface import NuevoJuego

class Partida:
    def __init__(self):
        self.tanteador = Tanteador()
        self.estado = EstadoPartido(
                            self.tanteador.puntos_jugador(1),
                            self.tanteador.puntos_jugador(2)
                        )
        self.j2 = Jugador("Mario", CartaMejor(), TrucoAdaptativo(), EnvidoAdaptativo(), FlorAdaptativa(), self.estado)
        # self.j1 = Jugador("Pedro", CartaMejor(), TrucoAdaptativo(), EnvidoAdaptativo(), FlorAdaptativa(), self.estado)
        self.jugador = Jugador(None, EstrategiaCartasHumana(), TrucoHumanoAdaptativo(), EnvidoAdaptativoHumano(), None, self.estado)
        self.se_juega_con_flor = False

    def jugar_partida(self):
        pie = pie_tanteador = self.j2
        ronda = 1

        # nuevo_juego = NuevoJuego(self.estado)

        respuesta = ["S", "N"]

        print("---- Bienvenido a jugar al Truco (v 1.0) -----")
        self.jugador.nombre = input("Ingrese el nombre con que desea jugar: ")
        print("----------------------------------------------")
        print(f"---- Hola {self.jugador.nombre}: ")
        print("Jugamos con la reglas del Rio de la Plata, se puede jugar con o sin flor")
        print("y se puede reenvidar una vez.")
        flor_o_no = input("¿Jugamos con flor (S / N)? ").upper()
        while flor_o_no not in respuesta: 
            flor_o_no = input("¿Jugamos con flor (S / N)? ").upper()
            if flor_o_no == "S":
                self.se_juega_con_flor = True
        
        print(f"Perfecto {self.jugador.nombre}, jugamos con flor.") if self.se_juega_con_flor == True else print(f"Perfecto {self.jugador.nombre}, jugamos sin flor.")





        # self.humano = nuevo_juego.init_interface()

        print(f"{self.jugador.nombre}")
        print(f"{self.j2.nombre}")

        print(f"Perfecto {self.jugador.nombre} empecemos...")
        mano = mano_tanteador = self.jugador
        print(f"{self.jugador.nombre} sos mano...")

        while not self.tanteador.ganador():
            print(f"\n---------------------- Ronda Nº {ronda} -------------------------")
            print(f"Mano en esta ronda: {mano.nombre} (mano) vs {pie.nombre} (pie)")
            nueva_mano = Mano(mano, pie, self.tanteador, self.se_juega_con_flor)            
            nueva_mano.jugar_mano()            
            
            # cambio_de_mano = mano
            # mano = pie 
            # pie = cambio_de_mano
            ronda += 1

            print("\nResultado parcial:")
            self.tanteador.mostrar(mano_tanteador, pie_tanteador)

        print("\nTanteador final: ")
        self.tanteador.mostrar(mano_tanteador, pie_tanteador)

        ganador = self.tanteador.ganador()
        print(f"Ganó {self.jugador.nombre if ganador == 1 else self.j2.nombre} el partido")
