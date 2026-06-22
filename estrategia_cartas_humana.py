class EstrategiaCartasHumana():
    def __init__(self):
        self.respuesta = ["S", "N"]
    
    def elegir_carta(self, mano):

        print("\nTus cartas:")

        for i, carta in enumerate(mano):
            print(f"{i+1}. {carta}")

        opcion = int(input("Elegí una carta: "))

        return mano[i-1]

    