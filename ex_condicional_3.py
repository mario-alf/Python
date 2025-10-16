#EJERCICIO 3: Crea un prgrama que identifique si el carcater ingresado es una vocal o consonante

letra = input("Ingres un caracter: ").lower()
#Lo que hace lower es la letra ingresada te la convierte a minuscula y la alamecena dentro de letra 

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"La letra {letra} si es una vocal")
else:
    print(f"La letra {letra} no es una vocal")