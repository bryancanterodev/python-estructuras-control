"""P-1: identifica el mayor de tres n�meros enteros o indica si son iguales."""

numero1 = int(input("Ingrese el primer n�mero entero: "))
numero2 = int(input("Ingrese el segundo n�mero entero: "))
numero3 = int(input("Ingrese el tercer n�mero entero: "))

if numero1 == numero2 == numero3:
    print("Los tres n�meros son iguales.")
elif numero1 >= numero2 and numero1 >= numero3:
    print(f"El mayor es: {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El mayor es: {numero2}")
else:
    print(f"El mayor es: {numero3}")
