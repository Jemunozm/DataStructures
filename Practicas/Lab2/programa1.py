from usuario import Usuario
from fecha import Fecha
from direccion import Direccion


def main():
    Fecha1 = Fecha(2, 6, 1999)
    Direccion1 = Direccion("78", "32-78", "Belén", "Medellín", "Niágara", "401")
    Julian_data = Usuario(
        "Julián",
        11527717436,
        Fecha1,
        "Bello, Antioquia",
        3114290433,
        "jugallegog@unal.edu.co",
        Direccion1,
    )
    return print(Julian_data)


if __name__ == "__main__":
    main()
