edad = 0
precio = 0
while True:

    try:
        edad = int(input("Ingresa la edad: "))
        if edad <= 12:
            precio = 8000
        elif edad <= 59:
            precio = 12000
        else:
            precio = 9000       
        print(precio)
    except ValueError:        
        print("valor ingresado es invalido.")