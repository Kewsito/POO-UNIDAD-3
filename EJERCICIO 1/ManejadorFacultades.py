from asyncore import read
from optparse import BadOptionError
from Facultad import facultad
from carrera import Carrera
import csv
class manejadorfacultades:
    __lista: list
    
    def __init__(self):
        self.__lista=[]
    
    def cargalista(self):
        with open ("Facultades.csv","r",encoding="latin1")as archivo:
            reader=csv.reader(archivo,delimiter=",")
            fila=next(reader) # Coloca el puntero en la primera posicion y lo guarda en la variable Fila perteneciente a la clase facultad
            bandera=True
            fac=[]
            while bandera:
                print("Facultad: {} ".format(fila))
                print("Carreras:")
                filacarrera=next(reader) #Coloca el puntero en la segunda posicion y lo gaurda en la variable Filacarrera perteneciente a la clase Carrera
                fac=facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                fac.append(fac)
                while bandera and fila[0] == filacarrera[0]: #Verifica si las carreras pertenecen a la facultad
                    print(filacarrera)
                    try:
                        c=Carrera(filacarrera[0],filacarrera[1],filacarrera[2],filacarrera[3],filacarrera[4],filacarrera[5])
                        fac.agregarcarre(c)
                        filacarrera=next(reader) #Coloca el puntero en la siguiente posicion
                    except StopIteration:
                        bandera=False
                
                fila=filacarrera
        