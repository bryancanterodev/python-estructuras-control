"""P-4: permite hasta tres intentos para ingresar la clave de demostraci�n."""

clave_correcta = "python123"
intentos = 0
acceso_concedido = False

while intentos < 3:
    clave_ingresada = input("Ingrese la clave: ")
    intentos += 1

    if clave_ingresada == clave_correcta:
        print("Acceso Concedido")
        acceso_concedido = True
        break
    else:
        intentos_restantes = 3 - intentos
        if intentos_restantes > 0:
            print(f"Clave incorrecta. Intentos restantes: {intentos_restantes}")

if not acceso_concedido:
    print("Cuenta Bloqueada")
