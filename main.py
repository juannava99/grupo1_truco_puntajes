from flor import gestionar_flor
from envido import gestionar_envido
from truco import gestionar_truco
from puntaje import verificar_victoria,mostrar_puntajes

puntaje_maximo = 30
global nombre_equipo_1
global nombre_equipo_2


def main():
    es_jugador_1 = True
    puntaje_equipo_1, puntaje_equipo_2 = 0,0
    ronda = 0
    nombre_equipo_1 = input("Ingrese el nombre del equipo 1: ")
    nombre_equipo_2 = input("Ingrese el nombre del equipo 2: ")
    
    while puntaje_equipo_1 < puntaje_maximo and puntaje_equipo_2 < puntaje_maximo:
        print(f"Ronda actual {ronda}")
        if es_jugador_1:
            print(f"Turno del jugador {nombre_equipo_1}")
            es_jugador_1 = False
        else:
            print(f"Turno del jugador {nombre_equipo_2}")
            es_jugador_1 = True
        puntaje_equipo_1,puntaje_equipo_2,se_jugo_envido = gestionar_envido(puntaje_equipo_1,puntaje_equipo_2)
        if not se_jugo_envido:
            puntaje_equipo_1,puntaje_equipo_2 = gestionar_flor(puntaje_equipo_1,puntaje_equipo_2)
        ronda += 1
        if verificar_victoria(puntaje_equipo_1):
            print(f"Gano el equipo {nombre_equipo_1}")
        if verificar_victoria(puntaje_equipo_2):
            print(f"Gano el equipo {nombre_equipo_2}")
        puntaje_equipo_1,puntaje_equipo_2 = gestionar_truco(puntaje_equipo_1,puntaje_equipo_2)
        mostrar_puntajes(puntaje_equipo_1,puntaje_equipo_2)
        if verificar_victoria(puntaje_equipo_1):
            print(f"Gano el equipo {nombre_equipo_1}")
        if verificar_victoria(puntaje_equipo_2):
            print(f"Gano el equipo {nombre_equipo_2}")
        
        
    



if __name__ == "__main__":
    main()

