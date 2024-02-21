from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion

def main():
    print("Ingrese la información personal del usuario y de contacto")
    nombre = input("Nombre: ")
    id = int(input("ID: "))
    print("Fecha de nacimiento")
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))
    fechaNacimiento = Fecha(dia, mes, anio)
    ciudadNacimiento = input("Ciudad de nacimiento: ")
    tel = int(input("Teléfono: "))
    email = input("Email: ")
    print("Dirección")
    calle = input("Calle: ")
    numero = int(input("Número: "))
    barrio = input("Barrio: ")
    ciudad = input("Ciudad: ")
    edifio = input("Edificio: ")
    apto = input("Apartamento: ")
    dir = Direccion(calle, numero, barrio, ciudad, edifio, apto)
    usuario = Usuario(nombre, id, fechaNacimiento, ciudadNacimiento, tel, email, dir)
    print(usuario)



main()