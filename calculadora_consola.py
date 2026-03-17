PI = 3.1416 
salir = True
while salir == True:
    print("\n==============================")
    print("  CALCULADORA DE FIGURAS 2D Y 3D")
    print("==============================")
    print("1: 2D")
    print("2: 3D")
    print("3: Salir")
 
    try:
        elegir = int(input("Elige una opcion: "))
 
        # ==================== 2D ====================
        if elegir == 1:
            salir2 = True
            while salir2 == True:
                print("\n--- FIGURAS 2D ---")
                print("1: Cuadrado")
                print("2: Circulo")
                print("3: Triangulo")
                print("4: Rectangulo")
                print("5: Triangulo Rectangulo")
                print("6: Atras")
 
                try:
                    elegir2 = int(input("Elige una opcion: "))
 
                    # ---------- CUADRADO ----------
                    if elegir2 == 1:
                        salir3 = True
                        while salir3 == True:
                            print("\n- CUADRADO -")
                            print("1: Calcular Area")
                            print("2: Calcular Perimetro")
                            print("3: Calcular Lado (dado el area)")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    lado = float(input("Ingresa el lado del cuadrado: "))
                                    area = lado ** 2
                                    print(f"El area del cuadrado es: {area:.2f}")
                                elif elegir3 == 2:
                                    lado = float(input("Ingresa el lado del cuadrado: "))
                                    perimetro = lado * 4
                                    print(f"El perimetro del cuadrado es: {perimetro:.2f}")
                                elif elegir3 == 3:
                                    area = float(input("Ingresa el area del cuadrado: "))
                                    # Raiz cuadrada manual: lado = area^(1/2)
                                    lado = area ** 0.5
                                    print(f"El lado del cuadrado es: {lado:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    # ---------- CIRCULO ----------
                    elif elegir2 == 2:
                        salir3 = True
                        while salir3 == True:
                            print("\n- CIRCULO -")
                            print("1: Calcular Area")
                            print("2: Calcular Perimetro (Circunferencia)")
                            print("3: Calcular Radio (dado el area)")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    radio = float(input("Ingresa el radio del circulo: "))
                                    area = PI * radio ** 2
                                    print(f"El area del circulo es: {area:.2f}")
                                elif elegir3 == 2:
                                    radio = float(input("Ingresa el radio del circulo: "))
                                    circunferencia = 2 * PI * radio
                                    print(f"La circunferencia del circulo es: {circunferencia:.2f}")
                                elif elegir3 == 3:
                                    area = float(input("Ingresa el area del circulo: "))
                                    radio = (area / PI) ** 0.5
                                    print(f"El radio del circulo es: {radio:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    # ---------- TRIANGULO ----------
                    elif elegir2 == 3:
                        salir3 = True
                        while salir3 == True:
                            print("\n- TRIANGULO -")
                            print("1: Calcular Area")
                            print("2: Calcular Perimetro")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    base = float(input("Ingresa la base del triangulo: "))
                                    altura = float(input("Ingresa la altura del triangulo: "))
                                    area = (base * altura) / 2
                                    print(f"El area del triangulo es: {area:.2f}")
                                elif elegir3 == 2:
                                    lado1 = float(input("Ingresa el lado 1: "))
                                    lado2 = float(input("Ingresa el lado 2: "))
                                    lado3 = float(input("Ingresa el lado 3: "))
                                    perimetro = lado1 + lado2 + lado3
                                    print(f"El perimetro del triangulo es: {perimetro:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    # ---------- RECTANGULO ----------
                    elif elegir2 == 4:
                        salir3 = True
                        while salir3 == True:
                            print("\n- RECTANGULO -")
                            print("1: Calcular Area")
                            print("2: Calcular Perimetro")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    base = float(input("Ingresa la base del rectangulo: "))
                                    altura = float(input("Ingresa la altura del rectangulo: "))
                                    area = base * altura
                                    print(f"El area del rectangulo es: {area:.2f}")
                                elif elegir3 == 2:
                                    base = float(input("Ingresa la base del rectangulo: "))
                                    altura = float(input("Ingresa la altura del rectangulo: "))
                                    perimetro = 2 * (base + altura)
                                    print(f"El perimetro del rectangulo es: {perimetro:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    # ---------- TRIANGULO RECTANGULO ----------
                    elif elegir2 == 5:
                        salir3 = True
                        while salir3 == True:
                            print("\n- TRIANGULO RECTANGULO -")
                            print("1: Calcular Area")
                            print("2: Calcular Perimetro")
                            print("3: Calcular Hipotenusa (Teorema de Pitagoras)")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    base = float(input("Ingresa la base: "))
                                    altura = float(input("Ingresa la altura: "))
                                    area = (base * altura) / 2
                                    print(f"El area del triangulo rectangulo es: {area:.2f}")
                                elif elegir3 == 2:
                                    cateto1 = float(input("Ingresa el cateto 1: "))
                                    cateto2 = float(input("Ingresa el cateto 2: "))
                                    # Hipotenusa con raiz manual
                                    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
                                    perimetro = cateto1 + cateto2 + hipotenusa
                                    print(f"El perimetro del triangulo rectangulo es: {perimetro:.2f}")
                                elif elegir3 == 3:
                                    cateto1 = float(input("Ingresa el cateto 1: "))
                                    cateto2 = float(input("Ingresa el cateto 2: "))
                                    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
                                    print(f"La hipotenusa es: {hipotenusa:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    elif elegir2 == 6:
                        salir2 = False
                    else:
                        print("Opcion no valida.")
                except:
                    print("Valor no valido.")
 
        # ==================== 3D ====================
        elif elegir == 2:
            salir2 = True
            while salir2 == True:
                print("\n--- FIGURAS 3D ---")
                print("1: Cubo")
                print("2: Esfera")
                print("3: Cilindro")
                print("4: Cono")
                print("5: Rectangulo (Prisma rectangular)")
                print("6: Atras")
 
                try:
                    elegir2 = int(input("Elige una opcion: "))
 
                    # ---------- CUBO ----------
                    if elegir2 == 1:
                        salir3 = True
                        while salir3 == True:
                            print("\n- CUBO -")
                            print("1: Calcular Volumen")
                            print("2: Calcular Area de Superficie")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    lado = float(input("Ingresa el lado del cubo: "))
                                    volumen = lado ** 3
                                    print(f"El volumen del cubo es: {volumen:.2f}")
                                elif elegir3 == 2:
                                    lado = float(input("Ingresa el lado del cubo: "))
                                    area = 6 * lado ** 2
                                    print(f"El area de superficie del cubo es: {area:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    # ---------- ESFERA ----------
                    elif elegir2 == 2:
                        salir3 = True
                        while salir3 == True:
                            print("\n- ESFERA -")
                            print("1: Calcular Volumen")
                            print("2: Calcular Area de Superficie")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    radio = float(input("Ingresa el radio de la esfera: "))
                                    volumen = (4/3) * PI * radio ** 3
                                    print(f"El volumen de la esfera es: {volumen:.2f}")
                                elif elegir3 == 2:
                                    radio = float(input("Ingresa el radio de la esfera: "))
                                    area = 4 * PI * radio ** 2
                                    print(f"El area de superficie de la esfera es: {area:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    # ---------- CILINDRO ----------
                    elif elegir2 == 3:
                        salir3 = True
                        while salir3 == True:
                            print("\n- CILINDRO -")
                            print("1: Calcular Volumen")
                            print("2: Calcular Area de Superficie")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    radio = float(input("Ingresa el radio del cilindro: "))
                                    altura = float(input("Ingresa la altura del cilindro: "))
                                    volumen = PI * radio ** 2 * altura
                                    print(f"El volumen del cilindro es: {volumen:.2f}")
                                elif elegir3 == 2:
                                    radio = float(input("Ingresa el radio del cilindro: "))
                                    altura = float(input("Ingresa la altura del cilindro: "))
                                    area = (2 * PI * radio * altura) + (2 * PI * radio ** 2)
                                    print(f"El area de superficie del cilindro es: {area:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    # ---------- CONO ----------
                    elif elegir2 == 4:
                        salir3 = True
                        while salir3 == True:
                            print("\n- CONO -")
                            print("1: Calcular Volumen")
                            print("2: Calcular Area de Superficie")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    radio = float(input("Ingresa el radio de la base del cono: "))
                                    altura = float(input("Ingresa la altura del cono: "))
                                    volumen = (1/3) * PI * radio ** 2 * altura
                                    print(f"El volumen del cono es: {volumen:.2f}")
                                elif elegir3 == 2:
                                    radio = float(input("Ingresa el radio de la base del cono: "))
                                    altura = float(input("Ingresa la altura del cono: "))
                                    apotema = (radio ** 2 + altura ** 2) ** 0.5
                                    area = PI * radio * (radio + apotema)
                                    print(f"El area de superficie del cono es: {area:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    # ---------- PRISMA RECTANGULAR ----------
                    elif elegir2 == 5:
                        salir3 = True
                        while salir3 == True:
                            print("\n- PRISMA RECTANGULAR -")
                            print("1: Calcular Volumen")
                            print("2: Calcular Area de Superficie")
                            print("0: Atras")
                            try:
                                elegir3 = int(input("Elige una opcion: "))
                                if elegir3 == 1:
                                    largo = float(input("Ingresa el largo: "))
                                    ancho = float(input("Ingresa el ancho: "))
                                    altura = float(input("Ingresa la altura: "))
                                    volumen = largo * ancho * altura
                                    print(f"El volumen del prisma rectangular es: {volumen:.2f}")
                                elif elegir3 == 2:
                                    largo = float(input("Ingresa el largo: "))
                                    ancho = float(input("Ingresa el ancho: "))
                                    altura = float(input("Ingresa la altura: "))
                                    area = 2 * (largo * ancho + largo * altura + ancho * altura)
                                    print(f"El area de superficie del prisma rectangular es: {area:.2f}")
                                elif elegir3 == 0:
                                    salir3 = False
                                else:
                                    print("Opcion no valida.")
                            except:
                                print("Valor no valido.")
 
                    elif elegir2 == 6:
                        salir2 = False
                    else:
                        print("Opcion no valida.")
                except:
                    print("Valor no valido.")
 
        elif elegir == 3:
            print("\nHasta luego!")
            salir = False
        else:
            print("Opcion no valida.")
    except:
        print("El valor que ingresaste no se encuentra en las opciones.")