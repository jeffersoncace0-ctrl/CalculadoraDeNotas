#ESTADISTICA DEL JUJU (JUNIOR)

partidos = int(input("Ingrese la cantidad de partidos: "))

puntos_totales = 0
pj = 0
pg = 0
pe = 0
pp = 0
gf = 0
gc = 0

for i in range(1, partidos + 1):
    while True:
        try:
            goles_favor = int(input(f"Goles a favor en el partido {i}: "))
            goles_contra = int(input(f"Goles en contra en el partido {i}: "))

            if goles_favor < 0 or goles_contra < 0:
                print("Error: los goles no pueden ser negativos.")
            else:
                gf += goles_favor
                gc += goles_contra
                break

        except ValueError:
            print("Error: solo se permiten números.")

    pj += 1

    if goles_favor > goles_contra:
        pg += 1
        puntos_totales += 3
    elif goles_favor == goles_contra:
        pe += 1
        puntos_totales += 1
    else: 8
        pp += 1

print("\nRESULTADOS")
print("Puntos totales:", puntos_totales)
print("Partidos jugados:", pj)
print("Partidos ganados:", pg)
print("Partidos empatados:", pe)
print("Partidos perdidos:", pp)
print("Goles a favor:", gf)
print("Goles en contra:", gc)