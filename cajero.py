#EJERCICIO 5: Hacer un prgrama que simule un cajero automático con un saldo inicial de $1000 
# y tendrá el siguiente menú de opciones: 
# 1.- Ingresar dinero a la cuenta
# 2.- Retirar dinero de la cuenta 
# 3.- Mostrar dinero disponible
# 4.- Salir

print("Selecciona la opción que desees realizar:\n1.- Ingresar dinero a la cuenta\n2.- Retirar dinero de la cuenta\n3.- Mostrar dinero disponible\n 4.- Salir\n")
dinero = 1000
opcion = int(input("Ingres la opcion que desees hacer: "))

if opcion == 1:
    ingresar = int(input("Ingresa la cantidad que desees despositar: "))
    saldo_final = dinero + ingresar
    print(f"Tu saldo final es de ${saldo_final}")

elif opcion == 2:
    ingresar = int(input("Ingresa la cantidad que desees retirar: "))
    if ingresar > dinero:
        print("Error: Ni cuentas ocn el saldo suficiente")
    else:
        saldo_final = dinero - ingresar
        print(f"Tu saldo final es de ${saldo_final}")

elif opcion == 3:
    print(f"Tu saldo actual es de ${dinero}")

elif opcion == 4:
    print("Gracias por usar nuestro sistema")

else:
        print(f"La opcion {opcion} no esta disponible.")