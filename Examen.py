# Evalución de Joicer Blanco y Nelson Cordoba
# Sobre Diccionarios..😎


#Creamos Diccionario
futbolistas = {"Messi": "Argentina", 
                "Ronaldo": "Portugal",
                "James": "Colombia",
                "Neymar": "Brasil",
                "Maradona":"Argentina",
                "Pele": "Brasil",
                "Modric":"Croacia",
                "Falcao":"Colombia",
                "Cuadrado":"Colombia",
                "Kross":"Alemania",
                "Benzema":"Francia"}
#Con este ciclo for lo ordenamos
for nombre,pais in futbolistas.items():
    print(f"{nombre} -> {pais}")
    
#Con este ciclo while True creamos las opciones para el usuario
while True:
    print("1. Agregar")
    print("2. Buscar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")
    
    opcion = input("Ingrese Opcion:")
    #Agregar 
    if opcion == "1":
        #
        nombre = input("Ingrese el nombre: ")
        pais = input("Ingrese el pais:")
        
        futbolistas[nombre] = pais
        
    #Buscar
    elif opcion == "2":
        nombre = input("Ingrese el futbolista que va buscar: ")
        
        if nombre in futbolistas:
            pais= futbolistas[nombre]
            print(f"El futbolista que busco es {nombre} y su pais es {pais}")
            
        else:
            print("El futbolista no existe")
            
        #Actualizar
    elif opcion == "3":
        nombre = input("Ingrese el pais del futbolista que va actualizar: ")
        pais = input("Ingrese el nombre del futbolista que va actualizar: ")
        
        nuevo_nombre = input("Nuevo pais del futbolista")
        nuevo_pais = input("Nuevo nombre del futbolista")
        
        futbolistas[nombre] = nuevo_pais
        print(f"El futbolista que actualizo es {nuevo_nombre} y su pais es {nuevo_pais}")
        
        #Eliminar
    elif opcion == "4":
        nombre_eliminar = input("Ingrese el nombre del futbolista que va eliminar: ")
        if nombre_eliminar in futbolistas:
            futbolistas.pop(nombre_eliminar)
        else:
            print ("El futbolista no existe")
        
        
    elif opcion == "5":
        break
    
    else:
        print("Error opcion no valida")
                
        
        
    for nombre, pais in futbolistas.items():
        print(f"{nombre} -> {pais}")
        
    
    

