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

from DataStructures import arraylist as adt
from App.comparation import Comparation
from App.comparation import cmpfunction
from Sorting.mergesort import mergesort
from time import process_time
import App.config as cf
import sys
import csv

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

    data['elements'].clear()
    temp = {}
    for link in data_link:
        try:
            with open(link, encoding="utf-8") as csvfile:
                spamreader = csv.DictReader(csvfile, dialect=dialect)
                for row in spamreader:
                    
                    if row['id'] not in temp.keys():
                        temp[row['id']] = {}
                    for detail in row.keys():
                        temp[row['id']][detail] = row[detail]
            
            for element in temp.keys():
                try:
                    adt.addLast(data, temp.get(element))
                except:
                    pass

        except:
            data['elements'].clear()
            print("Se presento un error en la carga del archivo")
    
    del temp

    t1_stop = process_time()  #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Encontrar buenas películas de un director")
    print("5- Crear un ranking a partir de una lista de opciones")
    print("0- Salir")

def printRanking() -> None:
    """
    Imprime las categorias para crear un ranking
    """
    print("\nCategorias:")
    print("1- Mas votada")
    print("2- Menos votada")
    print("3- Mejor puntuación")
    print("4- Peor puntuación")

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
    if adt.size(data)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for i in range(1,adt.size(data)):
            element = adt.getElement(data,i)[column]
            if criteria.lower() in element.lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(data, director):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """

    if adt.size(data)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter = 0  #Cantidad de repeticiones
        average = 0
        for i in range(1,adt.size(data)):
            vote = float(adt.getElement(data,i)['vote_average'])
            if (adt.getElement(data,i)['director_name'] == director)and(vote >= 6): #filtrar por promedio de votos
                counter += 1
                average += vote
                
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
        if average != 0:
            average /= counter
    
    return (counter,average)


def orderElementsByCriteria(data,less):
    if adt.size(data)==0:
        print("La lista esta vacía")
    else:
        mergesort(data, less)
        ranking = []
        for i in range(1,11):
            ranking.append(adt.getElement(data, i))
        return ranking

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    data = adt.newList(cmpfunction)

    data_link = [ #contiene los enlaces a los archivos .cvs
        "Data/themoviesdb/AllMoviesDetailsCleaned.csv",
        "Data/themoviesdb/AllMoviesCastingRaw.csv"
    ]
    categoria = [
        'vote_count',
        'vote_average'
    ]

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile(data_link, data) #llamar funcion cargar datos
                print("Datos cargados, "+str(adt.size(data))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if adt.size(data)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else:
                    print("La lista tiene " + str(adt.size(data)) + " elementos")
                    print(adt.getElement(data,1))
            elif int(inputs[0])==3: #opcion 3
                column=input('Ingrese el tipo de información que desea consultar\n')
                criteria=input('Ingrese el criterio de búsqueda\n')
                counter=countElementsFilteredByColumn(criteria, column, data) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria)
            elif int(inputs[0])==4: #opcion 4
                director = input('Ingrese el nombre del director\n')
                counter, average = countElementsByCriteria(data,director)
                print("Existen ", counter, " peliculas buenas del director ", director, "con una puntuacion promedio de: ", average)
            elif int(inputs[0]) == 5:
                switch = True
                while switch:
                    printRanking()
                    criteria = int(input('Seleccione una opción para continuar\n'))
                    if (criteria <= 4) and (criteria > 0):
                        switch = False
                    else:
                        print("Opcion no valida")
                less = Comparation(categoria[(criteria-1) // 2])
                
                if criteria % 2 == 1:
                    ranking = orderElementsByCriteria(data,less.upVal)
                else:
                    ranking = orderElementsByCriteria(data, less.downVal)
                
                top = 1
                for element in ranking:
                    print(f'\n{top}. {element["title"]} de {element["director_name"]} con {element[categoria[(criteria-1) // 2]]}')
                    top += 1

                del less
                del ranking

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()
