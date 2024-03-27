from Agenda import Agenda

def main():
  nueva_agenda = Agenda(5)
  nueva_agenda.importU("Agenda.txt")
  nueva_agenda.eliminar(1003395952)
  nueva_agenda.toFile("Agenda2.txt")
  print(nueva_agenda)
main()