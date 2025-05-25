#Programa de primeros auxilios.

print("Este es es un Programa de Primeros Auxilios")
# Inicio

print("Inicio - La persona esta lastimada")
opciones = ["si", "no"]

# Evaluar respuesta a estímulos
while True:
    persona = input("¿Responde a estímulos? (si o no): ").lower()

    if persona == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano")
        break
    elif persona == "no":
        print("Abrir la vía aérea")
        break
    else:
        print("Responder 'si' o 'no'")

print("Fin del programa\n")

# Evaluar si respira
while True:
    respira = input("¿Respira? (si o no): ").lower()

    if respira == "si":
        print("Permitirle posición de suficiente ventilación")
        print("Fin del programa")
        break
    elif respira == "no":
        print("Administrar 5 ventilaciones y llamar a ambulancia")
        break
    else:
        print("Responder 'si' o 'no'")

# Evaluar signos de vida
while True:
    signos = input("¿Signos de vida? (si o no): ").lower()

    if signos == "si":
        print("Reevaluar a la espera de la ambulancia")
        break
    elif signos == "no":
        print("Administrar compresiones torácicas hasta que llegue ambulancia")
        break
    else:
        print("Responder 'si' o 'no'")

# Verificar llegada de ambulancia
while True:
    ambulancia = input("¿Llegó la ambulancia? (si o no): ").lower()

    if ambulancia == "si":
        print("Fin del programa")
        break
    elif ambulancia == "no":
        print("¿Signos de vida?")
    else:
        print("Responder 'si' o 'no'")


# Responde a estimulos?
"""opciones = ["si","no"]

estimulos = True

while estimulos:
    persona = input("Responde a estimulos (Si o No): ")
    persona = persona.lower()

    if persona == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano")
        break
    elif persona not in opciones:
        print("Responder Si o No")
    
    else:
        print("Abrir la vía Aérea")
        
print("Fin del progrma")
        

    
        

respira = input("¿Respira si o no?:")
respira = respira.lower()

while True:
    if respira == "si":
        print("Permitirle posición de suficiente ventilación")
        print("Fin del programa")
        break
    
    elif respira not in opciones:
        print("Responder Si o No")
        
        
    
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")

signos = input("¿Signos de vida (si/no): ")
signos = signos.lower()

while True:
    if signos == "si":
        print("Reevaluar a la espera de la ambulancia")
        break

    elif signos != opciones:
        print("Responder si o no:")
    
    else:
        print("Administrar compresiones Torácicas hasta que llegue ambulancia")
    
print("¿Llego la ambulancia")

ambulancia = input("Responder si o no:")
ambulancia = ambulancia.lower()

while True:
    if ambulancia == "si":
        print("Fin del progrma")
        break

    elif ambulancia not in opciones:
        print("Responder si o no")
    
    else:
        print("¿Signos de Vida?")"""
# Si (Valora la necesidad de adllevarlo al hospital más cercano) -> Fin del programa

# No -> (Abrí la vía Aérea)

# ¿Respira?

# Si (Permitirle posición de suficiente ventilación) -> Fin del programa

# No -> Administrar 5 ventilaciones y llamar a Ambulancia

# ¿Signos de Vida?

# Si -> Reevaluar a la espera de la Ambulancia -> ¿Llego la ambulancia? -> Si -> Fin del progrma

# No -> Administrar Comprensiones torácicas hasta que llegue ambulancia -> ¿Llegó la ambulancia? -> No -> ¿Signos de Vida? (Vuelta al bucle)