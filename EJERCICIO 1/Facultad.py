from this import d
from turtle import st


from carrera import Carrera #se importa la clase continente
class facultad:
    __cod: int
    __nom: str
    __dire:str
    __loc:str
    __tel:int
    __carreras: list[Carrera] #Agregacion por composicion
    def __init__(self,cod,nom,dire,loc,tel):
        self.__cod=int(cod)
        self.__nom=str(nom)
        self.__dire=str(dire)
        self.__loc=str(loc)
        self.__tel=int(tel)
        self.__carreras=[] #SE AGREGA UNA LISTA VACIA
    
    def agregarcarre(self,obj): #Guarda las carreras en self.__carreras en forma de lista
        self.__carreras.append(obj)