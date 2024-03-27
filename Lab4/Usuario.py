from Direccion import Direccion
from Fecha import Fecha


class Usuario:
    def __init__(self, nombre=str, id=int, fechaNacimiento=(Fecha), ciudadNacimiento=None, tel=int, email=str, dir=(Direccion)):
        self.nombre = nombre
        self.id = id
        self.fechaNacimiento = fechaNacimiento
        self.ciudadNacimiento = ciudadNacimiento
        self.tel = tel
        self.email = email
        self.dir = dir

    def setNombre(self, n:str):
        self.nombre = n

    def setId(self, id:int):
        self.id = id

    def setFechaNacimiento(self, f):
        self.fechaNacimiento = f

    def setCiudadNacimiento(self, c):
        self.ciudadNacimiento = c

    def setTel(self, t):
        self.tel = t

    def setEmail(self, e):
        self.email = e
        
    def setDir(self, d):
        self.dir = d



    def getNombre(self):
        return self.nombre
    def getId(self):
        return self.id
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    def getCiudadNacimiento(self):
        return self.ciudadNacimiento
    def getTel(self):
        return self.tel
    def getEmail(self):
        return self.email
    def getDir(self):
        return self.dir
    def __str__(self):
        return f"{self.nombre} {self.id} {self.fechaNacimiento} {self.ciudadNacimiento} {self.tel} {self.email} {self.dir}"
