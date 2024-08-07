"""
Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos:
nombre y apellido. Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a
heredar de Persona, porque los clientes son personas, por lo que el Cliente va a heredar
entonces los atributos de Persona, pero también va a tener atributos propios, como número
de cuenta y balance, es decir, el saldo que tiene en su cuenta bancaria.
Pero eso no es todo: Cliente también va a tener tres métodos. El primero va a ser uno de los
métodos especiales y es el que permite que podamos imprimir a nuestro cliente. Este método
va a permitir que cuando el código pida imprimir Cliente, se muestren todos sus datos,
incluyendo el balance de su cuenta. Luego, un método llamado Depositar, que le va a permitir
decidir cuánto dinero quiere agregar a su cuenta. Y finalmente, un tercer método llamado
Retirar, que le permita decidir cuánto dinero quiere sacar de su cuenta.
Una vez que hayas creado estas dos clases, tienes que crear el código para que tu programa se
desarrolle, pidiéndole al usuario que elija si quiere hacer depósitos o retiros. El usuario puede
hacer tantas operaciones como quiera hasta que decida salir del programa. Por lo tanto, nuestro
código tiene que ir llevando la cuenta de cuánto dinero hay en el balance, y debes procurar, por
supuesto, que el cliente nunca pueda retirar más dinero del que posee. Esto no está permitido.
Recuerda que ahora que sabes crear clases y objetos que son estables y que retienen
información, no necesitas crear funciones que devuelvan el balance, ya que la instancia de
cliente puede saber constantemente cuál es su saldo debido a que puede hacer sus operaciones
llamando directamente a este atributo y no a una variable separada.
"""
import random


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f"Datos del cliente:\n"
                f"    Nombre:         {self.nombre}\n"
                f"    Apellido:       {self.apellido}\n"
                f"    Nº de cuenta:   {self.numero_cuenta}\n"
                f"    Saldo:          {self.balance}")

    def depositar(self):
        print("**************************************************")
        print(f"Bienvenido de nuevo {self.nombre} {self.apellido}")
        print("__________________________________________________")
        cantidad = int(input("¿Que cantidad que desea ingresar?\n "))
        self.balance += cantidad
        print("Operación realizada con éxito")
        print("*****************************")

    def retirar(self):
        print("**************************************************")
        print(f"Bienvenido de nuevo {self.nombre} {self.apellido}")
        print("__________________________________________________")
        cantidad = int(input("¿Que cantidad que desea retirar?\n "))

        if self.balance >= cantidad:
            self.balance -= cantidad
            print("Operación realizada con éxito")
            print("*****************************")
        else:
            print("Saldo insuficiente")
            print("******************")


def crear_cliente():
    nombre = "0"
    apellido = "0"
    numero_cuenta = "0"
    balance = 0

    while nombre.isnumeric():
        nombre = input("Introduce el nombre del cliente: ")
    while apellido.isnumeric():
        apellido = input("Introduce el apellido del cliente: ")

        numero_cuenta = str(random.randint(100000, 999999))

    print("****************************")
    print("!!Cliente creado con éxito¡¡")
    print("----------------------------")
    print(Cliente(nombre, apellido, numero_cuenta, balance))
    print("****************************")

    return Cliente(nombre, apellido, numero_cuenta, balance)


def seleccionar_cliente(lista_clientes):
    cliente_activo = 0

    print("Por favor, teclee su numero de cuenta:")
    numero_cuenta_cliente = input("Número de cuenta: ")
    print("\n")
    for persona in lista_clientes:
        if numero_cuenta_cliente != persona.numero_cuenta:
            cliente_activo += 1
        else:
            return cliente_activo

    return "Usuario no encontrado"


def inicio():
    opcion_elegida = ""
    lista_clientes = list()

    print("*" * 79)
    print("Bienvendido al Banco Virtual")
    print("*" * 79)

    while opcion_elegida != "5":
        print("¿Que operación desea escoger?")
        print("-" * 29)
        print("     1- Dar de alta a cliente.")
        print("     2- Depositar saldo.")
        print("     3- Retirar saldo.")
        print("     4- Ver datos cliente.")
        print("     5- Salir")
        opcion_elegida = input("Opción: ")

        match opcion_elegida:
            case "1":
                lista_clientes.append(crear_cliente())
            case "2":
                try:
                    print("----------------------------")
                    cliente_seleccionado = seleccionar_cliente(lista_clientes)
                    lista_clientes[cliente_seleccionado].depositar()
                    print("****************************")
                except TypeError:
                    print("!!Usuario no encontrado¡¡\n")
                    print("***************************")
            case "3":
                try:
                    print("----------------------------")
                    cliente_seleccionado = seleccionar_cliente(lista_clientes)
                    lista_clientes[cliente_seleccionado].retirar()
                    print("****************************")
                except TypeError:
                    print("!!Usuario no encontrado¡¡\n")
                    print("***************************")
            case "4":
                try:
                    cliente_seleccionado = seleccionar_cliente(lista_clientes)
                    print("----------------------------")
                    print(lista_clientes[cliente_seleccionado])
                    print("****************************")
                except TypeError:
                    print("!!Usuario no encontrado¡¡\n")
                    print("***************************")

    print("*************************************")
    print("Gracias por utilizar el Banco Virtual")
    print("*************************************")


"""
**************************************************************
                    INICIO DEL PROGRAMA
**************************************************************
"""
inicio()
