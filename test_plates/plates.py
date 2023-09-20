def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

#Definir si tiene entre 2 y 6 caracteres:
    if 2 <= len(s) <=6:
        longitud = True
    else:
        return False

    # 1. Definir si la placa empieza con dos letras:
    if s[0].isalpha() and s[1].isalpha():
        inicio_dos_letras = True
    else:
        return False



    #Definir si tiene puntos, espacios, etc.

    if s.isalnum():
        alfanumerico = True
    else:
        return False

    # definir si tiene números en el medio:
    indice = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            indice = i
            numero_placa = s[indice:len(s)]

            if numero_placa[0] == "0":
                    return False

            for i in numero_placa:
                if i.isalpha():
                    return False
            break



    return True


if __name__ == "__main__":
    main()



