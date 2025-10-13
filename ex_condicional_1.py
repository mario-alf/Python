#EJERCICIO 1: Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par, o si ambos lo son. 

num1 = int(input("ingrese un primer numero: "))
num2 = int(input("ingrese un segundo numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print(f"El numero {num1} y {num2} son par")

elif num1 % 2 == 0 and num2 % 2 != 0:
    print(f"El numero {num1} es par y el {num2} es impar")

elif num1 % 2 != 0 and num2 % 2 == 0:
    print(f"El numero {num1} es impar y el {num2} es par")
    