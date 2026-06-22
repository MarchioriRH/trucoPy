from jugador import Jugador
from estado_partido import EstadoPartido

class NuevoJuego:
    def __init__(self, estado):
        self.jugador = Jugador()
        self.estado = estado
        self.se_juega_con_flor = False
        pass

    def init_interface(self):
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


                