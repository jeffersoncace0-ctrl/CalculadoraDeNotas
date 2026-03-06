
texto  = input ("Ingrese el texto: ")

contador = 0
en_palabra = False

for a in texto:
    if a  is not  " " and en_palabra == False:
        contador += 1
        en_palabra = True
    elif a == " ":
        en_palabra = False

print("Cantidad de palabras:", contador)
