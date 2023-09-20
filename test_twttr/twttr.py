def main():

    print(shorten(input("Input: ")))



def shorten(palabra):

    lista_letras = ["a", "e", "i", "o", "u"]
    palabra2 = str()

    for i in palabra:
        if i.lower() not in lista_letras:
            palabra2 += i
        else:
            continue
    return palabra2


if __name__ == "__main__":
    main()