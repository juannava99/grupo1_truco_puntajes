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
    opcion = preguntar_truco()
    puntos = puntos_truco(opcion)
    if puntos > 0:
        equipo_ganador = input("¿Qué equipo ganó el truco? (1/2): ")
        if equipo_ganador == "1":
            puntaje_equipo_1 += puntos
        else:
            puntaje_equipo_2 += puntos
    else:
        equipo_ganador = input("¿Qué equipo ganó la mano? (1/2): ")
        puntos = 1
        if equipo_ganador == "1":
            puntaje_equipo_1 += puntos
        else:
            puntaje_equipo_2 += puntos
                
    print(f"Se anotaran {puntos} puntos al equipo {equipo_ganador}\n")
    return puntaje_equipo_1, puntaje_equipo_2

#def main():
#    puntaje_equipo_1 = 0
#    puntaje_equipo_2 = 0
#    while True:
#        print("Puntaje actual:")
#        print(f"Equipo 1: {puntaje_equipo_1}")
#        print(f"Equipo 2: {puntaje_equipo_2}")
#        print("¿Qué deseas hacer?")
#        print("1. Anotar truco")
#        ###print (Anotar envido)
#        ###print (Anotar irse al mazo)
#        print("2. Salir")
#        opcion = input("Ingrese una opción: ")
#        if opcion == "1":
#            puntaje_equipo_1, puntaje_equipo_2 = gestionar_truco(puntaje_equipo_1, puntaje_equipo_2)
#        elif opcion == "2":
#            break
#        else:
#            print("Opción inválida. Por favor, ingrese una opción válida.")
#
#main()

