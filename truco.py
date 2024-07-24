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
    else:
        querido = input("¿Querido? (s/n): ")
        if opcion == "1":
            if querido.lower() == "s":
                return 2
            else:
                return 1
        elif opcion == "2":
            if querido.lower() == "s":
                return 3
            else:
                return 2
        elif opcion == "3":
            if querido.lower() == "s":
                return 4
            else:
                return 3
        else:
            print("Opción inválida. No se anotaron puntos.")
            return 0

def gestionar_truco(puntaje_equipo_1, puntaje_equipo_2):
    pass
