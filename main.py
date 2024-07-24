from .flor import preguntar_flor,gestionar_flor
from .envido import preguntar_envido,gestionar_envido,puntos_envido
from .truco import preguntar_truco,gestionar_truco,puntos_truco
from .puntaje import verificar_victoria,mostrar_puntajes

puntaje_maximo = 30
puntaje_buenas = 15
puntaje_mala = 15


def main():
    es_jugador_1 = True
    puntaje_equipo_1, puntaje_equipo_2 = 0,0

    while puntaje_equipo_1 < puntaje_maximo or puntaje_equipo_2 < puntaje_maximo:
        if es_jugador_1:
            print("Turno del jugador 1")
            es_jugador_1 = False
        else:
            print("Turno del jugador 2")
            es_jugador_1 = True

        ya_pregunto = True



if __name__ == "__main__":
    main()

