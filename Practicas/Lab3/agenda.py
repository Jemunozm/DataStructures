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
            for line in f:
                nombre, id, fecha_in, ciudad, tel, email, direccion_in = (
                    line.strip().split(",")
                )
                dia, mes, anio = map(int, fecha_in.split("-"))
                fecha = Fecha(dia, mes, anio)
                calle, nomenclatura, barrio, ciudad_dir, edificio, apto = (
                    direccion_in.split(" ")
                )
                direccion = Direccion(
                    calle, nomenclatura, barrio, ciudad_dir, edificio, apto
                )
                usuario = Usuario(nombre, int(id), fecha, ciudad, tel, email, direccion)
                self.agregar(usuario)


"""
user1 = Usuario(
    "Julián1",
    1152717436,
    Fecha(2, 6, 1999),
    "Medellín",
    1152717436,
    "jugallegog@unal.edu.co",
    "78 32-78 Belen Medellín Niagara 401",
)
user2 = Usuario(
    "Julián2",
    1152717437,
    Fecha(2, 6, 1999),
    "Medellín",
    1152717437,
    "jugallegog@unal.edu.co",
    "78 32-78 Belen Medellín Niagara 401",
)
user3 = Usuario(
    "Julián3",
    1152717438,
    Fecha(2, 6, 1999),
    "Medellín",
    1152717438,
    "jugallegog@unal.edu.co",
    "78 32-78 Belen Medellín Niagara 401",
)
user4 = Usuario(
    "Julián4",
    1152717439,
    Fecha(2, 6, 1999),
    "Medellín",
    1152717439,
    "jugallegog@unal.edu.co",
    "78 32-78 Belen Medellín Niagara 401",
)
user5 = Usuario(
    "Julián5",
    1152717431,
    Fecha(2, 6, 1999),
    "Medellín",
    1152717431,
    "jugallegog@unal.edu.co",
    "78 32-78 Belen Medellín Niagara 401",
)

agenda = Agenda(5)
agenda.agregar(user1)
agenda.agregar(user2)
agenda.agregar(user3)
agenda.agregar(user4)
agenda.agregar(user5)

user_id = 1152717436
position = agenda.buscar(user_id)
print(f"User with id {user_id} is at position {position} in the agenda.")

agenda.export_archivo("Agenda.txt")
"""

agenda = Agenda(5)
agenda.import_archivo("Agenda.txt")

for i in range(agenda.__no_reg):
    print(agenda[i])

user_id_eliminar = 1152717436
agenda.eliminar(user_id_eliminar)

agenda.export_archivo("Agenda2.txt")
