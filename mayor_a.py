import sys

# Diccionario con las ventas del año
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




try:
    if len(sys.argv) > 1:
    
        valor = int(sys.argv[1])

        nueva_lista = []
#Valores >= valor
        for i in ventas:
            if ventas[i] >= valor:
                nueva_lista.append((i, ventas[i]))

        resultados = dict(nueva_lista)
        print(resultados)
        
    else:
        print("Ejecutar desde consola: python mayor_a valor númerico")

except ValueError:
    print("Ingresar solo valores númericos despues de mayor_a.py")



