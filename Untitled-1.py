# Programa para determinar si un número es positivo, negativo o cero

# Pedimos al usuario que ingrese un número
numero = float(input("Por favor, ingresa un número: "))

# Verificamos si el número es positivo, negativo o cero
if numero > 0:
    print("El número que ingresaste es positivo.")
elif numero < 0:
    print("El número que ingresaste es negativo.")
else:
    print("El número que ingresaste es cero.")