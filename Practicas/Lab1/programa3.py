def main(diccionario_usuarios: dict):
    """
    Busca autentificar los datos de usuario y contraseña ingresados por un usuario.

    Args:
        diccionario_usuarios (dict): Diccionario que contiene los datos de acceso correctos de los usuarios.

    Devuelve:
        String especificando si el acceso fue permitido o no.
    """
    conteo_intentos = 0
    while conteo_intentos < 3:
        usuario = str(input("Ingrese su usuario: "))
        password = str(input("Ingrese su contraseña: "))
        if (usuario, password) in diccionario_usuarios.items():
            return print("Acceso permitido")
        else:
            print("Datos incorrectos")
            conteo_intentos += 1
    print("Lo siento, su acceso no está permitido")


diccionario_usuarios = {
    "Juan1223": "J12an*.",
    "Maria2345": "M23a*.",
    "Pablo1459": "P14o*.",
    "Ana3456": "A34a*.",
}

main(diccionario_usuarios)
