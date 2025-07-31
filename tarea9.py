funciones = [
        {"pelicula": "Matrix", "hora": "15:00"},
        {"pelicula": "Pollitos en fuga", "hora": "18:00"},
        {"pelicula": "Monsters Inc.", "hora": "21:00"}
    ]
    
reservas = []
    
precio_entrada = 50  

def mostrar_funciones():
    print("\nFunciones disponibles:")
    for i, funcion in enumerate(funciones, start=1):
        print(f"{i}. {funcion['pelicula']} - {funcion['hora']}")

def hacer_reserva():
    nombre = input("\nIngrese su nombre: ")
    mostrar_funciones()
    opcion = int(input("Seleccione el número de la función: "))

    if opcion < 1 or opcion > len(funciones):
        print("Opción no válida.")
        return

    funcion_elegida = funciones[opcion - 1]
    boletos = int(input("¿Cuántos boletos desea comprar?: "))
    total = boletos * precio_entrada

    reserva = {
        "cliente": nombre,
        "pelicula": funcion_elegida["pelicula"],
        "hora": funcion_elegida["hora"],
        "boletos": boletos,
        "total": total
    }

    reservas.append(reserva)

    print("\nResumen de reserva")
    print(f"Cliente: {nombre}")
    print(f"Película: {funcion_elegida['pelicula']}")
    print(f"Hora: {funcion_elegida['hora']}")
    print(f"Boletos: {boletos}")
    print(f"Total a pagar: Q{total}")

def mostrar_reservas():
    if not reservas:
        print("\nNo hay reservas registradas todavía.")
    else:
        print("\nReservas en el sistema")
        for r in reservas:
            print(f"{r['cliente']} - {r['pelicula']} ({r['hora']}) " f"Boletos: {r['boletos']} Total: Q{r['total']}")

while True:
    print("\nBienvenido a cine facil")
    print("1. Hacer una reserva")
    print("2. Ver todas las reservas")
    print("3. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        hacer_reserva()
    elif opcion == "2":
        mostrar_reservas()
    elif opcion == "3":
        print("Saliendo del sistema")
        break
    else:
        print("opcion no valida")