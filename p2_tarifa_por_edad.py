"""P-2: calcula la tarifa de entrada de acuerdo con la edad."""

edad = int(input("Ingrese la edad del usuario: "))
tarifa_completa = float(input("Ingrese el precio de la tarifa completa: "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif edad < 5:
    tarifa = 0
    print("Entrada gratuita.")
elif edad <= 17:
    tarifa = tarifa_completa * 0.50
    print("Se aplica un descuento del 50%.")
elif edad <= 64:
    tarifa = tarifa_completa
    print("Se aplica la tarifa completa.")
else:
    tarifa = tarifa_completa * 0.60
    print("Se aplica un descuento del 40%.")

if edad >= 0:
    print(f"Total a pagar: {tarifa:.2f}")
