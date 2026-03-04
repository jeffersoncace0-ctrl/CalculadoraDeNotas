print ("SISTEMA DE PARQUEO")

parqueo_actual = 5
capacidad_maxima = 10

while True:
    
    cupos_disponibles = capacidad_maxima - parqueo_actual
    
    print (f"\n capacidad maxima:{capacidad_maxima}")
    print (f"\n parqueo actual:{parqueo_actual}")
    print ("\n cupos disponible:{cupos disṕonibles}")
    
    print ("1.Registrar entrada")
    print ("2.Registrar salida")
    print ("3.Salir del sistema")

    opcion = input("Seleccione su opcion: ")

    if opcion == "1":
    
        if parqueo_actual < capacidad_maxima:
            placa = input ("Ingrese su placa: ")
            parqueo_actual += 1
            print (f"carros con placa{placa}ingreso correctamente")

        else :
            print ("Parqueo lleno, no hay espacio sufiente")
    
    elif opcion == "2":
        if parqueo_actual > 0: 
                placa = input ("Ingrese la placa que quiere salir: ")
                parqueo_actual -=1
                print ("carros con placa , salio correctamente")

        else: opcion == "3"
        print ("saliendo del sistema...")
else:
        print ("Opcion invalida")
    
    