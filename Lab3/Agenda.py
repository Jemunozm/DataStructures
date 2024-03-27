from ..Lab2.Usuario import Usuario
from typing import List
class Agenda:
    def __init__(self, cantidad:int):
        self._registro = []
        self._no_registros = 0;   
        self._cantidad = cantidad
    
    def buscar(self, id:int):
        for i in range(len(self._registro)):
            if self._registro[i].getId() == id:
                return int(i)
            else :
                return int(-1)
    
        return None
    
    def agregar(self, usuario:Usuario):
        if self.buscar(usuario.getId()) == -1 and self._no_registros < self._cantidad:
            self._registro.append(usuario)
            self._no_registros += 1
            return True
        else:  
            return False
    def eliminar(self, id:int):
        if self.buscar(id) != -1:
            posicion = self.buscar(id)
            temp = self._registro.append(posicion)
            self._registro.remove(posicion)
            self._no_registros -= 1
            for espacioVacio in range(espacioVacio, self._no_registros,espacioVacio+1):
                self._registro[espacioVacio] = self._registro[espacioVacio+1]
            self._registro[-1] = None
            self._no_registros -= 1
            return True
        else:
            return False
        
    def toFile(self, archivo:str):
        file = open(archivo, "w")
        for i in range(self._no_registros):
            file.write(self._registro[i]+ "\n")
            #file.write(self._registro[i].Usuario() + "\n")
            #file.write(self._registro[i].getNombre() + " " + str(self._registro[i].getId()) + " " + str(self._registro[i].getFechaNacimiento()) + " " + self._registro[i].getCiudadNacimiento() + " " + str(self._registro[i].getTel()) + " " + self._registro[i].getEmail() + " " + str(self._registro[i].getDir()) + "\n")
        file.close()
    def importU(self):
        file = open("Agenda.txt", "r")
        for line in file:
            self._registro.append(line)
            self._no_registros += 1
        file.close()