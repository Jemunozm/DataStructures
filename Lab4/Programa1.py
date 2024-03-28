from ListDouble import ListDouble

def main():

    NumerosPares = ListDouble()
    for i in range(2, 21, 2):
        NumerosPares.addFirst(i)
    NumerosPares.removeFirst()
    NumerosPares.delete(10)

    print("Lista de números pares:")
    print(NumerosPares)

main()