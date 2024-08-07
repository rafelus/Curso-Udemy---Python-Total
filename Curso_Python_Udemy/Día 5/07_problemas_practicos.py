#Ejercicio 1
"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""
def devolver_distintos(num1, num2, num3):
    suma_total = num1+num2+num3
    lista = [num1, num2, num3]
    num_max = 0
    num_min = 0
    nume_med = 0
    if suma_total > 15:
        num_max = max(lista)
        return num_max
    elif suma_total < 10:
        num_min = min(lista)
        return num_min
    elif suma_total >= 10 and suma_total <= 15:
        lista.remove(max(lista))
        lista.remove(min(lista))
        nume_med = max(lista)
        """
        lista.sort()        # Otra forma de hacerlo según el profesor,
        return lista[1]     # primero se ordena la lista con la funcion 'sort' y despúes se coge el indice [1]
        """
        return nume_med
print(devolver_distintos(3,6,4))

#Ejercicio 2
"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d','e','i','n','o','r','t']
"""
def analizador_palabras (palabra_inicial):
    palabra_inicial = sorted(set(palabra_inicial))
    return palabra_inicial
print(analizador_palabras("entretenido"))
print(analizador_palabras("cascarrabias"))

#Ejercicio 3
"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""
def ceros_consecutivos(*args):
    contador = 0
    for arg in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False
print(ceros_consecutivos(5,6,7,8,8,0,0,5))
print(ceros_consecutivos(6,0,5,1,0,0,0,1))
print(ceros_consecutivos(0,0,5,1,3,0,6,6))

#Ejercicio 4
"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""
def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)
print(contar_primos(50))