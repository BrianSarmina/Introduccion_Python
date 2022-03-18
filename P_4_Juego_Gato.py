### JUEGO DE GATO ###
# Fecha: 14 / 03 / 2022
# Autor: Ing. Brian García Sarmina

#- Importar paqueterías -#
import numpy as np
import random

#- Función para actualizar el tablero -#
def actualizarTablero(tirada, tirada_maq, tiradas_totales_us):
    if tirada != []: # Recibe la tirada del usuario.
        tirada_x = tirada[0][0] # Coordenada X.
        tirada_y = tirada[0][1] # Coordenada Y.
        tiradas_totales_us[tirada_x][tirada_y] = 1 # El "1" simboliza la tirada del usuario.
    if tirada_maq != []: # Recibe la tirada de la maquina.
        tirada_x = tirada_maq[0][0] # Coordenada X.
        tirada_y = tirada_maq[0][1] # Coordenada Y.
        tiradas_totales_us[tirada_x][tirada_y] = 2 # El "2" simboliza la tirada de la maquina.
                
    return tiradas_totales_us # Nuevo tablero actualizado.

#- Función para que el usuario seleccione jugada -#
def eligeTirada():
    tirada = []
    jugada_x = input("Ingrese la posición X que usará: ") # Jugador elige coordenada X.
    jugada_y = input("Ingrese la posición Y que usará: ") # Jugador elige coordenada Y.
    tirada.append([int(jugada_x), int(jugada_y)]) # Agregamos la tirada del jugador.
    return tirada # Regresamos la tirada elegida por el usuario.

#- Función para que la maquina seleccione jugada -#
def maquinaTirada(tiradas_totales_us):
    tirada_maq = []
    while True: # WHILE INFINITO.
        # Las tiradas de la maquina se dan de forma aleatoria
        # usando un rango de 0 a 2 (".randrange(0,3)").
        jugada_x = random.randrange(0,3) # Coordenada X de tirada.
        jugada_y = random.randrange(0,3) # Coordenada Y de tirada.
        # Evaluamos si la posición aleatoria generada esta libre.
        if tiradas_totales_us[jugada_x][jugada_y] != 1 and tiradas_totales_us[jugada_x][jugada_y] != 2:
            tirada_maq.append([jugada_x,jugada_y]) 
            break # Salimos del WHILE INFINITO.
    return tirada_maq # Regresamos la tirada de la maquina.

#- Función para verificar ganador -#
def ganador(tiradas_totales_us):
    com_ganadoras = [[[0,0],[0,1],[0,2]], [[0,0],[1,1],[2,2]], [[0,0],[1,0],[2,0]],
                     [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]], [[1,0],[1,1],[1,2]],
                     [[2,0],[2,1],[2,2]], [[2,0],[1,1],[0,2]]] # Combinaciones ganadoras
    for combinacion in com_ganadoras:
        us_ganador = 0  # Contador de aciertos para usuario.
        com_ganador = 0 # Contador de aciertos para computadora.
        for pos in combinacion: # Iteramos sobre cada combinación.
            if tiradas_totales_us[pos[0]][pos[1]] == 1: # Contabilizar tiradas de usuario.
                us_ganador += 1 # Gana un punto.
                if us_ganador == 3: # Gana el juego.
                    ganador = 'USUARIO' # Gana usuario.
                    return ganador # Salimos de la busqueda de ganador.
                else:
                    ganador = 'no' # Sigue juego.
            if tiradas_totales_us[pos[0]][pos[1]] == 2: # Contabilizar tiradas de maquina.
                com_ganador += 1 # Gana un punto.
                if com_ganador == 3: # Gana juego.
                    ganador = 'COMPUTADORA' # Gana maquina.
                    return ganador # Salimos de la busqueda de ganador.
                else:
                    ganador = 'no' # Sigue juego.
    return ganador # En caso de que no haya ganador, regresamos 'no'.

#- Función para dibujar tablero actual -#
def dibujarTablero(tiradas_totales_us):
    print("-------")
    print(tiradas_totales_us) # Imprimimos la matriz actual del tablero
    print("-------")

### MAIN ###
if __name__ == '__main__':
    print("Bienvenid@ al Juego de Gato")
    print("Las posiciones posibles de tiro son:")
    print("-------")
    print("|(0,0)|(0,1)|(0,2)|")
    print("|(1,0)|(1,1)|(1,2)|")
    print("|(2,0)|(2,1)|(2,2)|")
    print("-------")
    incio = True
    tirada = []
    tirada_maq = []
    tiradas_totales_us = np.zeros((3,3)) # Crea un matriz 3x3 que contiene solo 0s.
    print("Iniciando juego...")
    dibujarTablero(tiradas_totales_us) # Dibujamos tablero inicial (solo 0s).
    fin = False
    while fin == False:
        tirada = eligeTirada() # Se elige tirada del usuario.
        tiradas_totales_us = actualizarTablero(tirada, tirada_maq, tiradas_totales_us) # Se actualiza el tablero.
        tirada_maq = maquinaTirada(tiradas_totales_us) # La maquina elige su tirada.
        tiradas_totales_us = actualizarTablero(tirada, tirada_maq, tiradas_totales_us) # Se actualiza el tablero.
        dibujarTablero(tiradas_totales_us) # Dibujamos tablero despues de las tiradas del usuario y la maquina.
        hay_ganador = ganador(tiradas_totales_us) # Evaluamos si hay ganador.
        if hay_ganador == 'no':
            fin = False # Se sigue jugando.
        else:
            print("El ganador es: ", hay_ganador)
            fin = True # Se termina el "while infinito" de juego.
            
