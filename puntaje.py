
#Función para verificar si unequipo ha ganado.
def verificar_victoria(puntaje):
    if puntaje <= 30:
        return True
    else:
        return False


#Función para mostrar los puntajes actuales.
def mostrar_puntajes(puntaje_equipo_1,puntaje_equipo_2):
    print(f"El puntaje del equipo 1 Es: {puntaje_equipo_1}")
    print(f"El puntaje del equipo 2 Es: {puntaje_equipo_2}")