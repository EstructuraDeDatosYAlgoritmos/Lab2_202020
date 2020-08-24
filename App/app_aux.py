"""
Este modulo contiene todas las funciones auxiliares
"""
import App.config as cf
import csv

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


def countElementsByCriteria1(moviedetails: list, moviecasting: list, director_name: str)->tuple:
    if adt.size(data)==0:
        print("La lista esta vacía")
    else:
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

