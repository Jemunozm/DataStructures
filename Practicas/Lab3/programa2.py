from agenda import Agenda


def main():
    agenda = Agenda(5)
    agenda.import_archivo("Agenda.txt")

    for usuario in agenda:
        print(usuario)

    user_id_eliminar = 1152717436
    agenda.eliminar(user_id_eliminar)

    agenda.export_archivo("Agenda2.txt")


if __name__ == "__main__":
    main()
