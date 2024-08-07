#Ejercicio 1
def mi_generador():
    infinito = 0
    while True:
        infinito += 1
        yield infinito


generador = mi_generador()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#Ejercicio 2
def mi_generador():
    infinito = 0
    while True:
        infinito += 7
        yield infinito


g = mi_generador()

#Ejercicio 3
def vidas_restantes():
    vidas = 3
    yield "Te quedan 3 vidas"

    vidas -= 1
    yield "Te quedan 2 vidas"

    vidas -= 1
    yield "Te queda 1 vida"

    vidas -= 1
    yield "Game Over"


perder_vida = vidas_restantes()