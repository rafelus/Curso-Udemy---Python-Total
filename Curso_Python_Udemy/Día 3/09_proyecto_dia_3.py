#   La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
#ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
#poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
#letras a su elección y a partir de ese momento nuestro código va a procesar esa información
#para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
#   1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
#recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
#que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
#debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
#y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
#encuentren absolutamente todas las letras es pasar, tanto el texto original como las
#letras a buscar, a minúsculas.
#   2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
#para lograr esta parte, recuerda que hay un método de string que permite transformarlo
#en una lista y que luego hay una función que permite averiguar el largo de una lista.
#   3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
#claramente echaremos mano de la indexación.
#   4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
#las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
#que permita unir esos elementos con espacios intermedios? Piénsalo.
#   5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
#texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
#puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
#manera de expresarle al usuario tu respuesta.


mi_frase_original = input("Ingresa un texto por consola: ")
tres_letras = list(input("Ahora introduce tres letras: "))

# 1- Contar caracteres
mi_frase = mi_frase_original.lower()
tres_letras = "".join(tres_letras).lower()
tres_letras = list(tres_letras)

sum1 = mi_frase.count(tres_letras[0])
sum2 = mi_frase.count(tres_letras[1])
sum3 = mi_frase.count(tres_letras[2])

print(f"La frase introducida contiene {sum1} veces el caracter '{tres_letras[0]}', {sum2} veces el caracter '{tres_letras[1]}' y {sum3} veces el caracter '{tres_letras[2]}'")

# 2- Contar palabras
mi_frase_original = mi_frase_original.split(" ")
print(f"La frase está formada por {len(mi_frase_original)} palabras")

# 3- Primera y última palabra
print(f"La primera palabra de la frase es '{mi_frase_original[0]}' y la última es '{mi_frase_original[-1]}'")

# 4- Invertir palabras
mi_frase_original= mi_frase_original[::-1]
print(" ".join(mi_frase_original))

# 5- Comprobar si existe la palabra "Python" en el texto
bool_var = "Python" in mi_frase_original
dic = {True: "si", False: "no"}
print(f"La palabra 'Python' {dic[bool_var]} se encuentra en el texto")