import sys


ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}
while True:

    print("Menu Principal")
    print("1. ejecutar algo")
    print("2. ejecutar algo")
    print("3. ejecutar algo")
    print("4. para salir")

    opcion = input("Ingresa la opcion")

    if opcion == "1":
        print("listo ...1")
    elif opcion == "2":
        print("listo ...2")
    elif opcion == "3":
        print("listo ...3")
    elif opcion == "4":
        print("saliste")
        break
    else:
        print("opcion no permitida")