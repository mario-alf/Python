#EJERCICIO 2: Crear un programa que pida 3 números y determine cual es el masa grande

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El numero mas grande es {num1}")

elif num2 >= num1 and num2 >= num3:
    print(f"El numero mas grande es {num2}")

elif num3 >= num1 and num3 >= num2:
    print(f"El numero mas grande es {num3}")


