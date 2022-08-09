import sys
import os
import re


def encontrar_error(archivo):
    error = input("Qué error quieres buscar? ")#Ex: ERROR Failed
    errores_archivo =[]
    patron_errores=[]

    with open(archivo,'r',encoding='UTF-8') as f:
        for lineas in f.readlines():
            for i in range(len(error.split(' '))):
                patron_errores.append(error.split(' ')[i].lower())
            #all() devuelve true si todos los elementos de la lista lo devuelven
            #es decir, si encuentra coincidencia de todo lo pasado por el usuario en la linea
            if all(re.search(patron_error,lineas.lower()) for patron_error in patron_errores):
                errores_archivo.append(lineas)
                

    return errores_archivo
        
def crear_archivo_errores(errores):
    #Abrimos el archivo en el directorio que queramos
    #que se descagué añadendole el nombre del mismo,
    #En mi caso quiero que se descargue en una carpeta
    #de mi escritorio que se llama practice
    file = 'C:\\Users\\soria\\OneDrive\\Escritorio\\practice\\reporte_errores.log'
    #Si no queremos que se borre lo que hay dentro del archivo
    #cada vez que lo abramos deberiamos poner w+
    with open(file, 'w') as f:
       
        for error in errores:
            f.write(error)

#Usamos lo siguiente para que al ejecutar el script
#se ejecute lo siguiente si o sí ya que la varible global
#name tomará el nombre de main y por tanto entrará en el condicional
#Otra forma sería crear una función main() pero luego habría que llamarla
if __name__ == "__main__":
    #Al escribir nuestro comando en la terminal, bastará
    #con poner el archivo de errores al lado de este para que lo coja
    #al poner sys.argv[1]
    archivo_total_errores = sys.argv[1]
    errores =encontrar_error(archivo_total_errores)
    crear_archivo_errores(errores)
    sys.exit(0)     #Para indicar que todo ha salido correcto