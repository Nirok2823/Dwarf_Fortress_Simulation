# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:34:25 2024

@author: Dell
"""

import random

class Material:
    def __init__(self, materiales):
        self.mapa_materiales = {'Madera': 0, 'Composta': 0, 'Aceite': 0, 
                                'Roca': 0, 'Sal': 0, 'Hierro': 0, 'Agua': 0,
                                'Arsilla': 0, 'Manzana': 0, 'Naranja': 0,
                                'Mango': 0, 'Uva': 0, 'Sandía': 0, 
                                'Fresa': 0, 'Trigo': 0}
        
        for m, c in materiales:
            if m in self.mapa_materiales:
                self.mapa_materiales[m] = c

class Terreno:
    def __init__(self, tipo, materiales, simbolo):
        self.tipo = tipo
        self.materiales = materiales
        self.simbolo = simbolo
        self.info = self.__repr__()
        
    def explotacion(self):
        return self.materiales.mapa_materiales
    
    def __repr__(self):
        return f"Tipo: {self.simbolo}_{self.tipo}, Materiales: {self.materiales.mapa_materiales}"

class Arbol(Terreno):
    def __init__(self):
        m = [('Madera', 5), ('Composta', 1), ('Aceite', 0.5)]  
        materiales = Material(m)
        simbolo = '🌳'
        super().__init__('Arbol', materiales, simbolo)
        
class Pino(Terreno):
    def __init__(self):
        m = [('Madera', 7), ('Composta', 1), ('Aceite', 2)]
        materiales = Material(m)
        simbolo = '🌲'
        super().__init__('Pino', materiales, simbolo)

class Montana(Terreno):
    def __init__(self):
        m = [('Roca', 7), ('Sal', 2), ('Hierro', 1)]
        materiales = Material(m)
        simbolo = '🗻'
        super().__init__('Montaña', materiales, simbolo)

class Agua(Terreno):
    def __init__(self):
        m = [('Agua', random.randint(1, 5))]
        materiales = Material(m)
        simbolo = '🌊'
        super().__init__('Agua', materiales, simbolo)

class Tierra(Terreno):
    def __init__(self):
        m = [('Arsilla', 1)]
        materiales = Material(m)
        simbolo = '🟨'
        super().__init__('Tierra', materiales, simbolo)

class Lodo(Terreno):
    def __init__(self):
        m = [('Arsilla', 1)]
        materiales = Material(m)
        simbolo = '🟫'
        super().__init__('Lodo', materiales, simbolo)
        
class Frutos:
    def __init__(self, tipo, materiales, simbolo):
        self.tipo = tipo
        self.materiales = materiales
        self.simbolo = simbolo
        self.info = self.__repr__()
    
    def explotacion(self):
        return self.materiales.mapa_materiales
    
    def __repr__(self):
        return f"Tipo: {self.simbolo}_{self.tipo}, Materiales: {self.materiales.mapa_materiales}"
    
class Manzana(Frutos):
    def __init__(self):
        m = [('Manzana', 2)]  
        materiales = Material(m)
        simbolo = '🍎'
        super().__init__('Manzana', materiales, simbolo)

class Naranja(Frutos):
    def __init__(self):
        m = [('Naranja', 2)]  
        materiales = Material(m)
        simbolo = '🍊'
        super().__init__('Naranja', materiales, simbolo)

class Mango(Frutos):
    def __init__(self):
        m = [('Mango', 2)]  
        materiales = Material(m)
        simbolo = '🥭'
        super().__init__('Mango', materiales, simbolo)

class Uva(Frutos):
    def __init__(self):
        m = [('Uva', 5)]  
        materiales = Material(m)
        simbolo = '🍇'
        super().__init__('Uva', materiales, simbolo)

class Sandia(Frutos):
    def __init__(self):
        m = [('Sandía', 3)]  
        materiales = Material(m)
        simbolo = '🍉'
        super().__init__('Sandía', materiales, simbolo)

class Fresa(Frutos):
    def __init__(self):
        m = [('Fresa', 5)]  
        materiales = Material(m)
        simbolo = '🍓'
        super().__init__('Fresa', materiales, simbolo)

class Trigo(Frutos):
    def __init__(self):
        m = [('Trigo', 2)]  
        materiales = Material(m)
        simbolo = '🌾'
        super().__init__('Trigo', materiales, simbolo)
        
def lista_terrenos():
    return [Arbol(), Pino(), Montana(), Agua(), Tierra(), Lodo()]

def lista_frutos():
    return [Manzana(), Naranja(), Mango(), Uva(), Sandia(), Fresa(), Trigo()]

if __name__ == "__main__":
    terrenos = lista_terrenos()
    
    for terreno in terrenos:
        print(terreno)
        print(f"Materiales de Explotación: {terreno.explotacion()}")
        print('---')
    print("\n\n")
        
    frutos = lista_frutos()
    for fruto in frutos:
        print(fruto)
        print(f"Materiales de Explotación: {fruto.explotacion()}")
        print('---')