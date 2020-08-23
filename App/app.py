"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar 
  datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (data_link, data, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    print("Cargando archivo ....")
    
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep
    
    data.clear()

    for link in data_link:
        try:
            with open(link, encoding="utf-8") as csvfile:
                spamreader = csv.DictReader(csvfile, dialect=dialect)
                for row in spamreader:
                    if row['id'] not in data.keys():
                        data[row['id']] = {}
                    for detail in row.keys():
                        data[row['id']][detail] = row[detail]
        except:
            data.clear()
            print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time()  #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def loadCSVFile1(archivo:str)->list:
    moviedetails = []
    
    archivo = open(archivo, "r")
    archivo.readline()
    linea = archivo.readline()
   
    while len(linea) > 0:
        
        lin=linea.split(";")
        moviedetails.append({"id":lin[0], "budget":lin[1],"genres":lin[2],"imdb_id":lin[3],"original_language":lin[4],"original_title":lin[5],"overview":lin[6],"popularity":lin[7],"nameproduction_companies":lin[8],"nameproduction_countries":lin[9],"release_date":lin[10],"revenue":lin[11],"runtime":lin[12],"namespoken_languages":lin[13],"status":lin[14],"tagline":lin[15],"title":lin[16],"vote_average":lin[17],"vote_count":lin[18],"numproduction_companies":lin[19],"numproduction_countries":lin[20],"numspoken_languages":lin[21]})
        linea = archivo.readline();
    archivo.close    
    return moviedetails

def loadCSVFile2 (archivo:str)->list:
    moviecasting = []
    
    archivo = open(archivo, "r")
    archivo.readline()
    linea = archivo.readline()
   
    while len(linea) > 0:
        
        lin=linea.split(";")
        moviecasting.append({"id":lin[0], "actor1_name":lin[1],"actor1_gender":lin[2],"actor2_name":lin[3],"actor2_gender":lin[4],"actor3_name":lin[5],"actor3_gender":lin[6],"actor4_name":lin[7],"actor4_gender":lin[8],"actor5_name":lin[9],"actor5_gender":lin[10],"actor_number":lin[11],"director_name":lin[12],"director_gender":lin[13],"director_number":lin[14],"producer_name":lin[15],"producer_number":lin[16],"screenplay_name":lin[17],"editor_name":lin[18]})
        linea = archivo.readline();
    archivo.close    
    return moviecasting


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Encontrar buenas películas de un director")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, data):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(data)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in data.keys():
            if criteria.lower() in data[element][column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(data, director):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """

    if len(data)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter = 0  #Cantidad de repeticiones
        average = 0
        for key in data.keys():
            vote = float(data[key]['vote_average'])
            if (data[key]['director_name'] == director)and(vote >= 6): #filtrar por promedio de votos
                counter += 1
                average += vote
                
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
        if average != 0:
            average /= counter
    
    return (counter,average)

def countElementsByCriteria1(moviedetails: list, moviecasting: list, director_name: str)->tuple:
     buenas = 0
     promedio = 0
     peliculas_d = 0                        
     for b in moviecasting:
        if b['director_name']==director_name: 
            peliculas_d+=1
            promedio += a['vote_average']
            promedio = promedio/peliculas_d
            for a in moviedetails:
                if a['vote_average']>= 6:
                    buenas+=1
                
                             
     resultado = (buenas, promedio)             
     return resultado

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    data = {} #instanciar un diccionario vacio

    data_link = [ #contiene los enlaces a los archivos .cvs
        "Data/themoviesdb/AllMoviesDetailsCleaned.csv",
        "Data/themoviesdb/AllMoviesCastingRaw.csv"
    ]

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile(data_link, data) #llamar funcion cargar datos
                print("Datos cargados, "+str(len(data))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(data)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else:
                    print("La lista tiene " + str(len(data)) + " elementos")
                    print(data['2'])
            elif int(inputs[0])==3: #opcion 3
                column=input('Ingrese el tipo de información que desea consultar\n')
                criteria=input('Ingrese el criterio de búsqueda\n')
                counter=countElementsFilteredByColumn(criteria, column, data) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria)
            elif int(inputs[0])==4: #opcion 4
                director = input('Ingrese el nombre del director\n')
                counter, average = countElementsByCriteria(data,director)
                print("Existen ",counter," peliculas buenas del director ", director, "con una puntuacion promedio de: ",average)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()
