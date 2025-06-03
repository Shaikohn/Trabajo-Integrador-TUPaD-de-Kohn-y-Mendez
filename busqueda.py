def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            print(f"El producto '{objetivo}' se encuentra en la posición {i}.")
            return i
    print(f"El producto '{objetivo}' no se encuentra en la lista.")
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            print(f"El producto '{objetivo}' se encuentra en la posición {medio} de la lista.")
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print(f"El producto '{objetivo}' no se encuentra en la lista.")
    return -1