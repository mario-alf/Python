#CONDICIOANLES ANIDADOS

edad = int(input("Ingrese su edad: "))

if edad > 0 and edad < 100:
    print("La edad es correcta")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("La edad es incorrecta")