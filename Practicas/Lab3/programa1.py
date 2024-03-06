from agenda import Agenda
from usuario import Usuario
from fecha import Fecha


def main():
    user1 = Usuario(
        "Julián1",
        1152717436,
        Fecha(2, 6, 1999),
        "Medellín",
        1152717436,
        "jugallegog@unal.edu.co",
        "Carrera_78 #32-78 Belen Medellín Edificio_Niagara Apartamento_401",
    )
    user2 = Usuario(
        "Julián2",
        1152717437,
        Fecha(2, 6, 1999),
        "Medellín",
        1152717437,
        "jugallegog@unal.edu.co",
        "Carrera_78 #32-78 Belen Medellín Edificio_Niagara Apartamento_401",
    )
    user3 = Usuario(
        "Julián3",
        1152717438,
        Fecha(2, 6, 1999),
        "Medellín",
        1152717438,
        "jugallegog@unal.edu.co",
        "Carrera_78 #32-78 Belen Medellín Edificio_Niagara Apartamento_401",
    )
    user4 = Usuario(
        "Julián4",
        1152717439,
        Fecha(2, 6, 1999),
        "Medellín",
        1152717439,
        "jugallegog@unal.edu.co",
        "Carrera_78 #32-78 Belen Medellín Edificio_Niagara Apartamento_401",
    )
    user5 = Usuario(
        "Julián5",
        1152717431,
        Fecha(2, 6, 1999),
        "Medellín",
        1152717431,
        "jugallegog@unal.edu.co",
        "Carrera_78 #32-78 Belen Medellín Edificio_Niagara Apartamento_401",
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


if __name__ == "__main__":
    main()
