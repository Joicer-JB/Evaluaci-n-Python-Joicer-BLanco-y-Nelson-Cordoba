# Evalución de Joicer Blanco y Nelson Cordoba
# Sobre Diccionarios..😎

# Creamos un diccionario
futbolistas = {
    "Messi": "Argentina",
    "Ronaldo": "Portugal",
    "James": "Colombia",
    "Neymar": "Brasil",
    "Maradona": "Argentina",
    "Pele": "Brasil",
    "Modric": "Croacia",
    "Falcao": "Colombia",
    "Cuadrado": "Colombia",
    "Kross": "Alemania",
    "Benzema": "Francia"
}

# Creamos el siclo while para darle las opciones al usuario
while True:
    print("1. Agregar")
    print("2. Buscar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")
    
    opcion = input("Ingrese Opcion: ")

    #Agregar
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        pais = input("Ingrese el pais: ")
        futbolistas[nombre] = pais
        print(f"{nombre} -> {pais} agregado correctamente.")
        
        
        
        
    #Buscar
    elif opcion == "2":
        nombre = input("Ingrese el futbolista que desea buscar: ")
        if nombre in futbolistas:
            pais = futbolistas[nombre]
            print(f"El futbolista que busca es {nombre} y su país es {pais}")
        else:
            print("El futbolista no existe")
            
            
            
            
    #Actualizar
    elif opcion == "3":
        nombre = input("Ingrese el nombre del futbolista que desea actualizar: ")
        if nombre in futbolistas:
            nuevo_nombre = input("Nuevo nombre del futbolista: ")
            nuevo_pais = input("Nuevo país del futbolista: ")
            futbolistas[nuevo_nombre] = nuevo_pais
            del futbolistas[nombre]
            print(f"El futbolista se actualizó a {nuevo_nombre} -> {nuevo_pais}")
        else:
            print("El futbolista no existe")
            
            
            
    #Eliminar
    elif opcion == "4":
        nombre_eliminar = input("Ingrese el nombre del futbolista que desea eliminar: ")
        if nombre_eliminar in futbolistas:
            del futbolistas[nombre_eliminar]
            print(f"{nombre_eliminar} eliminado correctamente.")
        else:
            print("El futbolista no existe")
            
            
    #Salir del programa
    elif opcion == "5":
        break

    else:
        print("Error: Opción no válida")

    # Mostrar la lista de futbolistas 
    for nombre, pais in futbolistas.items():
        print(f"{nombre} -> {pais}")
