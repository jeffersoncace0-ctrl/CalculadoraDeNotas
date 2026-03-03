#VALIDADOR DE CONTRASEÑAS


password = input("Enter your password: ")

if len(password)< 8:
            print ("The password must have at least 8 characteristics")

tiene_mayuscula = False
tiene_minuscula = False
tiene_un_caracter_especial= False
tiene_numero = False

for caracter in password:
        if caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            tiene_mayuscula = True

        if caracter in "abcdefghijklmnopqrstuvwxyz":
            tiene_minuscula = True

        if caracter in "0123456789":
            tiene_numero = True
            
        if caracter in "!@#$%^&*()_+-=[]{};:'\".<>?/|\\~`":
            tiene_un_caracter_especial = True

        if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_un_caracter_especial:
            print("Valid password")
        else:
            print("Invalid password")
            