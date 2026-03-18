print("SISTEMA DE PARQUEO")

capacidad_maxima = 10
parqueadero = []   
opcion = " "

while opcion != "3":
    
    parqueo_actual = len(parqueadero)
    cupos_disponibles = capacidad_maxima - parqueo_actual
    
    print(f"\nCapacidad máxima: {capacidad_maxima}")
    print(f"Parqueo actual: {parqueo_actual}")
    print(f"Cupos disponibles: {cupos_disponibles}")
    print("\n1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Salir del sistema")
    
    opcion = input("Seleccione su opción: ")
    if opcion == "1":
        if parqueo_actual < capacidad_maxima:
            placa = input("Ingrese su placa: ")
            if placa in parqueadero:
                print("Esta moto ya está en el parqueadero")
                
            else:
                parqueadero.append(placa)
                
        with open ("Registro de parqueo.txt", "a") as archivo:
                for opciones in parqueadero:
                    archivo.write (f"ENTRADA - {placa}\n")
                    
                    
                print(f"Moto con placa {placa} ingresó correctamente")
                
    else:
            print("Parqueo lleno, no hay espacio suficiente")
        elif opcion == "2":
        
    if parqueo_actual > 0:
            
            placa = input("Ingrese la placa que quiere salir: ")
            
    if placa in parqueadero:
                
                parqueadero.remove(placa)
                
    with open ("Registro de parqueo.txt", "a") as archivo:
                for opciones in parqueadero:
                    archivo.write (f"SALIDA  - {placa}\n")
        
                    
            
                print(f"Moto con {placa} salió correctamente")
                
    else:
            print("Esa placa no está en el parqueadero")
            
else:
    print ("no hay motos en el parqueadero")
elif:
    