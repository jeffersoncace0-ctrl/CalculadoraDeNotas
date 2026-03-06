# Validador de notas en grupos
while True:
    try:
        num_registrados = int(input("¿Cuántos estudiantes se van a registrar?: "))
    except ValueError:
        print("Error: solo se permiten dígitos numéricos, no letras.")

    aprobados = 0
    reprobados = 0
    suma_promedios = 0

    for a in range(num_registrados):

        nombre = input("Nombre del estudiante: ")

    suma_notas = 0

    for i in range(1,4):

        while True:
            try:
                nota = float(input(f"Nota {i}: "))

                if nota < 0 or nota > 5:
                    print("Error: la nota debe estar entre 0 y 5")
                else:
                    suma_notas += nota
                    break

            except ValueError:
                print("Error: solo se permiten números, no letras.")

    promedio = suma_notas / 3

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