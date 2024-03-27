from Usuario import Usuario
class Agenda:
    def __init__(self, cantidad:int):
        self._registro = []
        self._no_registros = 0;   
        self._cantidad = cantidad
    
    def buscar(self, id:int):
        data = 0
        while data < len(self._registro):
            if self._registro[data].getId() == id:
                return data
            data += 1
        return -1
    
    def agregar(self, usuario:Usuario):
        if (self.buscar(usuario.getId()) == -1) and (self._no_registros < self._cantidad):
            self._registro.append(usuario)
            self._no_registros += 1
            return True
        else:  
            return False
    def eliminar(self, id:int):
        if self.buscar(id) != -1:
            posicion = self.buscar(id)
            temp = self._registro[posicion]
            self._registro[posicion] = None
            self._no_registros -= 1
            for posicion in range(posicion, self._no_registros,posicion+1):
                self._registro[posicion] = self._registro[posicion+1]
            self._registro[-1] = None
            return print(f"Se ha eliminado el usuario {temp.getNombre()}")
        else:
            return False
        
    def toFile(self, archivo:str):
        file = open(archivo, "w")
        for i in range(self._no_registros):
            file.write(self._registro[i].getNombre() + " " + str(self._registro[i].getId()) + " " + str(self._registro[i].getFechaNacimiento()) + " " + self._registro[i].getCiudadNacimiento() + " " + str(self._registro[i].getTel()) + " " + self._registro[i].getEmail() + " " + str(self._registro[i].getDir()) + "\n")
        file.close()
    def importU(self, archivo:str):
        with open(archivo, "r") as file:
            for line in file:
                datosUsuario = line.strip().split(" ")
                nombre = datosUsuario[0]
                id = int(datosUsuario[1])
                fechaNacimiento = datosUsuario[2]
                ciudadNacimiento = datosUsuario[3]
                tel = int(datosUsuario[4])
                email = datosUsuario[5]
                dir = datosUsuario[6]
                usuario = Usuario(nombre, id, fechaNacimiento, ciudadNacimiento, tel, email, dir)
                self.agregar(usuario)