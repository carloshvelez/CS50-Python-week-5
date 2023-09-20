def main():
    pago = value(input("Saludo: "))
    print(f"${pago}")

def value(saludo):
    if saludo.lower().strip().startswith("hello"):
        return 0
    elif saludo.lower().strip().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
