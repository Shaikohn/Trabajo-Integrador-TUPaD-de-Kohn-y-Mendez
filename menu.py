import busqueda, ordenamiento, listas

bebidas = listas.bebidas
alimentos = listas.alimentos
herramientas = listas.herramientas

# Menu principal del programa
def menu():
    print("Menu de inicio")
    print("1. Ordenar una lista")
    print("2. Buscar un elemento en una lista")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    # Se obliga al usuario a seleccionar una opción válida
    while opcion not in ["1", "2", "3"]:
        print("Opción no válida. Intente de nuevo.")
        opcion = input("Seleccione una opción: ")
    if opcion == "1":
        menu_ordenamiento()
    elif opcion == "2":
        menu_busqueda()
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        return

# Submenu de ordenamiento
def menu_ordenamiento():
    print("Seleccione la lista a ordenar:")
    print("1. Bebidas")
    print("2. Alimentos")
    print("3. Herramientas")
    lista_opcion = input("Seleccione una opción: ")
    # Se obliga al usuario a seleccionar una opción válida
    while lista_opcion not in ["1", "2", "3"]:
        print("Opción no válida. Intente de nuevo.")
        lista_opcion = input("Seleccione una opción: ")
    if lista_opcion == "1":
        seleccion_de_ordenamiento_segun_length(bebidas)
    elif lista_opcion == "2":
        seleccion_de_ordenamiento_segun_length(alimentos)
    elif lista_opcion == "3":
        seleccion_de_ordenamiento_segun_length(herramientas)

# Submenu de busqueda
def menu_busqueda():
    print("Seleccione la lista en la que buscar:")
    print("1. Bebidas")
    print("2. Alimentos")
    print("3. Herramientas")
    lista_opcion = input("Seleccione una opción: ")
    while lista_opcion not in ["1", "2", "3"]:
        print("Opción no válida. Intente de nuevo.")
        lista_opcion = input("Seleccione una opción: ")
    # Se obliga al usuario a ingresar un producto a buscar
    producto_a_buscar = input("Ingrese el producto a buscar: ")
    while not producto_a_buscar:
        print("El producto no puede estar vacío. Intente de nuevo.")
        producto_a_buscar = input("Ingrese el producto a buscar: ")

    if lista_opcion == "1":
        seleccion_de_busqueda_segun_length(bebidas, producto_a_buscar)
    elif lista_opcion == "2":
        seleccion_de_busqueda_segun_length(alimentos, producto_a_buscar)
    elif lista_opcion == "3":
        seleccion_de_busqueda_segun_length(herramientas, producto_a_buscar)

# Funcion para seleccionar el tipo de ordenamiento según la longitud de la lista
def seleccion_de_ordenamiento_segun_length(lista):
    # Si la lista tiene menos de 10 elementos, se utiliza bubble sort
    if len(lista) < 10:
        ordenamiento.bubble_sort(lista)
        print(lista)
    else:
        # Si la lista tiene 10 o más elementos, se utiliza quicksort
        lista_ordenada = ordenamiento.quicksort(lista)
        print(lista_ordenada)

# Funcion para seleccionar el tipo de busqueda según la longitud de la lista
def seleccion_de_busqueda_segun_length(lista, producto):
    # Si la lista tiene menos de 10 elementos, se utiliza busqueda lineal
    if len(lista) < 10:
        busqueda.busqueda_lineal(lista, producto)
    else:
        # Se ordena la lista antes de realizar la busqueda binaria
        lista_ordenada = ordenamiento.quicksort(lista)
        busqueda.busqueda_binaria(lista_ordenada, producto)