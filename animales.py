# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:35:58 2024

@author: Dell
"""

import random

class Material:
    def __init__(self, materiales):
        self.mapa_materiales = {'Carne': 0, 'Huesos': 0, 'Plumas': 0, 
                                'Cuero': 0, 'Lana': 0, 'Pelaje': 0}
        
        for m, c in materiales:
            if m in self.mapa_materiales:
                self.mapa_materiales[m] = c

class Animal:
    def __init__(self, tipo, materiales, edad, edad_max, simbolo):
        self.tipo = tipo
        self.genero = self.generar_genero()
        self.materiales = materiales
        self.edad = edad
        self.edad_max = edad_max
        self.simbolo = simbolo
        self.info = self.__repr__()
    
    def generar_genero(self):
        return random.choices(['♂', '♀'], weights=[50, 50], k=1)[0]
    
    def sacrificio(self):
        return self.materiales.mapa_materiales
    
    def __repr__(self):
        return f"Tipo: {self.simbolo}_{self.tipo}, Género: {self.genero}, Edad: {self.edad}/{self.edad_max} años"

class Gallina(Animal):
    def __init__(self):
        m = [('Carne', 4), ('Plumas', 1)]  # 4 raciones de carne, 1 de plumas
        materiales = Material(m)
        edad = random.randint(0, 5)  # Edad inicial del animal
        edad_max = 10  # Esperanza de vida de la gallina
        simbolo = '🐔'
        super().__init__('Gallina', materiales, edad, edad_max, simbolo)
        
class Pescado(Animal):
    def __init__(self):
        m = [('Carne', 2)]  # 4 raciones de carne, 1 de plumas
        materiales = Material(m)
        edad = random.randint(0, 2)  # Edad inicial del animal
        edad_max = 5  # Esperanza de vida de la gallina
        simbolo = '🐟'
        super().__init__('Pescado', materiales, edad, edad_max, simbolo)

class Perro(Animal):
    def __init__(self):
        m = [('Carne', 8), ('Huesos', 3), ('Cuero', 1)]  # Materiales que se obtienen del perro
        materiales = Material(m)
        edad = random.randint(0, 10)
        edad_max = 20  # Esperanza de vida de un perro
        simbolo = '🐕'
        super().__init__('Perro', materiales, edad, edad_max, simbolo)

class Gato(Animal):
    def __init__(self):
        m = [('Carne', 3), ('Huesos', 2), ('Cuero', 1)]  # Materiales obtenidos del gato
        materiales = Material(m)
        edad = random.randint(0, 8)
        edad_max = 16  # Esperanza de vida de un gato
        simbolo = '🐈'
        super().__init__('Gato', materiales, edad, edad_max, simbolo)

class Cerdo(Animal):
    def __init__(self):
        m = [('Carne', 20), ('Huesos', 5), ('Cuero', 3)]  # Materiales obtenidos del cerdo
        materiales = Material(m)
        edad = random.randint(0, 5)
        edad_max = 15  # Esperanza de vida de un cerdo
        simbolo = '🐖'
        super().__init__('Cerdo', materiales, edad, edad_max, simbolo)

class Jabali(Animal):
    def __init__(self):
        m = [('Carne', 25), ('Huesos', 7), ('Cuero', 5)]  # Materiales obtenidos del cerdo
        materiales = Material(m)
        edad = random.randint(0, 10)
        edad_max = 25  # Esperanza de vida de un cerdo
        simbolo = '🐗'
        super().__init__('Jabali', materiales, edad, edad_max, simbolo)

class Vaca(Animal):
    def __init__(self):
        m = [('Carne', 50), ('Huesos', 20), ('Cuero', 10)]  # Materiales obtenidos de la vaca/toro
        materiales = Material(m)
        edad = random.randint(0, 10)
        edad_max = 25  # Esperanza de vida de una vaca
        simbolo = '🐄'
        super().__init__('Vaca', materiales, edad, edad_max, simbolo)

class Caballo(Animal):
    def __init__(self):
        m = [('Carne', 30), ('Huesos', 10), ('Cuero', 5)]  # Materiales obtenidos del caballo
        materiales = Material(m)
        edad = random.randint(0, 10)
        edad_max = 30  # Esperanza de vida de un caballo
        simbolo = '🐎'
        super().__init__('Caballo', materiales, edad, edad_max, simbolo)

class Poni(Animal):
    def __init__(self):
        m = [('Carne', 15), ('Huesos', 5), ('Cuero', 3)]  # Materiales obtenidos del poni
        materiales = Material(m)
        edad = random.randint(0, 5)
        edad_max = 20  # Esperanza de vida de un poni
        simbolo = '🦄'
        super().__init__('Poni', materiales, edad, edad_max, simbolo)

class Conejo(Animal):
    def __init__(self):
        m = [('Carne', 2), ('Huesos', 1), ('Cuero', 1)]  # Materiales obtenidos del conejo
        materiales = Material(m)
        edad = random.randint(0, 3)
        edad_max = 10  # Esperanza de vida de un conejo
        simbolo = '🐇'
        super().__init__('Conejo', materiales, edad, edad_max, simbolo)

class Rana(Animal):
    def __init__(self):
        m = [('Carne', 1), ('Huesos', 0.5)]  # Materiales obtenidos de la rana
        materiales = Material(m)
        edad = random.randint(0, 2)
        edad_max = 8  # Esperanza de vida de una rana
        simbolo = '🐸'
        super().__init__('Rana', materiales, edad, edad_max, simbolo)

class Borrego(Animal):
    def __init__(self):
        m = [('Carne', 15), ('Huesos', 7), ('Cuero', 3), ('Lana', 10)]  # Materiales obtenidos del borrego
        materiales = Material(m)
        edad = random.randint(0, 6)
        edad_max = 15  # Esperanza de vida de un borrego
        simbolo = '🐑'
        super().__init__('Borrego', materiales, edad, edad_max, simbolo)

class Chivo(Animal):
    def __init__(self):
        m = [('Carne', 12), ('Huesos', 6), ('Cuero', 2)]  # Materiales obtenidos del chivo
        materiales = Material(m)
        edad = random.randint(0, 5)
        edad_max = 15  # Esperanza de vida de un chivo
        simbolo = '🐐'
        super().__init__('Chivo', materiales, edad, edad_max, simbolo)

class Oso(Animal):
    def __init__(self):
        m = [('Carne', 25), ('Huesos', 15), ('Cuero', 30), ('Pelaje', 15)]  # Materiales obtenidos del borrego
        materiales = Material(m)
        edad = random.randint(3, 15)
        edad_max = 25  # Esperanza de vida de un borrego
        simbolo = '🐻'
        super().__init__('Oso', materiales, edad, edad_max, simbolo)


def lista_animales():    
    return [Gallina(), Pescado(), Perro(), Gato(), Cerdo(), Jabali(), Vaca(), 
            Caballo(), Poni(), Conejo(), Rana(), Borrego(), Chivo(), Oso()]

if __name__ == "__main__":
    animales = lista_animales()
    
    for animal in animales:
        print(animal)
        print(f"Materiales al sacrificio: {animal.sacrificio()}")
        print('---')
