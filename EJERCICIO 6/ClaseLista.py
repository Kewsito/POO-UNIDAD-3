from ClaseNodo import Nodo
from zope.interface import implementer
from Interfaz import Interfaz


@implementer(Interfaz)
class Lista:
    __comienzo: None
    __actual: None
    __ind: None
    __tope: None

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            valor=self.__actual.getvalor()
            self.__actual=self.__actual.getsiguiente()
            return valor

    def InsElem(self,pos,obj):
        cont=1
        cabeza=self.__comienzo
        if self.__comienzo is None:
            nodo = Nodo(obj)
            nodo.setsiguiente(self.__comienzo)


