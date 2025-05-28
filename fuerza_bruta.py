import getpass
from string import ascii_lowercase

print("Programa para hackear contraseña")


while True:
    clave = getpass.getpass("Ingresas clave (sin letra 'ñ' ni caracteres especiales): ")

    t = 0
    e = 0

    while True:
        if e < len(clave):
            for letra in ascii_lowercase:
                t += 1

                if letra == clave[e]:
                    break

            e += 1

        else:
            print(f"La clave ingresada es: {clave}")
            print(f"La cantidad de veces intentadas fue: {t} veces")
            break
    break
