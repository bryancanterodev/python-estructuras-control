"""P-3: calcula la media de N calificaciones y cuenta notas >= 6.0."""

cantidad = int(input("Cuantas calificaciones desea ingresar?: "))

if cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
else:
    suma = 0.0
    aprobadas = 0

    for numero in range(1, cantidad + 1):
        nota = float(input(f"Ingrese la calificacion {numero}: "))
        suma += nota

        if nota >= 6.0:
            aprobadas += 1

    promedio = suma / cantidad
    print(f"Promedio: {promedio:.2f}")
    print(f"Cantidad de notas iguales o mayores a 6.0: {aprobadas}")
