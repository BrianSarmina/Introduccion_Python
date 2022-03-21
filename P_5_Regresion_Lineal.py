### REGRESIÓN LINEAL ###
# Fecha: 16 / 03 / 2022
# Autor: Ing. Brian García Sarmina


#- Importar paqueterías -#
import numpy as np
import random as r
import matplotlib.pyplot as plt


#- Función para generar puntos "aleatorios" -#
def generarPuntos(num_puntos): # Función recibe el número de puntos para usar.
    punto_inicio = r.randrange(-5,5) # Seleccionamos un punto de inicio.
    puntos_gen = [] # Lista de puntos generados.
    puntos_x = [] # Lista de coordenadas X para los puntos.
    puntos_y = [] # Lista de coordenadas Y para los puntos.
    for i in range(num_puntos):
        distor_x = r.random() # Valor de distorción (salto) en X.
        distor_y = r.random() # Valor de distorción (salto) en Y.
        punto_x = punto_inicio + distor_x # Se distorsiona el punto de inicio en X.
        punto_y = punto_inicio + distor_y # Se distorsiona el punto de inicio en Y.
        punto_inicio += 0.4 # Nuevo inicio, se le aplica un salto de un valor constante.
        puntos_x.append(punto_x) # Lista de coordenadas X de los puntos.
        puntos_y.append(punto_y) # Lista de coordenadas Y de los puntos.
        puntos_gen.append([punto_x, punto_y]) # Agregamos los nuevos puntos.

    return puntos_gen, puntos_x, puntos_y # Regresamos la lista de puntos.


#- Calculo de regresión lineal -#
def calcularLinea(puntos_gen, puntos_x, puntos_y): # Recibe puntos generados.
    linea = [] # Linea de regresion.
    # Primero calculamos los promedios de los valores de X y Y.
    x_prom = np.sum(puntos_x) # Función "np.sum()" calcula la suma total de los elemtos de una lista.
    y_prom = np.sum(puntos_y) # Suma total de lista de coordenadas Y.
    x_prom = x_prom / len(puntos_gen) # Calculamos promedio de X.
    y_prom = y_prom / len(puntos_gen) # Calculamos promedio de Y.
    
    # Segundo: se calcula la "SUMA DE DESVIACIONES-CRUZADAS" entre Y y X.
    # Tercero: se calcula la "SUMA DE DESVIACIONES CUADRADAS" de X.
    sdc_xy = 0
    sdc_xx = 0 # Se calcula en el mismo FOR para ahorrar tiempo de ejecución.
    for punto in puntos_gen:
        #---Segundo---#
        x = punto[0] # Tomamos el valor de X.
        y = punto[1] # Tomamos el valor de Y.
        n = len(puntos_gen) # Valor de "n".
        d_xy = x*y - (n*x_prom*y_prom) # Calculo de desviación entre Xi y Yi.
        sdc_xy += d_xy # Suma de desviación cruzada.
        #---Tercero----#
        xx = np.power(x, 2) # x^2.
        x_prom_2 = np.power(x_prom, 2) # Valor de "x_prom" al cuadrado.
        d_xx = xx - n*x_prom_2 # Calculo de desviación para Xi.
        sdc_xx += d_xx         # Suma de desviación para Xi.

    # Cuatro: se calcula la "beta 1" y la "beta 0", para la ecuación de la recta.
    beta_1 = sdc_xy / sdc_xx        # Se relaciona con la "pendiente" de la curva.
    beta_0 = y_prom - beta_1*x_prom # Se relaciona con el "intercepto-y".

    # Quinto: calcular los puntos de la "RECTA DE REGRESIÓN".
    for punto in puntos_gen:
        x = punto[0] # Valores de coordenadas X.
        y_linea = beta_0 + beta_1*x # Función de la "RECTA DE REGRESIÓN".
        linea.append([x, y_linea])  # Guardamos los valores de la recta.

    return linea # Regresamos los valores de la RECTA de REGRESIÓN.


### MAIN ###
if __name__ == '__main__':
    print("Ejemplo para calculo de regresión lineal")
    num_puntos = int(input("¿Cuántos puntos desea usar ( <= 100 ): "))
    puntos_gen, puntos_x, puntos_y = generarPuntos(num_puntos) # Función para generar puntos de linea.
    linea = calcularLinea(puntos_gen, puntos_x, puntos_y)      # Función para calcular mejor linea "regresion".
    #- Visualización de puntos y recta de regresión -#
    plt.plot([0, 0], [-100, 100], color='black', linestyle="--")
    plt.plot([-100, 100], [0, 0], color='black', linestyle="--")
    plt.scatter(puntos_x, puntos_y) # Graficar puntos aleatorios.
    plt.plot([x[0] for x in linea], [y[1] for y in linea], color='red') # Grafica de recta de regresión.
    plt.grid(linestyle='--')
    plt.xlabel("x (INDEPENDIENTE)")
    plt.ylabel("y = f(x) (DEPENDIENTE)")
    plt.show()
