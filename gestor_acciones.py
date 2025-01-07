# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:35:16 2024

@author: Dell
"""

import queue
import razas  
from collections import deque

import os
import time

niveles = {
    'Pobre': 1, 
    'Aprendiz': 2, 
    'Adecuado': 3, 
    'Muy Adecuado': 4, 
    'Experto': 5}

posibles_oficios = ['Minero', 'Albañil', 'Carnicero', 'Cazador', 'Pescador', 
                    'Herrero', 'Joyero', 'Granjero', 'Veterinario', 'Medico', 
                    'Artesano', 'Militar', 'Cocinero', 'Carpintero']

tipos_acciones = {
    'Agua': ['Granjero', 'Cazador', 'Pescador', 'Cocinero', 'Carnicero', 
             'Veterinario', 'Albañil', 'Minero', 'Joyero', 'Herrero', 
             'Artesano', 'Carpintero', 'Medico', 'Militar'],
    'Talar': ['Granjero', 'Cazador', 'Pescador', 'Cocinero', 'Carnicero', 
              'Veterinario', 'Albañil', 'Minero', 'Joyero', 'Herrero', 
              'Artesano', 'Carpintero', 'Medico', 'Militar'],
    'Alimento': ['Granjero', 'Cazador', 'Pescador', 'Cocinero', 'Carnicero', 
                 'Veterinario', 'Albañil', 'Minero', 'Joyero', 'Herrero', 
                 'Artesano', 'Carpintero', 'Medico', 'Militar'],
    'Minar': ['Minero', 'Albañil', 'Herrero', 'Granjero', 'Joyero', 
              'Artesano', 'Carpintero','Cazador', 'Pescador', 'Cocinero', 
              'Carnicero', 'Veterinario',  'Medico', 'Militar'],
    'Comerciar': ['Joyero', 'Artesano', 'Carpintero', 'Herrero', 'Granjero', 
                  'Cazador', 'Pescador', 'Cocinero', 'Carnicero', 'Veterinario', 
                  'Albañil', 'Minero', 'Medico', 'Militar'],
    'Atacar': ['Militar', 'Minero', 'Albañil', 'Herrero', 'Granjero', 
               'Joyero', 'Artesano', 'Carpintero','Cazador', 'Pescador', 
               'Cocinero', 'Carnicero', 'Veterinario',  'Medico']
    }

animaciones = {'Agua': [[["~", " ", "~"],
                         [" ", "~", " "],
                         ["~", " ", "~"]],
                        [[" ", "~", " "],
                         ["~", " ", "~"],
                         [" ", "~", " "]],
                        [["~", " ", "~"],
                         [" ", "~", " "],
                         ["~", " ", "~"]],
                        [[" ", "~", " "],
                         ["~", " ", "~"],
                         [" ", "~", " "]]],
               'Talar': [[["|", " ", " "],
                          [" ", "|", " "],
                          [" ", " ", "|"]],
                         [[" ", "|", " "],
                          [" ", "|", " "],
                          [" ", "|", " "]],
                         [[" ", " ", "|"],
                          [" ", "|", " "],
                          ["|", " ", " "]],
                         [[" ", "|", " "],
                          [" ", "|", " "],
                          [" ", "|", " "]]],
               'Alimento': [[["*", " ", "*"],
                             [" ", "*", " "],
                             ["*", " ", "*"]],
                            [[" ", "*", " "],
                             ["*", " ", "*"],
                             [" ", "*", " "]],
                            [["*", " ", "*"],
                             [" ", "*", " "],
                             ["*", " ", "*"]],
                            [[" ", "*", " "],
                             ["*", " ", "*"],
                             [" ", "*", " "]]],
               'Minar': [[[" ", "o", " "],
                          ["o", " ", "o"],
                          [" ", "o", " "]],
                         [["o", " ", "o"],
                          [" ", "o", " "],
                          ["o", " ", "o"]],
                         [[" ", "o", " "],
                          ["o", " ", "o"],
                          [" ", "o", " "]],
                         [["o", " ", "o"],
                          [" ", "o", " "],
                          ["o", " ", "o"]]],
               'Comerciar': [[["$", " ", "$"],
                              [" ", "$", " "],
                              ["$", " ", "$"]],
                             [[" ", "$", " "],
                              ["$", " ", "$"],
                              [" ", "$", " "]],
                             [["$", " ", "$"],
                              [" ", "$", " "],
                              ["$", " ", "$"]],
                             [[" ", "$", " "],
                              ["$", " ", "$"],
                              [" ", "$", " "]]],
               'Atacar': [[["!", " ", "!"],
                           [" ", "!", " "],
                           ["!", " ", "!"]],
                          [[" ", "!", " "],
                           ["!", " ", "!"],
                           [" ", "!", " "]],
                          [["!", " ", "!"],
                           [" ", "!", " "],
                           ["!", " ", "!"]],
                          [[" ", "!", " "],
                           ["!", " ", "!"],
                           [" ", "!", " "]]]}

def reproducir_animacion(enano, accion):
    print(f"{enano.simbolo} {enano.nombre} realizando {accion}")
    for animacion in animaciones[accion]:
        # os.system('cls' if os.name == 'nt' else 'clear')
        for fila in animacion:
            print("".join(fila))
        time.sleep(0.3)
        print("\033[F" * 3, end="")  # Mueve el cursor 8 líneas hacia arriba
    print("\033[F" * 1, end="")

def evaluar_compatibilidad(enano, accion):
    puntaje_compatibilidad = 0
    
    jerarquia_oficios_por_accion = tipos_acciones.get(accion, [])
    
    # Iterar sobre los oficios del enano para calcular el puntaje de compatibilidad
    for oficio, nivel in enano.oficios:
        if oficio in jerarquia_oficios_por_accion:
            # Obtener posición en jerarquía y valor de nivel
            posicion = jerarquia_oficios_por_accion.index(oficio)
            nivel_valor = niveles.get(nivel, 0)
            
            # Calcular compatibilidad, aumentando con el nivel y bajando con la posición
            compatibilidad_actual = nivel_valor * (len(jerarquia_oficios_por_accion) - posicion)
            puntaje_compatibilidad = max(puntaje_compatibilidad, compatibilidad_actual)
    
    return puntaje_compatibilidad


# Función para seleccionar al mejor enano para una acción
def seleccionar_mejor_enano(accion, poblacion):
    mejor_enano = None
    mayor_prioridad = 0
    enanos_disponibles = []
    
    # while not poblacion:
    for p in poblacion:
        # enano = poblacion.get()
        enano = p
        
        compatibilidad = evaluar_compatibilidad(enano, accion)
        
        if compatibilidad > mayor_prioridad:
            mayor_prioridad = compatibilidad
            mejor_enano = enano
            
        enanos_disponibles.append((mayor_prioridad, enano))  # Guardar enanos revisados para retornarlos

    # # Devolver los enanos revisados a la colonia, excepto el mejor
    # for prioridad, enano in enanos_disponibles:
    #     if enano != mejor_enano:
    #         colonia.put((prioridad, enano))

    return mejor_enano

# Función para procesar el buffer de acciones y ejecutar las compatibles
def procesar_acciones(buffer_acciones, colonia, poblacion):
    acciones_a_realizar = []

    while buffer_acciones:
        accion = buffer_acciones.popleft()
        enano = seleccionar_mejor_enano(accion, poblacion)

        if enano:
            # Marcar al enano como ocupado con la acción
            enano.disponibilidad = [False, accion]
            # poblacion.append(enano)
            poblacion.remove(enano)
            acciones_a_realizar.append([enano, accion])
    
    return acciones_a_realizar  # Devuelve los pares [enano, acción] para el reporte
