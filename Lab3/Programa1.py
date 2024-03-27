from Agenda import Agenda

def main():
    agenda = Agenda(5)
    agenda.agregar("Jesus", 1003395952, "10/10/1999", "Montería", 3209467789, "jemunozm@unal.edu.co", "68","51b-31","Sevilla", "Medellín", "piso 2", "")
    agenda.agregar("Daniel", 1107520134, "05/09/2000", "Cali", 3113825465, "dsarmientov@unal.edu.co", "35","65d-42","Conquistadores", "Medellín", "piso 6", "SantAngelo")
    agenda.agregar("Diego", 4206969, "15/2/1999", "Medellín", 3105309854, "diegoa@unal.edu.co", "10","80d-42","belen", "Medellín", "piso 3", "owo")
    agenda.agregar("Emir", 10055625911, "1/6/2000", "Sincelejo", 3023271941, "eperef@unal.edu.co", "56", "25-84", "Chagualo", "Medellín", "piso 6", "Paseo de sevilla")
    agenda.agregar("Juan", 10042525911, "27/8/2000", "Boyacá", 3029461941, "Jmanrtinezp@unal.edu.co", "56", "25-84", "Chagualo", "Medellín", "piso 15", "Paseo de sevilla")
    print(agenda.buscar(1003395952))
    agenda.toFile("Agenda.txt")

main()