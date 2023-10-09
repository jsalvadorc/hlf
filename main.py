from clases import Tablero
from funciones import *
from variables import *
import random
def jugar_turno(tablero):
    while True:
        fila = int(input("Introduce fila para disparar (0-9): "))
        columna = int(input("Introduce columna para disparar (0-9): "))
        if 0 <= fila < tamaño_tablero and 0 <= columna < tamaño_tablero and tablero.tablero_disparos[fila][columna] == "-":
            resultado_disparo = tablero.disparar(fila, columna)
            return fila, columna, resultado_disparo
        else:
            print("Coordenadas inválidas o ya disparaste allí. Inténtalo de nuevo.")
if __name__ == "__main__":
    '''Usage: This line checks whether the current script is being run directly (as the main program) or if it is being imported as 
    a module into another script.
Why: By using __name__ == "__main__", you can write code that will only be executed when the script is run directly. 
This allows you to separate the script's functionality (when run standalone) from its functions and classes that might be reused in other scripts. It promotes code reusability'''
    # Create separate boards for the player and the machine
    tablero_jugador = Tablero(tamaño_tablero, barcos)
    tablero_maquina = Tablero(tamaño_tablero, barcos)

    # Game loop
    while True:
        '''Usage: The while True loop creates an infinite loop, meaning it will keep executing its block of code as long as the 
        condition True remains true.
Why: In the context of the game, an infinite loop is used to keep the game running until a specific condition (winning or
 losing) is met. This structure ensures that the game continues indefinitely until one of the players wins or loses.'''
        # Player's turn
        print("Tu turno:")
        fila, columna, resultado_disparo = jugar_turno_jugador(tablero_maquina)
        print(f"Has disparado en la fila {fila} y columna {columna}.")
        if resultado_disparo:
            print("¡Impacto! Has golpeado un barco.")
        else:
            print("Agua. No has golpeado ningún barco.")
        tablero_maquina.mostrar_tablero_actual()

        # Check if player has won
        if tablero_maquina.hundir_todos_barcos():
            print("¡Felicidades! Has hundido todos los barcos de la máquina.")
            break

        # Computer's turn
        print("Turno de la máquina:")
        fila, columna, resultado_disparo = jugar_turno_maquina(tablero_jugador)
        print(f"La máquina disparó en la fila {fila} y columna {columna}.")
        if resultado_disparo:
            print("¡Impacto! La máquina ha golpeado un barco.")
        else:
            print("Agua. La máquina no ha golpeado ningún barco.")
        tablero_jugador.mostrar_tablero_actual()

        # Check if computer has won
        if tablero_jugador.hundir_todos_barcos():
            print("¡La máquina ha hundido todos tus barcos! Has perdido.")
            break











