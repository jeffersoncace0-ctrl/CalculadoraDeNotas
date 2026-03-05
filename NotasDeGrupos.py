# Validador de notas en grupos

try:
        num_registrados = int(input("¿Cuántos estudiantes se van a registrar?: "))

except ValueError:
        print("Error: solo se permiten dígitos numéricos, no letras.")

aprobados = 0
reprobados = 0
suma_promedios = 0

for a in range(num_registrados):

    nombre = input("Nombre del estudiante: ")


    while True:
        try:
            nota1 = float(input("Nota 1: "))
            if nota1 < 0 or nota1 > 5:
                print("Error: la nota debe estar entre 0 y 5")
            else:
                break
        except ValueError:
            print("Error: solo se permiten números, no letras.")

    while True:
        try:
            nota2 = float(input("Nota 2: "))
            if nota2 < 0 or nota2 > 5:
                print("Error: la nota debe estar entre 0 y 5")
            else:
                break
        except ValueError:
            print("Error: solo se permiten números, no letras.")

    while True:
        try:
            nota3 = float(input("Nota 3: "))
            if nota3 < 0 or nota3 > 5:
                print("Error: la nota debe estar entre 0 y 5")
            else:
                break
        except ValueError:
            print("Error: solo se permiten números, no letras.")

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 3:
        aprobados += 1
        print(nombre, "aprobó con", promedio)
    else:
        reprobados += 1
        print(nombre, "reprobó con", promedio)

    suma_promedios += promedio


promedio_general = suma_promedios / num_registrados

print("\nRESULTADOS")
print("Total estudiantes:", num_registrados)
print("Número de reprobados:", reprobados)
print("Número de aprobados:", aprobados)
print("Promedio general:", promedio_general)