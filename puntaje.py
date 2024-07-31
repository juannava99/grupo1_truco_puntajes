# Función para verificar si unequipo ha ganado.
def verificar_victoria(puntaje):
    puntaje_maximo = 30
    if puntaje >= puntaje_maximo:
        return True
    else:
        return False


# Función para mostrar los puntajes actuales.
def mostrar_puntajes(puntaje_equipo_1, puntaje_equipo_2):
    print(f"\nEl puntaje del equipo 1 es: {puntaje_equipo_1}")
    print(f"El puntaje del equipo 2 es: {puntaje_equipo_2}\n")
