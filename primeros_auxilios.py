#Programa de primeros auxilios.

print("Este es un Programa de Primeros Auxilios")
print("Inicio - La persona está lastimada")

opciones = ["si", "no"]

# Evaluar respuesta a estímulos
while True:
    persona = input("¿Responde a estímulos? (si o no): ").lower()
    if persona == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano")
        print("Fin del programa")
        exit()
    elif persona == "no":
        print("Abrir la vía aérea")
        break
    else:
        print("Por favor, responde 'si' o 'no'.")

# Evaluar si respira
while True:
    respira = input("¿Respira? (si o no): ").lower()
    if respira == "si":
        print("Permitirle posición de suficiente ventilación")
        print("Fin del programa")
        exit()
    elif respira == "no":
        print("Administrar 5 ventilaciones y llamar a la ambulancia")
        break
    else:
        print("Por favor, responde 'si' o 'no'.")

# Evaluar signos de vida y verificar llegada de ambulancia
while True:
    signos = input("¿Tiene signos de vida? (si o no): ").lower()
    if signos == "si":
        print("Reevaluar mientras esperas la ambulancia")
    elif signos == "no":
        print("Administrar compresiones torácicas hasta que llegue la ambulancia")
    else:
        print("Por favor, responde 'si' o 'no'.")
        continue  # volver a preguntar por signos

    while True:
        ambulancia = input("¿Llegó la ambulancia? (si o no): ").lower()
        if ambulancia == "si":
            print("Fin del programa")
            exit()
        elif ambulancia == "no":
            # Volver al inicio del ciclo de signos de vida
            print("Continuar asistencia. Reevaluando signos de vida...")
            break  # rompe ciclo interno y vuelve a preguntar por signos
        else:
            print("Por favor, responde 'si' o 'no'.")

