####Fede, ahi subi el modulo truco, en relacion a este modulo entiendo que la funcion preguntar_envido y puntos_envido, en caso de envido envido no querido sumaria 1 puntos, y deberian ser 3

# Función para preguntar el tipo de envido.
def preguntar_envido():
    x = input("¿Se jugó el envido? (s/n): ").lower()
    if x == 'n':
        return False, None
    elif x == 's':
        opciones_validas = ["1", "2", "3", "4", "5"]
        while True:
            opcion = input("¿Qué tipo de envido se jugó?\n1.envido\n2.real envido\n3.envido envido\n4.falta envido\n5.no querido\nIngrese la opcion: ").lower()
            if opcion in opciones_validas:
                return True, opcion
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
    else:
        print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")
        return preguntar_envido()

# Función para calcular los puntos del envido.
def puntos_envido(opcion, puntaje_ganador, puntaje_perdedor, malas):
    if opcion == 'envido':
        return 2 
    elif opcion == "2":
        return 3
    elif opcion == "3":
        return 4
    elif opcion == 'falta envido':
        if malas:
            return 30 - puntaje_ganador
        else:
            return 30 - puntaje_perdedor
    elif opcion == "5":
        return 1 
    return 0 # en caso de que no coincida con ninguna 

# Función para actualizar el puntaje en caso de que haya envido.
def gestionar_envido(puntaje_equipo_1, puntaje_equipo_2, malas):
    se_jugo, opcion = preguntar_envido()
    if se_jugo:
        puntos = puntos_envido(opcion, puntaje_equipo_1, puntaje_equipo_2, malas)
        ganador = input("¿Quién ganó el envido? (e1 o e2): ").lower()
        if ganador == 'e1':
            puntaje_equipo_1 += puntos
        elif ganador == '2':
            print(f"Se anotaran {puntos} puntos al equipo {ganador}\n")
            puntaje_equipo_2 += puntos
        else:
            print("Opción no válida, ingrese 'e1' o 'e2'.")
            return gestionar_envido(puntaje_equipo_1, puntaje_equipo_2, malas) # en caso de que cargue una opción no válida vuelve a preguntar
    else:
        print("No se jugó el envido en esta mano.")
        return puntaje_equipo_1, puntaje_equipo_2, False
    return puntaje_equipo_1, puntaje_equipo_2, True

# Ejemplo de uso
puntaje_equipo_1 = 0
puntaje_equipo_2 = 0

# Asumimos que sabemos si estamos en "malas" o "buenas". Aquí lo configuramos manualmente.
malas = True # Cambia a False si estás en buenas

# Gestionamos el envido en una partida
puntaje_equipo_1, puntaje_equipo_2, se_jugo_envido = gestionar_envido(puntaje_equipo_1, puntaje_equipo_2, malas)

print(f"Equipo 1: {puntaje_equipo_1} puntos")
print(f"Equipo 2: {puntaje_equipo_2} puntos")


#def main():
#    puntaje_equipo_1 = 0
#    puntaje_equipo_2 = 0
#    while True:
#        print("Puntaje actual:")
#        print(f"Equipo 1: {puntaje_equipo_1}")
#        print(f"Equipo 2: {puntaje_equipo_2}")
#        print("¿Qué deseas hacer?")
#        print("1. Anotar envido")
#        ###print (Anotar envido)
#        ###print (Anotar irse al mazo)
#        print("2. Salir")
#        opcion = input("Ingrese una opción: ")
#        if opcion == "1":
#            puntaje_equipo_1, puntaje_equipo_2 = gestionar_envido(puntaje_equipo_1, puntaje_equipo_2)
#        elif opcion == "2":
#            break
#        else:
#            print("Opción inválida. Por favor, ingrese una opción válida.")
#
#main()