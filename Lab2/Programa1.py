from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion

def main():
    Fecha1 = Fecha(10, 10, 1999)
    Direccion1 = Direccion("68","51b-31","Sevilla", "Medellín", "piso 2", "")
    Jesus = Usuario("Jesus", 1003395952, Fecha1, "Montería", 3209467789, "jemunozm@unal.edu.co", Direccion1)
    print(Jesus)

main()