import numpy as np
from variables import BOARD_SIZE, BARCO_1_LENGTH, BARCO_2_LENGTH, BARCO_3_LENGTH, BARCO_4_LENGTH

class Tablero:
    def __init__(self, jugador_id):
        self.jugador_id = jugador_id
        self.dimensiones = (BOARD_SIZE, BOARD_SIZE)
        self.barcos = {
            "Barco1": BARCO_1_LENGTH,
            "Barco2": BARCO_2_LENGTH,
            "Barco3": BARCO_3_LENGTH,
            "Barco4": BARCO_4_LENGTH
        }
        self.tablero_barcos = np.zeros(self.dimensiones)
        self.tablero_disparos = np.zeros(self.dimensiones)
        
    def colocar_barcos(self):
        for barco, longitud in self.barcos.items():
            cantidad = globals()[f'BARCO_{barco[-1]}_QUANTITY']
            for _ in range(cantidad):
                fila, columna, direccion = self.generar_coordenada_y_direccion(longitud)
                while not self.validar_colocacion_barco(fila, columna, longitud, direccion):
                    fila, columna, direccion = self.generar_coordenada_y_direccion(longitud)

                for i in range(longitud):
                    if direccion == 'norte':
                        self.tablero_barcos[fila - i][columna] = 1
                    elif direccion == 'sur':
                        self.tablero_barcos[fila + i][columna] = 1
                    elif direccion == 'este':
                        self.tablero_barcos[fila][columna + i] = 1
                    elif direccion == 'oeste':
                        self.tablero_barcos[fila][columna - i] = 1

    def generar_coordenada_y_direccion(self, longitud):
        fila = np.random.randint(0, BOARD_SIZE)
        columna = np.random.randint(0, BOARD_SIZE)
        direccion = np.random.choice(['norte', 'sur', 'este', 'oeste'])
        return fila, columna, direccion

    def validar_colocacion_barco(self, fila, columna, longitud, direccion):
        if direccion == 'norte' and fila - longitud >= 0:
            if np.sum(self.tablero_barcos[fila - longitud:fila, columna]) == 0:
                return True
        elif direccion == 'sur' and fila + longitud <= BOARD_SIZE:
            if np.sum(self.tablero_barcos[fila:fila + longitud, columna]) == 0:
                return True
        elif direccion == 'este' and columna + longitud <= BOARD_SIZE:
            if np.sum(self.tablero_barcos[fila, columna:columna + longitud]) == 0:
                return True
        elif direccion == 'oeste' and columna - longitud >= 0:
            if np.sum(self.tablero_barcos[fila, columna - longitud:columna]) == 0:
                return True
        return False

    def disparar(self, coordenada):
        fila, columna = coordenada
        if self.tablero_barcos[fila][columna] == 1:
            self.tablero_barcos[fila][columna] = 2  # Mark hit
            return True
        else:
            return False

    def hundido_todos_barcos(self):
        return np.sum(self.tablero_barcos) == 0
    def actualizar_tablero(self, coordenada, resultado):
        fila, columna = coordenada
        if resultado == "hit":
            self.tablero_disparos[fila][columna] = "X"  # Mark hit on the shots board
        else:
            self.tablero_disparos[fila][columna] = "F"  # Mark miss on the shots board
 