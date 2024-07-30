#Función para preguntar si hubo flor en la ronda.
def preguntar_flor():
    flor = input("Hay flor en esta mano? (s/n): ").lower()
    if flor == "s":
        return True
    elif flor == "n":
        return False
    else:
        print("Respuesta no válida. Por favor, ingrese 's' o 'n'.")         #si la respuesta no es s o n pide la entrada de nuevo llamando a la misma funcion nuevamente
        return preguntar_flor()

#Función para actualizar el puntaje en caso de que haya flor.
def gestionar_flor(pts_equipo_1, pts_equipo_2):
        
    if(preguntar_flor()):
        while True:
            ganador = input("¿Quién ganó la flor? (1/2): ")
            if ganador in ['1', '2']:
                if ganador == '1':
                    pts_equipo_1 += 3
                    print(f"Equipo 1 gana 3 puntos por la flor.\n")
                elif ganador == '2':
                    pts_equipo_2 += 3
                    print(f"Equipo 2 gana 3 puntos por la flor.\n")
                break
            else:
                print("Introduzca un valor válido (1 o 2)")

    return pts_equipo_1, pts_equipo_2