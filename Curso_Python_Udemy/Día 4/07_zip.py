#Ejercicio 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
conjunto = list(zip(paises,capitales))
for pais,capital in conjunto:
    print(f"La capital de {pais} es {capital}")
#Ejercicio 2
marcas = ["Levis","Adidas","Philips"]
productos =["vaqueros","zapatillas","televisiones"]
mi_zip = zip(marcas,productos)
#Ejercicio 3
español = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince"]
portugués = ["um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze"]
inglés = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirdteen","fourteen","fiveteen"]
numeros = list(zip(español,portugués,inglés))