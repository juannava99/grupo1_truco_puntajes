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
        print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")         #si la respuesta no es s o n pide la entrada de nuevo llamando a la misma funcion nuevamente
        return preguntar_envido()

#Función para calcular los puntos del envido.
def puntos_envido(opcion, puntaje_ganador,puntaje_perdedor):
    if opcion == "1":
        return 2 
    elif opcion == "2":
        return 3
    elif opcion == "3":
        return 4
    
    #creo que la de falta envido esta mal, habria que chequear
    
    elif opcion == "4":
        if puntaje_perdedor <= 15: 
            return 30 - puntaje_ganador
        else:
            return 30 - puntaje_perdedor
    elif opcion == "5":
        return 1 
    return 0 # en caso de que no coincida con ninguna 

#Función para actualizar el puntaje en caso de que haya envido.
def gestionar_envido(puntaje_equipo_1,puntaje_equipo_2):
    se_jugo,opcion = preguntar_envido()
    if se_jugo:
        puntos = puntos_envido(opcion,puntaje_equipo_1,puntaje_equipo_2)
        ganador = input("Quien gano el envido? (1/2): ")
        if ganador == '1':
            print(f"Se anotaran {puntos} puntos al equipo {ganador}\n")
            puntaje_equipo_1 += puntos
        elif ganador == '2':
            print(f"Se anotaran {puntos} puntos al equipo {ganador}\n")
            puntaje_equipo_2 += puntos
        else:
            print("Opcion no valida, ingrese '1' o '2'.")
            return gestionar_envido(puntaje_equipo_1,puntaje_equipo_2) # en caso de que cargue una opcion no valida vuelve a preguntar
    else:
        print("No se jugo el envido en esta mano.")
        return puntaje_equipo_1, puntaje_equipo_2,False
    return puntaje_equipo_1, puntaje_equipo_2,True
<<<<<<< HEAD
=======

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
>>>>>>> 75bd257 (Nuevo Commit)
