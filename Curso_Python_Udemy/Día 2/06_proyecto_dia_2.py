#La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
#del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
#comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
#mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
#corresponde por las comisiones.

nombre = input("Como te llamas? ")
ventas = input("A cuanto ascienden tus ventas totales? ")

print(f"La comision de {nombre} es de {round(float(ventas)*0.13,2)} euros")