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

REGLAS_TANTO = {
    "NADA": {
        "opciones": ["ENVIDO", "REAL_ENVIDO", "FALTA_ENVIDO"],
        "puntos_quiero": 0, "puntos_no_quiero": 0
    },
    "ENVIDO": {
        "opciones": ["QUIERO", "NO_QUIERO", "ENVIDO", "REAL_ENVIDO", "FALTA_ENVIDO"],
        "puntos_quiero": 2, "puntos_no_quiero": 1
    },
    "ENVIDO_ENVIDO": {
        "opciones": ["QUIERO", "NO_QUIERO", "REAL_ENVIDO", "FALTA_ENVIDO"],
        "puntos_quiero": 4, "puntos_no_quiero": 2
    },
    "REAL_ENVIDO": {
        "opciones": ["QUIERO", "NO_QUIERO", "FALTA_ENVIDO"],
        "puntos_quiero": 3, "puntos_no_quiero": 1  # Nota: estos puntos se suman si viene de un envido previo
    },
    "FALTA_ENVIDO": {
        "opciones": ["QUIERO", "NO_QUIERO"],
        "puntos_quiero": "FALTA", "puntos_no_quiero": 1
    }
}

REGLAS_TRUCO = {
    "NADA": {
        "opciones": ["QUIERO", "NO QUIERO", "TRUCO", "RETRUCO", "VALE_CUATRO"],
        "puntos_quiero": 0, "puntos_no_quiero": 0
    },
    "TRUCO": {
        "opciones": ["QUIERO", "NO QUIERO", "RETRUCO", "VALE_CUATRO"],
        "puntos_quiero": 2, "puntos_no_quiero": 1
    },
    "RETRUCO": {
        "opciones": ["QUIERO", "NO QUIERO", "VALE_CUATRO"],
        "puntos_quiero": 3, "puntos_no_quiero": 2
    },
    "VALE_CUATRO": {
        "opciones": ["QUIERO", "NO QUIERO"],
        "puntos_quiero": 4, "puntos_no_quiero": 3
    }
}





   
