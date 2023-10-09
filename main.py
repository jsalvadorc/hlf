from clases import Tablero
from funciones import *
from variables import *


def jugar():
    jugador = Tablero(jugador_id="Jugador")
    maquina = Tablero(jugador_id="Máquina")
    #se define la funcion jugar y se crean los objetos tablero
    jugador.colocar_barcos()
    maquina.colocar_barcos()
    #se llama a la funcion para colocar los barcos
    while True:
        mostrar_tablero(jugador.tablero_barcos, jugador.tablero_disparos)
        mostrar_tablero(maquina.tablero_disparos, maquina.tablero_barcos)  
    
        entrada = input("Tu turno. Ingresa coordenadas (fila y columna separadas por espacio): ").split()
        if len(entrada) != 2:
            print("Por favor, ingresa dos coordenadas separadas por espacio.")
            continue
        
        try:
            fila, columna = int(entrada[0]), int(entrada[1])
        except ValueError:
            print("Por favor, ingresa coordenadas válidas.")
            continue
        
        if 0 <= fila < len(jugador.tablero_disparos) and 0 <= columna < len(jugador.tablero_disparos[0]):
            if maquina.disparar((fila, columna)):
                print("¡Tocado!")
            else:
                print("Agua")
        else:
            print("Coordenadas fuera del rango.")
        
        if maquina.hundido_todos_barcos():
            print("¡Felicidades! Has ganado el juego.")
            break
        
        fila, columna = maquina.generar_coordenada_aleatoria()
        if jugador.disparar((fila, columna)):
            print(f"La máquina te ha impactado en la fila {fila} y columna {columna}.")
        else:
            print(f"La máquina ha fallado en la fila {fila} y columna {columna}.")
        
        if jugador.hundido_todos_barcos():
            print("La máquina ha ganado. Intenta de nuevo.")
            break

if __name__ == "__main__":
    jugar()