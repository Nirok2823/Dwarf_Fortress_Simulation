# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:06:59 2024

@author: Dell
"""

import random
import time
import razas
import story_generator as st
import Story_gen as gs
"""
Puntos importantes para generar amistad
1. Tipo
2. Genero
3. Gremio (Oficio)
4. Posicion Social

Por el momento se van a considerar estas caracteristicas para
generar una amistad no solo entre enanos sino entre razas tambien

Tipos de amistad
1. Amorosa: Entre humanos , elfos, y enanos, no se discrimina el amor.
2. Conveniencia: Amistad entre razas como lo puede ser entre ogro y enano para su proteccion
3. De Oficio: Amistad entre los que comparten el mismo tipo de oficio
4. Amigos Cercanos: Algun evento los hace amigos cercanos
5. Conocidos: Simplemente se conocen.
"""

def generar_amistad(per1, per2):
    #Primero vamos a verificar la amistad entre los 2 personajes y se le dara un
    #Valor para ver la compatibilidad con el tipo de amistad.
    #El tipo de amistad con mas valor sera la que prevalesca tomando en cuenta los parametros pasados
    #Tipos de amistad
    if per1 not in per2.friends:
        amistad = {"amorosa" : 0, "de conveniencia": 0, 
                   "de oficio": 0, "cercana": 0, "casual": 0}
        amor = "amorosa"
        conv = "de conveniencia"
        gremio = "de oficio"
        cercanos = "cercana"
        conocidos = "casual"
        
        #Amistad amor y cercanos, Si son humanos, elfos o  Enanos
        # if (isinstance(per1, razas.Humano) or isinstance(per1, razas.Elfo) or isinstance(per1, razas.Enano)) and (isinstance(per2, razas.Humano) or isinstance(per2, razas.Elfo) or isinstance(per2, razas.Enano)):
        #     if per1.genero != per2.genero and per1.tipo == per2.tipo:
        #         amor += .4 # el genero de una persona dictamina el amor hacia otra
        #         # y mas si son de la misma especie
        #     elif per1.genero != per2.genero:
        #         amor += .1
        #     else:
        #         conocidos += .3 #si son del mismo genero, lo conocido y amigos puede aumentar
        #         cercanos += .3
        
        if per1.genero != per2.genero and per1.tipo == per2.tipo:
            amistad[amor] += .3 # el genero de una persona dictamina el amor hacia otra
                # y mas si son de la misma especie
        elif per1.genero != per2.genero:
            amistad[amor] += .2
        elif per1.genero == per2.genero and per1.tipo == per2.tipo:
            amistad[cercanos] += .3
        elif per1.genero == per2.genero:
            amistad[cercanos] += .2
        else:
            amistad[conocidos] += .3 #si son del mismo genero, lo conocido y amigos puede aumentar
            
        
        flag = 0
        for oficio, nivel in per1.oficios:#verificar el numero de oficios en comun
            for ofi, lvl in per2.oficios:
                if(oficio == ofi and nivel == lvl):
                    amistad[gremio] += .35
                    amistad[cercanos] += .15
                    amistad[amor] += .1
                    flag = 1
                elif oficio == ofi :
                    amistad[gremio] += .25
                    amistad[cercanos] += .1
                    flag = 1
            if flag == 1:
                amistad[conv] += .1
                flag = 0
        
        social= {'Ciudadano': 1 , 'Soldado': 2, 'Capataz': 3, 'Noble': 4, 'Rey/Reina': 5}
        
        if social[per1.posicion_social] == social[per2.posicion_social]:
            amistad[cercanos] += .2
            amistad[conocidos] += .2
        else:
            amistad[conv] += .2
        maxKey = ""
        maxVal = 0
        for key, value in amistad.items():
            if(value > maxVal):
                maxVal = value
                maxKey = key
        
        per1.friends[per2.nombre] = (per2, f"Amistad {maxKey}")
        per2.friends[per1.nombre] = (per1, f"Amistad {maxKey}")
        
        return st.generate_story(f"{maxKey}", per1, per2)
    
    else:
        return None
        # acciones = ["Agua", "Talar", "Alimento", "Minar", "Comerciar"]
        # return gs.gen_story(random.choice(acciones), per1, per2)
            
    
        
        
        
    
        
        
            