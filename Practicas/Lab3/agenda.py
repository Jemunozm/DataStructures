import sys

sys.path.append("/home/juliangallegog/Documents/Courses/DSA/Practicas/Lab2")

from usuario import Usuario
from fecha import Fecha
from direccion import Direccion


class Agenda:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__registro = [] * capacity
        self.__no_reg = 0

    def agregar(self, usuario: Usuario) -> bool:
        pass

    def buscar(self, id: int) -> int:
        pass

    def eliminar(self, id: int) -> bool:
        pass
