#Programa de primeros auxilios.

print("Este es es un Programa de Primeros Auxilios")
# Inicio

print("Inicio - La persona esta lastimada")


# Responde a estimulos?
opciones = ["si","no"]


while True:
    persona = input("Responde a estimulos (Si o No): ")
    persona = persona.lower()

    if persona == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano")
        print("Fin del progrma")
        break

    if persona not in opciones:
        print("Responder Si o No")

# Si (Valora la necesidad de adllevarlo al hospital más cercano) -> Fin del programa

# No -> (Abrí la vía Aérea)

# ¿Respira?

# Si (Permitirle posición de suficiente ventilación) -> Fin del programa

# No -> Administrar 5 ventilaciones y llamar a Ambulancia

# ¿Signos de Vida?

# Si -> Reevaluar a la espera de la Ambulancia -> ¿Llego la ambulancia? -> Si -> Fin del progrma

# No -> Administrar Comprensiones torácicas hasta que llegue ambulancia -> ¿Llegó la ambulancia? -> No -> ¿Signos de Vida? (Vuelta al bucle)