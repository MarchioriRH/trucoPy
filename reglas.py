def valor_truco(carta):

    especiales = {
        (1, "Espada"):14,
        (1, "Basto"):13,
        (7, "Espada"):12,
        (7, "Oro"):11,
    }

    if (carta.numero, carta.palo) in especiales:
        return especiales[(carta.numero, carta.palo)]

    if carta.numero == 3:
        return 10
    if carta.numero == 2:
        return 9
    if carta.numero == 1:
        return 8
    if carta.numero == 12:
        return 7
    if carta.numero == 11:
        return 6
    if carta.numero == 10:
        return 5
    if carta.numero == 7:
        return 4
    if carta.numero == 6:
        return 3 
    if carta.numero == 5:
        return 2
    if carta.numero == 4:
        return 1
