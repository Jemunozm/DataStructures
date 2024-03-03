def generar_lista():
    """
    Solicita al usuario la cantidad de números enteros que desea ingresar y luego
    solicita esos números enteros. Retorna una lista con los números ingresados.
    """
    cantidad_enteros = int(
        input("Ingrese la cantidad de números enteros que desea ingresar: ")
    )
    lista_enteros = []
    for _ in range(cantidad_enteros):
        numero = int(input("Ingrese un número entero: "))
        lista_enteros.append(numero)
    return lista_enteros


def valor_maximo(lista):
    """
    Retorna el valor máximo de una lista de números enteros.
    """
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo


def valor_minimo(lista):
    """
    Retorna el valor mínimo de una lista de números enteros.
    """
    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo


def suma_enteros(lista):
    """
    Retorna la suma de los valores de una lista de números enteros.
    """
    suma = 0
    for i in lista:
        suma += i
    return suma


def valor_promedio(lista):
    """
    Retorna el promedio de los valores de una lista de números enteros.
    """
    suma = suma_enteros(lista)
    longitud_lista = 0
    for i in range(len(lista)):
        longitud_lista += 1
    promedio = suma / longitud_lista
    return promedio


def main():
    """
    Función principal del programa. Genera una lista de números enteros,
    calcula y muestra el valor máximo, el valor mínimo, la suma y el promedio
    de los valores de la lista.
    """
    lista = generar_lista()
    print(f"El valor máximo de la lista es: {valor_maximo(lista)}")
    print(f"El valor mínimo de la lista es: {valor_minimo(lista)}")
    print(f"La suma de los valores de la lista es: {suma_enteros(lista)}")
    print(f"El promedio de los valores de la lista es: {valor_promedio(lista)}")


main()
