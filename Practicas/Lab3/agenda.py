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
        if usuario not in self.__registro and self.__no_reg < self.__capacity:
            self.__registro[self.__no_reg + 1] = usuario
        else:
            print("No fue posible agregar el usuario")
            return False

    def buscar(self, id: int) -> int:
        for i in range(self.__no_reg):
            if self.__registro[i] == id:
                return i
        if id not in self.__registro:
            return int("-1")

    def eliminar(self, id: int) -> bool:
        pass

    def toFile():
        for i in range(self.__no_reg):
            with open("agenda.txt", "a") as f:
                f.append(self.__registro[i] + "\n")

    def importt():
        with open("agenda.txt", "r") as f:
            for line in f.read():
                agregar(line)
