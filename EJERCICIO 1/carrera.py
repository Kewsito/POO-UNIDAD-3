from this import d
from turtle import st


class Carrera:
    __cod: int
    __nom: str
    __fechaini: st
    __dur: str
    __tit: str
    
    def __init__(self,cod,nom,fecha,dur,tit):
        self.__cod=int(cod)
        self.__nom=str(nom)
        self.__fechaini=str(fecha)
        self.__dur=str(dur)
        self.__tit=str(tit)
        