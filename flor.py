def preguntar_flor():
    flor = input("Hay flor en esta mano? (s/n): ")
    return flor.lower() == 's'


def gestionar_flor(pts_equipo_1, pts_equipo_2):
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
