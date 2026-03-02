print("")
print("#################################")
print("#                               #")
print("#        TIENDA DE ABU          #")
print("#                               #")
print("#################################")
print("")

try:
    nombreCliente = input("Hola, por favor ingrese el nombre del cliente: ")
    totalHuevo = 0
    totalPan = 0
    totalLeche = 0
    cantHuevo = 0
    cantPan = 0
    cantLeche = 0

    while True:
        productos = print("\n1. Huevo 10.500  \n2. Leche 5.500  \n3. Pan 2.000")
        print("")
        huevo = 10.500
        leche = 5.500
        pan = 2.000

        productoPedir = int(input("¿Que producto desea comprar?: "))

        match productoPedir:
            case 1:
                cantidad = int(input("Digite la cantidad de cajas huevos a comprar: "))
                cantHuevo += cantidad
                totalHuevo += huevo * cantidad
            case 2:
                cantidad = int(input("Digite la cantidad de litros de leche a comprar: "))
                cantLeche += cantidad
                totalLeche += leche * cantidad
            case 3:
                cantidad = int(input("Digite la cantidad de pan a comprar: "))
                cantPan += cantidad
                totalPan += pan * cantidad
            case _:
                print("No tenemos mas productos por el momento.")
                break
    
        decision = input("¿Desea seguir comprando (s/n)?:" ).lower()
        if decision == "s":
            continue
        else:
            break

    vip = input("Tiene membresia VIP? (s/n) ").lower()  
    vipBool = (vip == "s")
    
    subtotal = totalHuevo + totalLeche + totalPan
    descuento = 0.0
    iva = 0.19
    
    if vipBool:
        descuento = subtotal * 0.10

    subtIva = subtotal * iva
    totalPagar = subtotal - descuento + subtIva

    print("\n" + "*" * 45)
    print("* FACTURA DE LA COMPRA      ")
    print(F"Nombre:                        {nombreCliente}")
    print(f"Huevo:               cant: {cantHuevo}   ${totalHuevo:.3f}")
    print(f"Pan:                 cant: {cantPan}     ${totalPan:.3f}")
    print(f"Leche:               cant: {cantLeche}   ${totalLeche:.3f}")
    print("")
    print(f"Subtotal:                      ${subtotal:.3f}")
    
    if vipBool:
        print(f"Descuento aplicado (10%):      ${descuento:.3f}")
    else:
        print(f"Descuento aplicado (10%):      No aplica")

    print(f"IVA 19%:                      ${subtIva:.3f}")
    
    print(f"Total final a pagar:           ${totalPagar:.3f}")

except ValueError:
    print("Error: Por favor ingrese valores numericos validos para precio y cantidad.")