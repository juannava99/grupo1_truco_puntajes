def preguntar_truco():
    print("¿Qué tipo de truco se jugó?")
    print("1. Truco")
    print("2. Truco, Quiero Retruco")
    print("3. Truco, Quiero Retruco y Quiero Vale 4")
    print("4. No se cantó truco")
    opcion = input("Ingrese una opción: ")
    return opcion


def puntos_truco(opcion):
    if opcion == "4":
        return 0

    querido = input("¿Querido? (s/n): ").lower()
    if opcion == "1":
        return 2 if querido == "s" else 1
    elif opcion == "2":
        return 3 if querido == "s" else 2
    elif opcion == "3":
        return 4 if querido == "s" else 3
    else:
        print("Opción inválida. No se anotaron puntos.")
        return 0


def gestionar_truco(puntaje_equipo_1, puntaje_equipo_2):
    opcion = preguntar_truco()
    puntos = puntos_truco(opcion)

    if puntos == 0:
        equipo_ganador = input("¿Qué equipo ganó la mano? (1/2): ")
        puntos = 1
    else:
        equipo_ganador = input("¿Qué equipo ganó el truco? (1/2): ")

    if equipo_ganador == "1":
        puntaje_equipo_1 += puntos
    elif equipo_ganador == "2":
        puntaje_equipo_2 += puntos
    else:
        print("Opción inválida para equipo ganador.")

    print(f"Se anotarán {puntos} puntos al equipo {equipo_ganador}\n")
    return puntaje_equipo_1, puntaje_equipo_2
