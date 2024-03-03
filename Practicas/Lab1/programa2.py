def lectura_archivo(file_path):
    """
    Lee un archivo y devuelve las lineas .

    Args:
        file_path (str): Ruta completa del archivo.

    Retorna:
        list: Una lista con todas las lineas presentes en el archivo.
    """
    with open(file_path, "r", encoding="utf-8") as archivo:
        lineas = [linea.strip() for linea in archivo]
    return lineas


def split_linea(lineas, palabra_buscada):
    """
    Separa cada linea en palabras y cuenta la ocurrencia de una palabra requerida.

    Args:
        lineas (list): Lista de lineas presentes en el texto.
        palabra_buscada (str): Palabra a buscar en el texto.

    Retorna:
        int: Número de ocurrencias de la palabra.
    """
    contador_palabra = 0
    for linea in lineas:
        for palabra in linea.split():
            if palabra == palabra_buscada:
                contador_palabra += 1
    return contador_palabra


def main(file_path):
    """
    Funcion principa para unir las anteriores

    Args:
        file_path (str): Ruta completa del archivo de texto.

    Retorna:
        int: Conteo de ocurrencias de la palabra en.
    """
    contador = split_linea(lectura_archivo(file_path), "el")
    return print("La palabra 'en' aparece {} veces en el archivo.".format(contador))


path = input(str("Ingrese el path del archivo: "))

main(path)
