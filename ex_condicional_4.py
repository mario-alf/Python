#EJERCICIO 4: Crear un programa que simule una calcualdora segun la letra ingresada realizara la operación
#S, s -> Suma
# R, r -> Resta
# P, p, M, m -> Multiplicación
# D, d -> División
# E, e -> Exponenciación

print("Comanods para operaciones:\nSuma -> s o S\nResta -> r, R\nMultiplicación -> P, p, M, m\nDivision -> D, d\nExponenciacion -> E, e")
letra = input("Ingrese uan letra segun la operación que desee realizar: ") 

if letra == 's' or letra == 'S':
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    resultado = num1 + num2
    print(f"E resultdo de la suma entre {num1} + {num2} es {resultado}")

elif letra == 'r' or letra == 'R':
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    resultado = num1 - num2
    print(f"E resultdo de la resta entre {num1} - {num2} es {resultado}")

elif letra == 'm' or letra == 'M' or letra == 'p' or letra == 'P':
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    resultado = num1 * num2
    print(f"E resultdo de la multiplicacion entre {num1} * {num2} es {resultado}")

elif letra == 'd' or letra == 'D':
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    resultado = num1 / num2
    print(f"E resultdo de la division entre {num1} / {num2} es {resultado}")

elif letra == 'e' or letra == 'E':
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa la base al que lo quieras elevar: "))
    resultado = num1 ** num2
    print(f"E resultdo de la exponenciacion de {num1} a {num2} es {resultado}")

