# Programa para calificar una nota

# Pedimos al usuario que ingrese una nota
nota = float(input("Ingresa tu nota (entre 0 y 100): "))

# Verificamos la calificación según el rango
if nota >= 90 and nota <= 100:
    print("Excelente")
elif nota >= 70 and nota < 90:
    print("Aprobado")
elif nota >= 0 and nota < 70:
    print("Reprobado")
else:
    print("Nota fuera de rango")