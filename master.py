import mapa_consola as m_c
import razas
import animales
import terrenos_y_materiales as tm
import gestor_acciones
import Story_gen as st
import story_generator as sg
import Friendship_Gen as fg
from Pilas import Stack
import queue 
import os
import keyboard
from tabulate import tabulate
import time
import random
from itertools import count
import sys
import Grafos as gf
#sys.stdout.reconfigure(encoding='utf-8')

contador = count()  # Generador de índices únicos

def extraer_poblacion(mapa):
    poblacion = queue.deque()
    allPobl = [] #"Para poder iterar a toda la poblacion"
    edificaciones = queue.deque()
    
    for linea in mapa:
        for item in linea:
            if isinstance(item, razas.Enano):
                poblacion.append(item)
                allPobl.append(item)
            elif isinstance(item, razas.Humano) or isinstance(item, razas.Elfo)  or isinstance(item, razas.Orco) or isinstance(item, razas.Goblin) or isinstance(item, razas.Trol):
                allPobl.append(item) 
    #si el item es igual a un personaje, se agrega a una lista de personajes que contiene a todos
    return poblacion, allPobl

def mostrar_poblacion(poblacion):
    data_transpuesta = []

    for atributo in ["Símbolo Nombre", "Salud", "Oficio"]:
        fila = []
        for persona in poblacion:
            if atributo == "Símbolo Nombre":
                valor = f"{persona.simbolo} {persona.nombre}"
            elif atributo == "Salud":
                valor = persona.salud_estado
            else:
                valor = f"{persona.oficio_principal[0]} {persona.oficio_principal[1]}"
            fila.append(valor)
        data_transpuesta.append(fila)

    # print(tabulate(data_transpuesta, tablefmt="fancy_grid", stralign="CENTER"))
    print(tabulate(data_transpuesta, stralign="CENTER"))
    


prioridad_acciones = {
    'Atacar': 1,
    'Agua': 2,
    'Alimento': 3,
    'Talar': 4,
    'Minar': 5,
    'Comerciar': 6,
    'Domesticar': 7
}

def insertar_con_prioridad(acciones_a_realizar, colonia):
    for enano, accion in acciones_a_realizar:
        prioridad = prioridad_acciones.get(accion, 10)  # 10 como valor por defecto si la acción no está en el diccionario
        index = next(contador)
        colonia.put((prioridad, index, [enano, accion]))
 

pausa = False
una_vez = True
salir = False
def cambio_pausa():
    global pausa, una_vez
    pausa = not pausa
    una_vez = True

def terminar():
    global salir
    salir = True

def mostrar_colonia():
    # print("Acciones en la Priority Queue: ", list(colonia.queue))
    print("Acciones en la Priority Queue: ", end="")
    for p, i, data in list(colonia.queue):
        print(f"{p} - {data[0].nombre} -> {data[1]}", end=", ")
    
    print()
    
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
    
    seleccion = input("Selecciona los numeros de los enanos para formar el escuadron (ejemplo '1,3,4,5') o '0' para regresar: ")
    if seleccion == '0':
        return
    nuevo_grupo = set()
    nombre = ""
    tarea = ""
    new = seleccion.split(",")
    for nEnano in new:
        nuevo_grupo.add(disponibles[int(nEnano) - 1]) #se agrega al nuevo set del grupo
        todos_grupo.add(disponibles[int(nEnano) - 1]) #se agrega al set general de los grupos
    
    nombre = input("Ingresa el nuevo nombre de tu grupo: ")
    print("1. Patrullar")    
    print("2. Explorar")   
    print("3. Investigar")
    
    op = int(input("Selecciona una tarea para tu escuadron: "))
    if op == 1:
        tarea = "Patrullar"
    if op == 2:
        tarea = "Explorar"
    if op == 3:
        tarea = "Investigar"
    
    print(f"Nuevo Grupo: {nombre} para {tarea} sea creado con exito")
    input("Presiona enter para continuar ")
    
    grupo[nombre] = (nuevo_grupo, tarea)
    return
       
    
            
def menu_grupo(todos, grupo, todos_grupo):
    #imprimimos a los miembros del grupo
    if grupo:
        for nombre, escuadron in grupo.items():
            print(nombre, f"  Mision: {escuadron[1]}")
            for miembro in escuadron[0]:
                print(miembro.show_name())
        print("-------------------------------------------")
    else:
        print("Aun no hay grupos formados\n")
        
        
    print("1. Crear un Nuevo grupo")   
    print("0. Salir") 
    op = int(input("Selecciona una Opcion: "))
    
    if op == 1:
        os.system('cls')
        crear_grupo(todos, grupo, todos_grupo)
    
    else:
        return

def menu_acciones(buffer_acciones, todos, grupo, todos_grupo):  
    opcion = 0
        
    mostrar_colonia()
    
    while opcion != -1:
        print("Buffer de Acciones: ", buffer_acciones, end="\n")
        #for i in todos:
            
           # print(i.nombre)
        print("1. Recolectar: \t\t6. Comerciar \t7. Domesticar \t8. Atacar")    
        print("\t1.2: Agua")
        print("\t1.3: Talar")
        print("\t1.4: Cazar/Pezcar/Piscar")
        print("\t1.5: Minar")
        print("9. Ver Red Social")
        print("10. Ver Historial")
        print("11. Grupos")
        print("0. Regresar")
        opcion = input("Ingrese Opción: ")
        
        if opcion == '2':
            buffer_acciones.append('Agua')
        elif opcion == '3':
            buffer_acciones.append('Talar')
        elif opcion == '4':
            buffer_acciones.append('Alimento')
        elif opcion == '5':
            buffer_acciones.append('Minar')
        elif opcion == '6':
            buffer_acciones.append('Comerciar')
        elif opcion == '7':
            buffer_acciones.append('Domesticar')
        elif opcion == '8':
            buffer_acciones.append('Atacar')
        elif opcion == '9':
            #menu_enanos(todos)
            gf.plot_social_net(todos)
            input("Presiona enter para continuar")
        elif opcion == '10':
            os.system('cls')
            historial.printStack()
            input("Presiona enter para regresar")
            os.system('cls')
            m_c.imprimir_mapa_consola(mapa, mascara)
            print("                                                                                          ")
            
            print("                                                                                          ") 
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
        elif opcion == '11':
            os.system('cls')
            menu_grupo(todos, grupo, todos_grupo)
            os.system('cls')
            m_c.imprimir_mapa_consola(mapa, mascara)
            print("                                                                                          ")
            
            print("                                                                                          ") 
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
            print("                                                                                          ")
        elif opcion == '0':
            break
        print("\033[F" * 11, end="")  # Mueve el cursor 8 líneas hacia arriba
        
    
def menu_enanos(todos):
    op = 0
    while op != -1:
        os.system('cls')
        print("Enanos:", end="\n")
        i = 0
        for enano in todos:
            print(f"{i + 1}. {enano.nombre}")
            i += 1
            
        print("0. Regresar")  
        op = int(input("Selecciona un enano: "))
        if op == 0:
            break;
        else:
            os.system('cls')
            
            print(todos[op - 1].show_name())
            print(todos[op - 1].show_amigos())
            print(todos[op -1].show_enemigos())
            
            input("Presiona enter para regresar")
    
    os.system('cls')
    m_c.imprimir_mapa_consola(mapa, mascara)
    print("Buffer de Acciones: ", buffer_acciones, end="\n")
    
    print("1. Recolectar: \t\t6. Comerciar \t7. Domesticar \t8. Atacar")    
    print("\t1.2: Agua")
    print("\t1.3: Talar")
    print("\t1.4: Cazar/Pezcar/Piscar")
    print("\t1.5: Minar")
    print("9. Ver enanos")
    print("10. Ver Historial")
    print("0. Regresar")
    
    

ejecutando = False
def ejecutar():
    global ejecutando
    ejecutando = True


# def ejecuta_accion(enano, accion):
#     gestor_acciones.reproducir_animacion(enano, accion)
    
#     return enano

def posicion_enano(enano, mascara):
    for x, fila in enumerate(mascara):
        for y, elemento in enumerate(fila):
            if elemento == enano:
                return x, y
    return None  # Retorna None si no se encuentra


tipo_recurso = {
    'Agua': [tm.Agua()],
    'Talar': [tm.Arbol(), tm.Pino()],
    'Alimento': [tm.Fresa(), tm.Mango(), tm.Manzana(), tm.Naranja(), 
                 tm.Sandia(), tm.Trigo(), tm.Uva()],
    'Minar': [tm.Montana(), tm.Tierra(), tm.Lodo()],
    'Comerciar': [razas.Elfo(), razas.Humano(), razas.Mago()],
    'Domesticar': animales.lista_animales(),
    'Atacar': [razas.Goblin(), razas.Orco(), razas.Trol()],
    }


acciones = ["Agua", 
            "Talar",
            "Alimento", 
            "Minar",
            "Domesticar",
            "Atacar"]
            

    
def ejecuta_accion(enano, accion, mapa, mascara, todos): 
    t_recurso = tipo_recurso[accion]
    # t_recurso = t_recurso[0]
    t_recurso = random.choice(t_recurso)
    if not t_recurso:
        print(f"Acción desconocida: {accion}")
        return enano
    op = 0;
    amigos = []
    for key , amigo in enano.friends.items( ):
        amigos.append(amigo[0])
    #Si el enano que va a realizar la accion tiene amigos estos lo pueden acompaniar
    # if enano.friend:
    #     print(f"{enano.nombre} tiene amigos para hacer la tarea {accion}, quieres que alguno le ayude?")
    #     i = 0
    #     for enanos in enano.amigos:
    #         print(f"{i + 1}. {enanos.show_name()}")
    #         amigos.append(enanos)
    #         i += 1
    #     print("0. No quiero ayuda")
    #     op = input("Selecciona una opcion: ")
        
    
    op = random.randint(0, 20)
    if op != 15:
        print(f"posicion inicial de {enano.nombre}:\t", posicion_enano(enano, mascara))
        enano_pos = posicion_enano(enano, mascara)
        objetivo = obtener_objetivo_mas_cercano(enano_pos, mapa, t_recurso)
    
        if objetivo:
            mover_enano_hacia(enano, objetivo, mapa, mascara)
            gestor_acciones.reproducir_animacion(enano, accion)
            
            mapa[objetivo[0]][objetivo[1]] = tm.Tierra()
            # mascara[objetivo[0]][objetivo[1]] = None  # Actualizar la máscara
            enano.disponibilidad = [True, None]  # Marcar como disponible
        else:
            print(f"No se encontró ningún recurso.")
        
        print(f"posicion final de {enano.nombre}:\t", posicion_enano(enano, mascara))
        time.sleep(3)
        # prob = random.randint(1, 2)
        # if prob == 2:  
        #      st.interactive_story(accion, enano, todos)
        return enano
    
    else:
        amigo = random.choice(amigos)
        print(f"posicion inicial de {enano.nombre}:\t", posicion_enano(enano, mascara))
        enano_pos = posicion_enano(enano, mascara)
        objetivo = obtener_objetivo_mas_cercano(enano_pos, mapa, t_recurso)
    
        if objetivo:
            mover_enano_hacia(enano, objetivo, mapa, mascara)
            gestor_acciones.reproducir_animacion(enano, accion)
            
            mapa[objetivo[0]][objetivo[1]] = tm.Tierra()
            # mascara[objetivo[0]][objetivo[1]] = None  # Actualizar la máscara
            enano.disponibilidad = [True, None]  # Marcar como disponible
        else:
            print(f"No se encontró ningún recurso.")
        
        print(f"posicion final de {enano.nombre}:\t", posicion_enano(enano, mascara))
        time.sleep(3)
        print(f"{amigo.nombre} Esta ayudando a su amigo : {enano.nombre}")
        print(f"posicion inicial de {amigo.nombre}: \t", posicion_enano(amigo, mascara))
        enano_pos = posicion_enano(amigo, mascara)
        objetivo = obtener_objetivo_mas_cercano(enano_pos, mapa, t_recurso)
        
        if objetivo:
            mover_enano_hacia(amigo, objetivo, mapa, mascara)
            gestor_acciones.reproducir_animacion(amigo, accion)
                
            mapa[objetivo[0]][objetivo[1]] = tm.Tierra()
                # mascara[objetivo[0]][objetivo[1]] = None  # Actualizar la máscara
            enano.disponibilidad = [True, None]  # Marcar como disponible
        else:
            print(f"No se encontró ningún recurso.")
        
        print("posicion final de {amigo.nombre}:\t", posicion_enano(amigo, mascara))
        time.sleep(3)
        # prob = random.randint(1, 2)
        # if prob == 2:  
        #      st.interactive_story(accion, enano, todos)
        return enano

def distancia(p1, p2):
    """Calcula la distancia de Manhattan entre dos puntos."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def obtener_objetivo_mas_cercano(enano_pos, mapa, t_recurso):
    fila_cercana, col_cercana = None, None
    menor_distancia = float('inf')

    for fila in range(len(mapa)):
        for col in range(len(mapa[0])):
            if isinstance(mapa[fila][col], type(t_recurso)):
                d = distancia(enano_pos, (fila, col))
                if d < menor_distancia:
                    menor_distancia = d
                    fila_cercana, col_cercana = fila, col

    return (fila_cercana, col_cercana) if menor_distancia < float('inf') else None

def mover_enano_hacia(enano, destino, mapa, mascara):
    enano_pos = posicion_enano(enano, mascara)
    if enano_pos is None:
        print(f"Error: No se encontró la posición de {enano.nombre} en la máscara.")
        return  
    
    while enano_pos != destino:
        nueva_fila = enano_pos[0] + (1 if enano_pos[0] < destino[0] else -1 if enano_pos[0] > destino[0] else 0)
        nueva_col = enano_pos[1] + (1 if enano_pos[1] < destino[1] else -1 if enano_pos[1] > destino[1] else 0)
        
        # Verificar que nueva_fila y nueva_col estén dentro de los límites de la matriz
        if 0 <= nueva_fila < len(mascara) and 0 <= nueva_col < len(mascara[0]):
            mascara[enano_pos[0]][enano_pos[1]] = None  # Borra al enano de su posición actual
            enano_pos = (nueva_fila, nueva_col)
            mascara[enano_pos[0]][enano_pos[1]] = enano  # Coloca al enano en la nueva posición
            enano.posicion = enano_pos  # Actualiza la posición en el enano

            os.system('cls')
            m_c.imprimir_mapa_consola(mapa, mascara)
            time.sleep(0.005)  
        else:
            print(f"Error: Nueva posición {nueva_fila, nueva_col} está fuera de los límites.")
            break
        

if __name__ == "__main__":    
    mapa, mascara = m_c.generar_mapa()
    
    colonia = queue.PriorityQueue()
    poblacion,todos = extraer_poblacion(mascara)
    buffer_acciones = queue.deque()
    historial = Stack()
    poblacion,todos = extraer_poblacion(mapa)
    
    keyboard.add_hotkey('space', cambio_pausa)
    keyboard.add_hotkey('escape', terminar)
    keyboard.add_hotkey('f1', ejecutar)
    
    grupos = {}
    todos_grupo = set()
    
    pausa = False
    una_vez = True
    while True:
        if not pausa:
            os.system('cls')
            m_c.imprimir_mapa_consola(mapa, mascara)
            una_vez = True
            if buffer_acciones:
                acciones_a_realizar = gestor_acciones.procesar_acciones(buffer_acciones, colonia, poblacion)
                
                insertar_con_prioridad(acciones_a_realizar, colonia)
            prob = random.randint(1, 10)
            if prob == 5:
                p1 = random.choice(todos)
                p2 = random.choice(todos)
                while(p1 == p2 or p1 in p2.friends):
                    p2 = random.choice(todos)
                
                
                historial.push(fg.generar_amistad(p1, p2))
                print(historial.top())
                time.sleep(3)
            #Hay una probabilidad del 5% de que se genere una historia
                        
        elif una_vez:
            mostrar_poblacion(poblacion)
            menu_acciones(buffer_acciones, todos, grupos, todos_grupo)
            
            una_vez = False
            
        if ejecutando:
            print("Realizando acciones....")
            while not colonia.empty(): 
                p, index, [enano, accion] = colonia.get()
                # enano = ejecuta_accion(enano, accion)
                enano = ejecuta_accion(enano, accion, mapa, mascara, todos)
                if enano:
                    poblacion.append(enano)
                  

            print("Todas las acciones han sido completadas.")
            ejecutando = False  
                
        if salir:
            break

        time.sleep(0.1)
        # keyboard.wait('space')
    

    
    
    

    
    
    