from variables import BOARD_SIZE
import numpy as np

def generar_coordenada_aleatoria():
    fila = np.random.randint(0, BOARD_SIZE)
    columna = np.random.randint(0, BOARD_SIZE)
    return fila, columna
def mostrar_tablero(tablero_barcos, tablero_disparos):
    print("Tablero de Barcos:")
    for fila in tablero_barcos:
        print(" ".join(str(casilla) for casilla in fila))
    print("Tablero de Disparos:")
    for fila in tablero_disparos:
        print(" ".join(str(casilla) for casilla in fila))