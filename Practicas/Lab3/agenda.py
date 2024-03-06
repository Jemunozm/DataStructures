from usuario import Usuario
from fecha import Fecha
from direccion import Direccion


class Agenda:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__registro = [] * capacity
        self.__no_reg = 0

    def __getitem__(self, index):
        return self.__registro[index]

    def agregar(self, usuario) -> bool:
        identification = usuario.getId()
        if self.__no_reg < self.__capacity and identification not in [
            user.getId() for user in self.__registro
        ]:
            self.__registro.append(usuario)
            self.__no_reg += 1
            return True
        return False

    def buscar(self, user_id) -> int:
        for i in range(self.__no_reg - 1):
            temp_id = self.__registro[i].getId()
            if temp_id == user_id:
                return i

    def eliminar(self, user_id) -> bool:
        id_search = self.buscar(id)
        if id_search is None:
            return False
        for i in range(id_search, self.__no_reg - 1):
            self.__registro[i] = self.__registro[i + 1]
        self.__no_reg -= 1
        return True

    def export_archivo(self, file_name):
        with open(file_name, "w") as f:
            for user in self.__registro:
                f.write(str(user) + "\n")

    def import_archivo(self, file_name):
        with open(file_name, "r") as f:
            for line in f:
                nombre, iden, fecha_in, ciudad, tel, email, direccion_in = (
                    line.strip().split(",")
                )

                dia, mes, anio = map(int, fecha_in.split("-"))
                fecha = Fecha(dia, mes, anio)

                calle, nomenclatura, barrio, ciudad_dir, edificio, edificio_apto = (
                    direccion_in.strip().split(" ")
                )
                direccion = Direccion(
                    calle, nomenclatura, barrio, ciudad_dir, edificio, edificio_apto
                )
                usuario = Usuario(
                    nombre, int(iden), fecha, ciudad, tel, email, direccion
                )
                self.__registro.append(usuario)
