# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:15:00 2024

@author: Dell
"""
'''
Se va a implementar la creacion de escuadrones, en la cual pueda realizar alguna que otra accion
Las acciones propuestas para grupos seran:
    Patrullaje
    Exploracion
    Investigacion
Estas acciones pueden extenderse a acciones mas complejas e agregar recursos o experiencia en base al tipo de accion realizada
Si es Exploracion puede haber mas recurso o algo por el estilo
Si es Investigacion, puede ser ganancia de mas experiencia
Pero por el momento se va a implementar solamente el cascaron de seleccion de enanos
Teniendo en el menu:
    Enanos Disponibles y los escuadrones ya formados
Groups sera un hash del nombre del escuadron y de su mision
se agregara un atributo a la clase personaje que determine si esta en un grupo o no
Se puede tener un hash de sets que almacene los personajes dentro de un grupo
para determinar su mision y eso
'''
def crear_grupo(todos, grupo, todos_grupo):
    print("Personajes Disponibles: ")
    disponibles = []
    i = 0
    for personaje in todos:
        if personaje not in todos_grupo:
            print(f"{i + 1} {personaje.simbolo} {personaje.tipo} {personaje.nombre}")
            disponibles.append(personaje)
            i += 1
            
    if i == 0:
        print ("No hay personajes disponibles")
        input("Presiona enter para continuar: ")
        return
    
    seleccion = input("Selecciona los numeros de los enanos para formar el escuadron (ejemplo '1345') o '0' para regresar: ")
    if seleccion == '0':
        return
    nuevo_grupo = set()
    nombre = ""
    tarea = ""
    for nEnano in seleccion:
        nuevo_grupo.add(disponibles[int(nEnano) - 1]) #se agrega al nuevo set del grupo
        todos_grupo.add(disponibles[int(nEnano) - 1]) #se agrega al set general de los grupos
    
    nombre = input("Ingresa el nuevo nombre de tu grupo: ")
    print("1. Patrullar")    
    print("2. Explorar")   
    print("3. Investigar")
    
    tarea = input("Selecciona una tarea para tu escuadron: ")
    
    print(f"Grupo: {nombre} con tarea {tarea} sea creado con exito")
    
    grupo[nombre] = (nuevo_grupo, tarea)
    return
       
    
            
def menu_grupo(todos, grupo, todos_grupo):
    #imprimimos a los miembros del grupo
    if grupo:
        for nombre, escuadron in grupo:
            print(nombre, f"  Mision: {escuadron[1]}")
            for miembro in escuadron[0]:
                print(miembro.show_name)
        print("-------------------------------------------")
    else:
        print("Aun no hay grupos formados\n")
        
        
    print("1. Crear un Nuevo grupo")   
    print("0. Salir") 
    op = int(input("Selecciona una Opcion: "))
    
    if op == 1:
        crear_grupo(todos, grupo, todos_grupo)
    
    else:
        return
    
        
    