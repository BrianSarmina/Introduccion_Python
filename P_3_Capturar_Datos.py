### RECABAR DATOS ###
# Fecha: 09 / 02 / 2022
# Autor: Ing. Brian García Sarmina

#- Importar paqueterias -#
import numpy as np


#- Función para solicitar los datos del nuev@ empleado@ -#
def solicitarDatos():
    print("Ingrese los datos del nuev@ emplead@")
    nombre = input("Ingrese el nombre (Nombre Apellido1 Apellido2): ") # Ingresa nombre.
    edad = input("Ingrese la edad: ") # Ingresa edad.
    sexo = input("Ingrese el sexo: ") # Ingresa sexo.
    return nombre, edad, sexo # Regresamos los datos en variables separadas.

#- Función para verificar los datos -#
def verificarDatos(nombre, edad, sexo): # La función recibe los datos del nuev@ emplead@.
    print("\n")
    print("-------------------VERIFICAR-------------------")
    print("El nombre ingresado fue: ", nombre)  # Presentamos nombre.
    print("La edad ingresada: ", edad)          # Presentamos edad.
    print("El sexo que refiere el emplead@ es: ", sexo) # Presentamos sexo.
    verificar = input("Los datos ingresados son correctos (s/n): ") # Preguntamos si son correctos.
    print("----------------------------------------------")
    
    if verificar == 's': # Verificamos correctos los datos.
        verificar = True # Regresamos "True" para salir del while del main.
    else:
        verificar = False # Se repite el while del main, y se vuelven a preguntar los datos.

    return verificar    # Regresamos verificar como booleano (TRUE o FALSE).

#- Función para guardar datos en archivo .txt -#
def guardarDatos(nombre, edad, sexo): # Recibe los parametros de nombre, edad y sexo.

    # Primero tenemos que separar el nombre y apellidos.
    # La función ".split()" separa una cadena (string) en elementos
    # de una lista ['nombre', 'apellido1', 'apellido2'] segun el
    # elemento que asignamos dentro del parentesis, en este caso
    # se coloca (" ") se indica separar por cada espacio detectado.
    nombre = nombre.split(" ")
    nombre_em = nombre[0]  # Tomamos el primer elemento de la lista, que es el nombre.
    apellido_1 = nombre[1] # Seguno elemento "nombre[1]" corresponde al primer apellido.
    apellido_2 = nombre[2] # Tercer elemento "nombre[2]" corresponde al segundo apellido.

    # Este es el metodo para abrir un archivo de texto con el nombre
    # "datos_empleados.txt", si este archivo no existe, este mismo comando
    # lo crea. Despues se tiene "w" que indica el tipo de acción que buscamos
    # con el archivo, en este caso "w" se refiere a "write" que permite editar
    # en el archivo y escribir en el, tambien se puede hacer solo de lectura.
    tipo_edicion = 'a'
    with open("datos_empleados.txt", tipo_edicion) as f: # "f" es el nombre de la variable referente al archivo.
        if tipo_edicion == 'a':
            # Datos es la varible que contendra todos los datos del empleado en el formato expuesto.
            datos = nombre_em + '; ' + apellido_1 + '; ' + apellido_2 + '; ' + edad + '; ' + sexo
            f.write(datos) # "f.write()" sirve para escribir información en el archivo "f".
            f.write("\n")
        else: # En caso de ser primera creación de archivo.
            f.write("----------------FORMATO-----------------")
            f.write("\n")
            f.write("Nombre; Apellido1; Apellido2; Edad; Sexo") # Formato de columnas.
            f.write("\n")
            f.write("----------------------------------------")
            f.write("\n")
            datos = nombre_em + '; ' + apellido_1 + '; ' + apellido_2 + '; ' + edad + '; ' + sexo
            f.write(datos)
            f.write("\n")
        f.close() # SE CIERRA EL ARCHIVO Y SE GUARDA LA INFORMACIÓN.

       
#--- MAIN ---#
if __name__ == "__main__":

    verificar = False # Variable para verificar datos, originalmente en FALSE.

    while (verificar == False): # WHILE se ejecuta mientras los datos no sean verificados.
        nombre, edad, sexo = solicitarDatos() # Llamamos a la funcion de solicitar datos.
        verificar = verificarDatos(nombre, edad, sexo) # Función de verificación.

    # Preguntamos para guardar datos en archivo.
    guardar = input("Desea guardar los datos ingresados (s/n): ")
    # Se guardan datos en archivo, si "s", en caso contrario termina programa.
    if guardar == 's':
        guardarDatos(nombre, edad, sexo)
        print("Datos guardados con exito.")
    else:
        print("Fin del programa, datos no guardados.")
                
#--- MAIN ---#    
