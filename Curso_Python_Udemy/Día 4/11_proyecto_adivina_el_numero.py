'''La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.
Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos. '''
from random import *

player_name = input("Cuál es tu nombre: ")
print(f"Hola {player_name}, he pensado un número del 1 al 100 y tienes ocho intentos para adivinarlo, cuál crees que puede ser?")
print("")
secret_number = randint(1,101)
answer = 0
attempts = 0
opportunities = 8

while answer != secret_number and opportunities > 0:
    print(f"Te quedan {opportunities} intentos, elige bien!")
    print("")
    answer = int(input("Que número elige? "))
    if answer > 100 or answer < 1:
        print("Tienes que elegir un número entre 1 y 100")
    elif answer > secret_number:
        print("Te has pasado! el número secreto esta por debajo")
    elif answer < secret_number:
        print("El número secreto es mayor")
    else:
        print(f"Enhorabuena!!! Has adivinado el número secreto en {attempts} intentos")
    print("")
    attempts += 1
    opportunities -= 1

if answer != secret_number:
    print(f"Lo siento has agotado todos los intentos, el número secreto era el {secret_number}\nMás suerte la próxima vez.")