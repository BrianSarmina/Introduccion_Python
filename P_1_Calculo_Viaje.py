###* Programa para el cálculo de tiempo de viaje *###
###*    con multiples puntos de viaje            *###
# Fecha: 03 / 02 / 2022
# Autor: Ing. Brian García Sarmina

#- Importar paqueterias -#
import os                           # Paquetería para funciones del sistema.
import numpy as np                  # Paquetería estandar de Python para cómputo científico.
import matplotlib.pyplot as plt     # Paquetería para visualización.


while True: # Ciclo "while infinito".
    
    #- Pedir los datos al usuario -#
    print("Ingrese los datos para el calculo de tiempo de viaje")
    puntos = int(input("¿Cuántas ubicaciones tiene el recorrido (entero)? "))
    contador_puntos = 0     # Contador de puntos para las ubicaciones del recorrido.
    ubicaciones = [] # Coordenadas relacionadas entre "x" y "y".
    posiciones_x = []   # Valores de ubicaciones en el eje "x".
    posiciones_y = []   # Valores de ubicaciones en el eje "y".
    
    
    for i in range(puntos):
        # Aqui se va agregando cada ubicación del punto correspondiente, separando entre
        # coordenada "x" y "y".
        x_nom = "Agregar la ubicación X del punto " + str(contador_puntos) + ": "
        y_nom = "Agregar la unicación Y del punto " + str(contador_puntos) + ": "
        ubi_x = float(input(x_nom))
        ubi_y = float(input(y_nom))
        ubicaciones.append([ubi_x, ubi_y])
        posiciones_x.append(ubi_x) # Se guardan las ubicaciones en "x".
        posiciones_y.append(ubi_y) # Se guardan las ubicaciones en "y".
        contador_puntos += 1

    # Velocidad promedio, se supone en (km/h).
    velocidad = float(input("Ingrese la velocidad promedio del viaje (float): "))

    #- Calculo de distancias -#
    distancias = []     # Lista para almacenar las distancias.
    dist_nom_val = []   # Lista de nombres y valores para lineas.
    distancia_total = 0 # Valor total de distancia recorrida.
    contador_puntos = 0 # Contador de puntos, para el número de etiqueta de distancia.
    
    for i in range(0, len(ubicaciones)-1):  # Recorrido de todas las ubicaciones, es importante quitar una posición.
        ubi_1 = ubicaciones[i]              # Ubicación de origen.
        ubi_2 = ubicaciones[i+1]            # Ubicación destino.
        #- Ecuación para el cálculo de la distancia -# FORMA [[x1,y1],[x2,y2]]
        dist_x = np.power((ubi_2[0] - ubi_1[0]), 2)     # Valor al cuadrado de "x2 - x1".
        dist_y = np.power((ubi_2[1] - ubi_1[1]), 2)     # Valor al cuadrado de "y2 - y1".
        distancia = np.sqrt((dist_x + dist_y))          # Valor de la distancia.
        #---#
        #- Cálculo de posiciones de distancias -#
        nombre_y_val = "Dist " + str(contador_puntos) + " = " + str(round(distancia, 4)) + "km" # Se establece el nombre y la distancia.
        et_x = (ubi_2[0] + ubi_1[0]) / 2    # Valor medio de valores de x.
        et_y = (ubi_2[1] + ubi_1[1]) / 2    # Valor medio de valores de y.
        plt.text(et_x, et_y, nombre_y_val)  # Incorporar los valores medios a una etiqueta en Matplotlib.
        #---#
        dist_nom_val.append(nombre_y_val)   # Agregamos el nombre y la distancia a la lista.
        distancia_total += distancia        # Se incrementa el valor de la distancia total.
        distancias.append(distancia)        # Agregar la distancia calculada a la lista.
        contador_puntos += 1                # Incrementamos el contador de puntos, para los nombres de las líneas.

    #- Cálculo de tiempo total de recorrido -#
    print("Distancia total de recorrido: ", distancia_total, " kms")
    tiempo_total = distancia_total / velocidad
    print("Tiempo total de recorrido: ", tiempo_total, " hrs")
        
    #- Visualización de los datos -#
    plt.grid(linestyle='--')                # Tipo de malla para la gráfica.
    plt.plot(posiciones_x, posiciones_y)    # Generar las lineas de union entre las ubicaciones.
    plt.scatter(posiciones_x, posiciones_y, color='red') # Ubicaciones del recorrido.

    for i in range(len(ubicaciones)): # Nos aseguramos de iterar sobre todos los puntos.
        nombre = 'Punto ' + str(i)  # Vamos modificando el nombre del punto.
        plt.text((posiciones_x[i]+0.1), (posiciones_y[i]), nombre) # Agregamos el nombre del punto.

    plt.xlabel("Eje x (km)")     # Etiqueta del eje "x".
    plt.ylabel("Eje y (km)")     # Etiqueta del eje "y".
    plt.show()              # Función para mostrar la gráfica.
    
    #- Salir del programa -#
    print("\n")
    salir = input("Desea salir del programa (s/n): ") # Preguntamos por salida del programa.
    if salir == 's': # Si responde que "s" (si) se aplica un "break" y salimos del while infinito.
        break
    else:
        print ("\n" * 5) # Si responde otra cosa diferente a "s" se continua el while infinito y aplicamos                
        continue         # da un salto de 5 espacios.
    
##-- FIN DEL PROGRAMA --##
