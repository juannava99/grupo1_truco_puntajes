from flor import gestionar_flor
from envido import gestionar_envido
from truco import gestionar_truco
from puntaje import verificar_victoria, mostrar_puntajes

puntaje_maximo = 30


def main():
    puntaje_equipo_1, puntaje_equipo_2 = 0, 0
    ronda = 1
    print("Gestion de puntajes de truco\n")
    while puntaje_equipo_1 < puntaje_maximo and puntaje_equipo_2 < puntaje_maximo:
        print(f"Ronda actual {ronda}")
        puntaje_equipo_1, puntaje_equipo_2, se_jugo_envido = gestionar_envido(
            puntaje_equipo_1, puntaje_equipo_2
        )
        if not se_jugo_envido:
            puntaje_equipo_1, puntaje_equipo_2 = gestionar_flor(
                puntaje_equipo_1, puntaje_equipo_2
            )
        gano_equipo_1 = verificar_victoria(puntaje_equipo_1)
        gano_antes = False
        if gano_equipo_1:
            print(f"Gano el equipo equipo 1 con un puntaje de: {puntaje_equipo_1}")
            gano_antes = True
        gano_equipo_2 = verificar_victoria(puntaje_equipo_2)
        if gano_equipo_2 and not gano_equipo_1:
            print(f"Gano el equipo equipo 2 con un puntaje de: {puntaje_equipo_2}")
            gano_antes = True
        if not gano_equipo_1 and not gano_equipo_2:
            puntaje_equipo_1, puntaje_equipo_2 = gestionar_truco(
                puntaje_equipo_1, puntaje_equipo_2
            )

        mostrar_puntajes(puntaje_equipo_1, puntaje_equipo_2)

        gano_equipo_1 = verificar_victoria(puntaje_equipo_1)
        if gano_equipo_1 and not gano_antes:
            print(f"Gano el equipo equipo 1 con un puntaje de: {puntaje_equipo_1}")
        gano_equipo_2 = verificar_victoria(puntaje_equipo_2)
        if gano_equipo_2 and not gano_equipo_1 and not gano_antes:
            print(f"Gano el equipo equipo 2 con un puntaje de: {puntaje_equipo_2}")

        ronda += 1


if __name__ == "__main__":
    main()
