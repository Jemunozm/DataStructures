import re

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
        id_search = self.buscar(user_id)
        for i in range(id_search, self.__no_reg - 1):
            if self.__registro[i].getId() == user_id:
                self.__registro.pop(i)
                self.__no_reg -= 1
                return True
        return False

    def export_archivo(self, file_name):
        with open(file_name, "w") as f:
            for user in self.__registro:
                f.write(str(user) + "\n")

    def import_archivo(self, file_name):
        with open(file_name, "r") as f:
            # Count the number of lines to initialize the Agenda
            num_lines = sum(1 for line in f)
            self.usuarios = [None] * num_lines
            f.seek(0)  # Reset the file pointer to the beginning

            line_number = 0
            for line in f:
                nombre, id, fecha_in, ciudad, tel, email, direccion_in = (
                    line.strip().split(",")
                )

                dia, mes, anio = map(int, fecha_in.split("-"))
                fecha = Fecha(dia, mes, anio)

                # Use regular expressions to extract address parts
                address_pattern = r"^(\w+)\s+(\d+[a-zA-Z]?)\s*([-#]\d+)?\s*(\w+)?\s*(\w+)?\s*(\w+)\s*(\w+\s\w+)?$"
                match = re.match(address_pattern, direccion_in)

                if match:
                    (
                        calle,
                        nomenclatura,
                        numero,
                        barrio,
                        ciudad_dir,
                        edificio,
                        edificio_apto,
                    ) = match.groups()
                    if edificio_apto:
                        edificio, apto = edificio_apto.split()
                    else:
                        apto = ""
                    direccion = Direccion(
                        calle,
                        nomenclatura,
                        numero,
                        barrio,
                        ciudad_dir or "",
                        edificio,
                        apto,
                    )
                else:
                    # Handle cases where the address doesn't match the expected pattern
                    direccion = Direccion("", "", "", "", "", "", "")

                usuario = Usuario(nombre, int(id), fecha, ciudad, tel, email, direccion)
                self.usuarios[line_number] = usuario
                line_number += 1
