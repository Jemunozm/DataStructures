from Agenda import Agenda
from Usuario import Usuario
import os

def main():
    agenda = Agenda(5)
    agenda.agregar(Usuario("Jesus", 1003395952, "10/10/1999", "Montería", 3209467789, "jemunozm@unal.edu.co", "68, 51b-31, Sevilla, Medellín, piso 2, """))
    agenda.agregar(Usuario("Daniel", 1107520134, "5,9,2000", "Cali", 3113825465, "dsarmientov@unal.edu.co", "35, 65d-42, Conquistadores, Medellín, piso 6, SantAngelo"))
    agenda.agregar(Usuario("Diego", 4206969, "15,2,1999", "Medellín", 3105309854, "diegoa@unal.edu.co", "10, 80d-42, belen, Medellín, piso 3, owo"))
    agenda.agregar(Usuario("Emir", 10055625911, "1,6,2000", "Sincelejo", 3023271941, "eperef@unal.edu.co", "56, 25-84, Chagualo, Medellín, piso 6, Paseo de sevilla"))
    agenda.agregar(Usuario("Juan", 10042525911, "27,8,2000", "Boyacá", 3029461941, "Jmanrtinezp@unal.edu.co", "56, 25-84, Chagualo, Medellín, piso 15, Paseo de sevilla"))
    agenda.toFile("Agenda.txt")
    print(agenda.buscar(1003395952))
    agenda.eliminar(1003395952)
main()