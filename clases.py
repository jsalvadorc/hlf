import numpy as np
from variables import *
from funciones import crear_barco_random
import random


class Tablero:
    # Constructor de la clase Tablero que inicializa el tablero y coloca los barcos aleatoriament
    def __init__(self, tamaño, barcos):
        self.tamaño = tamaño
        self.tablero_barcos = self.crear_tablero()
        self.tablero_disparos = self.crear_tablero()
        self.colocar_barcos_random(barcos)

    def crear_tablero(self):# Crea un tablero vacío del tamaño especificado, lleno de "-"
        return [["-" for _ in range(self.tamaño)] for _ in range(self.tamaño)]

    def colocar_barcos_random(self, barcos):
        # Coloca los barcos en el tablero de manera aleatoria
        for eslora in barcos:
            while True:
                fila, columna, direccion = self.generar_coordenada_y_direccion(eslora)
                if self.validar_colocacion_barco(fila, columna, eslora, direccion):
                    for i in range(eslora):
                        if direccion == 'norte':
                            self.tablero_barcos[fila - i][columna] = "O"
                        elif direccion == 'sur':
                            self.tablero_barcos[fila + i][columna] = "O"
                        elif direccion == 'este':
                            self.tablero_barcos[fila][columna + i] = "O"
                        elif direccion == 'oeste':
                            self.tablero_barcos[fila][columna - i] = "O"
                    break
            
    def generar_coordenada_y_direccion(self,longitud): # Genera coordenadas y dirección aleatoria para colocar los barcos
        fila = random.randint(0, self.tamaño - 1)
        columna = random.randint(0, self.tamaño - 1)
        direccion = random.choice(['norte', 'sur', 'este', 'oeste'])
        return fila, columna, direccion

    def validar_colocacion_barco(self, fila, columna, longitud, direccion): # Valida si es posible colocar un barco en las coordenadas y dirección especificadas
        if direccion == 'norte' and fila - longitud >= 0:
            if all(self.tablero_barcos[fila - i][columna] == "-" for i in range(longitud)):
                return True
        elif direccion == 'sur' and fila + longitud <= self.tamaño:
            if all(self.tablero_barcos[fila + i][columna] == "-" for i in range(longitud)):
                return True
        elif direccion == 'este' and columna + longitud <= self.tamaño:
            if all(self.tablero_barcos[fila][columna + i] == "-" for i in range(longitud)):
                return True
        elif direccion == 'oeste' and columna - longitud >= 0:
            if all(self.tablero_barcos[fila][columna - i] == "-" for i in range(longitud)):
                return True
        return False
    def hundir_todos_barcos(self):# Verifica si todos los barcos han sido hundidos en el tablero
        for fila in self.tablero_barcos:
            for casilla in fila:
                if casilla == "O":
                    return False 
        return True   
    def disparar(self, fila, columna):# Realiza un disparo en las coordenadas especificadas y devuelve True si golpea un barco, False si no
        if self.tablero_barcos[fila][columna] == "O":
            self.tablero_barcos[fila][columna] = "X"
            self.tablero_disparos[fila][columna] = "X"
            return True
        else:
            self.tablero_disparos[fila][columna] = "F"
            return False

    def mostrar_tablero_actual(self):# Muestra el tablero actual de barcos y disparos
        print("Tablero de Barcos:")
        for fila in self.tablero_barcos:
            print(" ".join(str(casilla) for casilla in fila))
        print("Tablero de Disparos:")
        for fila in self.tablero_disparos:
            print(" ".join(str(casilla) for casilla in fila))

