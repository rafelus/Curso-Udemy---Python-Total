def generador_turno_perfumeria():
    turno = 0
    while True:
        turno += 1
        yield f"****    P - {turno}     ****\n"


def generador_turno_farmacia():
    turno = 0
    while True:
        turno += 1
        yield f"****    F - {turno}     ****\n"


def generador_turno_cosmetica():
    turno = 0
    while True:
        turno += 1
        yield f"****    C - {turno}     ****\n"


turno_perfumeria = generador_turno_perfumeria()
turno_farmacia = generador_turno_farmacia()
turno_cosmetica = generador_turno_cosmetica()


def decorador_ticket(opcion):
    print("*********************")
    print("**** Su turno es ****\n")
    match opcion:
        case 1:
            print(next(turno_perfumeria))
        case 2:
            print(next(turno_farmacia))
        case 3:
            print(next(turno_cosmetica))
    print("Espere a ser atendido")
    print("****** Gracias ******")
    print("*********************")