#Ejercicio 1
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor*valor for valor in valores]
#Ejercicio 2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor % 2 == 0]
#Ejercicio 3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(valor-32)*(5/9) for valor in temperatura_fahrenheit]