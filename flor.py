#Función para preguntar si hubo flor en la ronda.
def preguntar_flor():
    flor = input("Hay flor en esta mano? (s/n): ")
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
        pts = 3
        while True:
            ganador = input("¿Quién ganó la flor? (e1 o e2): ").lower()
            if ganador in ['e1', 'e2']:
                if ganador == 'e1':
                    pts_equipo_1 += pts
                    print(f"Equipo 1 gana {pts} puntos por la flor.")
                elif ganador == 'e2':
                    pts_equipo_2 += pts
                    print(f"Equipo 2 gana {pts} puntos por la flor.")
                break
            else:
                print("Introduzca un valor válido (e1 o e2)")

    return pts_equipo_1, pts_equipo_2