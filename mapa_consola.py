# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:34:46 2024

@author: Dell
"""

import random

import razas 
import animales
import terrenos_y_materiales as tm


ALTO = 50
ANCHO = 50

def nuevo_personaje(raza):
    personajes = {'Enano': razas.Enano(),
                  'Humano': razas.Humano(),
                  'Elfo': razas.Elfo(),
                  'Mago': razas.Mago(),
                  'Orco': razas.Orco(),
                  'Goblin': razas.Goblin(),
                  'Trol': razas.Trol()}
    
    return personajes[raza]

def nuevo_animal(tipo):    
    creaturas = {
        'Gallina': animales.Gallina(),  
        'Pescado': animales.Pescado(),
        'Perro': animales.Perro(),    
        'Gato': animales.Gato(),     
        'Cerdo': animales.Cerdo(),    
        'Vaca': animales.Vaca(),  
        'Caballo': animales.Caballo(),  
        'Poni': animales.Poni(),    
        'Conejo': animales.Conejo(),   
        'Rana': animales.Rana(),     
        'Borrego': animales.Borrego(),  
        'Chivo': animales.Chivo(),     
        'Jabali': animales.Jabali(),
        'Oso': animales.Oso()
    }
    
    return creaturas[tipo]
    
def nuevo_fruto(tipo):
    recursos = {'Manzana': tm.Manzana(),
                'Naranja': tm.Naranja(),
                'Mango': tm.Mango(),
                'Uva': tm.Uva(),
                'Sandía': tm.Sandia(),
                'Fresa': tm.Fresa(),
                'Trigo': tm.Trigo()}
    
    return recursos[tipo]

def generar_terreno():    
    terrenos = tm.lista_terrenos()
    probabilidades = [30, 20, 20, 30, 10, 10]
    
    mapa = []
    for i in range(ALTO):
        fila = []
        for j in range(ANCHO):
            terreno = random.choices(terrenos, weights=probabilidades, k=1)[0]
            fila.append(terreno)
        mapa.append(fila)
    return mapa

def colocar_personajes(mapa, raza, area):
    x_inicio, x_fin, y_inicio, y_fin = area
    cantidad = random.randint(5, 8)  # Cantidad de personajes de esa raza
    for _ in range(cantidad):
        x = random.randint(x_inicio, x_fin)
        y = random.randint(y_inicio, y_fin)
        mapa[x][y] = nuevo_personaje(raza)

def colocar_animales(mapa, tipo, area):
    x_o, y_o = area
    cantidad = random.randint(1, 3)  
    for _ in range(cantidad):
        x = random.randint(x_o, 49)
        y = random.randint(y_o, 49)
        mapa[x][y] = nuevo_animal(tipo)  

def colocar_recursos(mapa, tipo, area):
    x_o, y_o = area
    cantidad = random.randint(1, 3)  
    for _ in range(cantidad):
        x = random.randint(x_o, 49)
        y = random.randint(y_o, 49)
        mapa[x][y] = nuevo_fruto(tipo)

def generar_mapa():
    mapa = generar_terreno()
    mascara = [[None]*len(mapa) for _ in range(len(mapa))]

    areas = {
        'Enano': (0, 9, 0, 9),      
        'Elfo': (0, 9, 10, 19),   
        'Humano': (0, 9, 20, 29),  
        'Mago': (10, 29, 35, 49),   
        'Orco': (40, 49, 10, 19), 
        'Trol': (40, 49, 20, 29), 
        'Goblin': (40, 49, 30, 39)   
    }

    # Colocar personajes de cada raza en sus áreas
    for raza, area in areas.items():
        if raza != 'Enano':
            colocar_personajes(mapa, raza, area)
        else:
            colocar_personajes(mascara, raza, area)
    
    creaturas = animales.lista_animales()
    for animal in creaturas:
        x = random.randint(0, 49)
        y = random.randint(0, 49)
        colocar_animales(mapa, animal.tipo, (x, y))    
    
    frutos = tm.lista_frutos()
    for fruto in frutos:
        x = random.randint(0, 49)
        y = random.randint(0, 49)
        colocar_recursos(mapa, fruto.tipo, (x, y))  
        
    return mapa, mascara    

def imprimir_mapa_consola(mapa, mascara):
    output = ''
    for fila_mapa, fila_mascara in zip(mapa, mascara):
        for tipo_mapa, tipo_mascara in zip(fila_mapa, fila_mascara):
            if isinstance(tipo_mascara, razas.Enano):
                output += ''.join(tipo_mascara.simbolo)
            else: 
                output += ''.join(tipo_mapa.simbolo)
            
        output += '\n'
        
    print(output)

if __name__ == "__main__":    
    mapa, mascara = generar_mapa()
        
    imprimir_mapa_consola(mapa, mascara)
    
    
