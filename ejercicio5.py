#Ejercicio 5: Calcular el costo final de un precio donde se le resta eñ 15% del total de la compra

precio1 = float(input("Ingrese el costo final de la compra: "))

descuento = precio1 * 0.15

precio2 = precio1 - descuento

print(f"El precio ya con descuento es de ${precio2:.2f}")