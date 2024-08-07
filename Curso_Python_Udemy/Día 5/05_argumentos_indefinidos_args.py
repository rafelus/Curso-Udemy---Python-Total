#Ejercicio 1
def suma_cuadrados(*args):
    total_suma= 0
    for arg in args:
        total_suma += (arg*arg)
    return total_suma
#Ejercicio 2
def suma_absolutos (*args):
    suma = 0
    for arg in args:
        if arg < 0:
            arg = arg*-1
            suma += arg
        else:
            suma += arg
    return suma
#Ejercicio 3
def numeros_persona (nombre, *args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg
    return f"{nombre}, la suma de tus números es {suma_numeros}"