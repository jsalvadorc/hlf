from variables import *
import numpy as np
import random

'''
def mostrar_tablero(tablero_barcos, tablero_disparos):
    # Función para mostrar el tablero de barcos y disparos
    print("Tablero de Barcos:")
    for fila in tablero_barcos:
        print(" ".join(str(casilla) for casilla in fila))
    print("Tablero de Disparos:")
    for fila in tablero_disparos:
        print(" ".join(str(casilla) for casilla in fila))'''

def validar_coordenadas(fila, columna, tamaño_tablero):
    # Función para validar si las coordenadas están dentro del rango del tablero
    if 0 <= fila < tamaño_tablero and 0 <= columna < tamaño_tablero:
        return True
    else:
        return False

def jugar_turno_jugador(tablero):
    # Función para el turno del jugador
    while True:
        fila = int(input("Introduce fila para disparar (0-9): "))
        columna = int(input("Introduce columna para disparar (0-9): "))
        if validar_coordenadas(fila, columna, tablero.tamaño):
            resultado_disparo = tablero.disparar(fila, columna)
            return fila, columna, resultado_disparo
        else:
            print("Coordenadas fuera del rango. Inténtalo de nuevo.")

def jugar_turno_maquina(tablero):
    # Función para el turno de la máquina (juego automático)
    fila = random.randint(0, tablero.tamaño - 1)
    columna = random.randint(0, tablero.tamaño - 1)
    resultado_disparo = tablero.disparar(fila, columna)
    return fila, columna, resultado_disparo
def disparar(self, fila, columna):
        '''
Usage: Updates the game boards based on the specified coordinates, marking hits ("X") or misses ("F") on the opponent's 
ships board (tablero_barcos) and shots fired board (tablero_disparos).
Why: Manages the state of the game, determining the impact of each shot and facilitating the win condition.'''
        # Función para realizar un disparo en las coordenadas especificadas
    # y actualizar el tablero de barcos y disparos
        if self.tablero_barcos[fila][columna] == "O":
            self.tablero_barcos[fila][columna] = "X"
            self.tablero_disparos[fila][columna] = "X"
            return True
        else:
            self.tablero_disparos[fila][columna] = "F"
            return False

'''def crear_barco_random(eslora):

    # Función para crear un barco de eslora específica en una posición aleatoria
    orientacion = random.choice(["este", "oeste", "norte", "sur"]) 
    barco_random = []
    fila_random = random.randint(0, 9)
    columna_random = random.randint(0, 9)
    barco_random.append((fila_random, columna_random))

    if orientacion == "este":
        # Este
        while len(barco_random) < eslora:
            columna_random = columna_random + 1
            barco_random.append((fila_random, columna_random))
    elif orientacion == "oeste":
        # Oeste
        while len(barco_random) < eslora:
            columna_random = columna_random - 1
            barco_random.append((fila_random, columna_random))
    elif orientacion == "norte":
        # Norte
        while len(barco_random) < eslora:
            fila_random = fila_random - 1
            barco_random.append((fila_random, columna_random))
    elif orientacion == "sur":
        # Sur
        while len(barco_random) < eslora:
            fila_random = fila_random + 1
            barco_random.append((fila_random, columna_random))
    
    return barco_random'''
