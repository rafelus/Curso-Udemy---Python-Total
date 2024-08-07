#Ejemplo
from os import system
nombre = input("Dime tu nombre: ")
system("cls")
edad = input("Dime tu edad: ")
system("cls")

print(f"Tu nombre es {nombre} y tienes {edad} años")

"""Para que no aparezca el rectángulo tachado cuando se ejecuta el programa
hay que activar primero la opción 'Emulate terminal in output console' y crear un RUNMODE
para éste archivo que tenga esa opción"""