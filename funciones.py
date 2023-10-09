from variables import BOARD_SIZE
import numpy as np

def generar_coordenada_aleatoria():
    fila = np.random.randint(0, BOARD_SIZE)
    columna = np.random.randint(0, BOARD_SIZE)
    return fila, columna
def mostrar_tablero(tablero_jugador, tablero_disparos):
        print("Tablero de Barcos:")
        for fila in tablero_jugador:
            print(" ".join(str(casilla) for casilla in fila))
        
        print("\nTablero de Disparos:")
        for fila in tablero_disparos:
            print(" ".join(" " if casilla == 0 else "X" if casilla == 1 else "O" for casilla in fila))