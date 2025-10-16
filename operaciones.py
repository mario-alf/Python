'''
    Este es un código de como se utilizan los operandos en python
    Hay dos ejemplos
    1) Donde realiza las operaciones con jerarquia de signos
    2) Donde realiza las operaciones con jerarquia de agrupaciones (parentesis)

    Args:
        num1 (int): Primer numero a sumar 
        num2 (int): Segundo numero a sumar

    Returns:
        oper1 (float): Resultado de la orimer operación
        oper2 (float): Resultado de la segunda operación
    
    Examples:
        >>> multiplicar 10 * 20.5 / 2 + 10
        112.5

        >>> sumar 10 + 20.5 * 10 / 2
        152.5
'''

#Declaración de variables
num1 = 10
num2 = 20.5
suma = num1 + num2
oper1 = num1 + num2 * 10 / 2
oper2 = (num1 + num2) * 10 / 2

#Imprimimos resultados en pantalla
print(f"La suma de {num1} + {num2} es igual a: {suma}")
print(f"El resultado de la operacion1 de {num1} + {num2} * 10 / 2 es igual a: {oper1}")
print(f"El resultado de la operacion2 de ({num1} + {num2}) * 10 / 2 es igual a: {oper2}")
