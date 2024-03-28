from ListDouble import ListDouble
from Usuario import Usuario

def main():
    UsuariosList = ListDouble()
    UsuariosList.addFirst(Usuario("Jesus", 1003395952, "10/10/1999", "Montería", 3209467789, "jemunozm@unal.edu.co", "68, 51b-31, Sevilla, Medellín, piso 2, """))
    UsuariosList.addFirst(Usuario("Daniel", 1107520134, "5,9,2000", "Cali", 3113825465, "dsarmientov@unal.edu.co", "35, 65d-42, Conquistadores, Medellín, piso 6, SantAngelo"))
    UsuariosList.addFirst(Usuario("Diego", 4206969, "15,2,1999", "Medellín", 3105309854, "diegoa@unal.edu.co", "10, 80d-42, belen, Medellín, piso 3, owo"))
    UsuariosList.addFirst(Usuario("Emir", 10055625911, "1,6,2000", "Sincelejo", 3023271941, "eperef@unal.edu.co", "56, 25-84, Chagualo, Medellín, piso 6, Paseo de sevilla"))
    UsuariosList.addFirst(Usuario("Juan", 10042525911, "27,8,2000", "Boyacá", 3029461941, "Jmanrtinezp@unal.edu.co", "56, 25-84, Chagualo, Medellín, piso 15, Paseo de sevilla"))
    print(UsuariosList)

    nombre = input("Ingrese el nombre de usuario: ")
    id = int(input("Ingrese el id del usuario: "))
    fecha = input("Ingrese la fecha de nacimiento del usuario: ")
    ciudad = input("Ingrese la ciudad del usuario: ")
    telefono = int(input("Ingrese el telefono del usuario: "))
    email = input("Ingrese el email del usuario: ")
    direccion = input("Ingrese la dirección del usuario: ")
    UsuariosList.addFirst(Usuario(nombre, id, fecha, ciudad, telefono, email, direccion))

    nombre = input("Ingrese el nombre de usuario: ")
    id = int(input("Ingrese el id del usuario: "))
    fecha = input("Ingrese la fecha de nacimiento del usuario: ")
    ciudad = input("Ingrese la ciudad del usuario: ")
    telefono = int(input("Ingrese el telefono del usuario: "))
    email = input("Ingrese el email del usuario: ")
    direccion = input("Ingrese la dirección del usuario: ")
    UsuariosList.addLast(Usuario(nombre, id, fecha, ciudad, telefono, email, direccion))

    print(UsuariosList)

    if isinstance(UsuariosList, ListDouble):
        id = int(input("Ingrese el id del usuario a insertar despues del tercero: "))
        nombre = input("Ingrese el nombre del usuario a insertar despues del tercero: ")
        fecha = input("Ingrese la fecha de nacimiento del usuario a insertar despues del tercero: ")
        ciudad = input("Ingrese la ciudad del usuario a insertar despues del tercero: ")
        telefono = int(input("Ingrese el telefono del usuario a insertar despues del tercero: "))
        email = input("Ingrese el email del usuario a insertar despues del tercero: ")
        direccion = input("Ingrese la dirección del usuario a insertar despues del tercero: ")

        posicion = 1
        nodeChosen = UsuariosList.first()
        while nodeChosen != None:
            if posicion == 3:
                UsuariosList.addAfter(nodeChosen, Usuario(nombre, id, fecha, ciudad, telefono, email, direccion))
                break
            nodeChosen = nodeChosen.getNext()
            posicion += 1
        print(UsuariosList)

main()
        