
print("CALCULA TU PROMEDIO DE NOTAS")

entrada = input("Ingresa tus notas separadas por coma y las decimales separlas con Punto: ")


notas_str = entrada.split(",")        
notas = [float(nota) for nota in notas_str]  

if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print("Tu promedio es:", promedio)
else:
    print("No ingresaste ninguna nota.")

if promedio >= 3: 
    print ("¡Felicidades! Has aprobado")
else: 
    print ("No aprobaste")
