# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:33:19 2024

@author: Dell
"""

import random

"""
Enano: 🧔♂️ (Aunque es un mago, puede simbolizar un enano por su barba y apariencia)
Elfo: 🧝‍♂️ o 🧝‍♀️ (Representan a un elfo masculino o femenino)
Humano: 🧑 (Sencillo y genérico para representar un humano)
Orco: 👹 (Una criatura con rasgos monstruosos que puede simbolizar un orco)
Trol: 🧟‍♂️ o 🧟‍♀️ (Simboliza un trol o una criatura parecida a un zombi)
Goblin: 👺 (Simboliza a una criatura traviesa o malévola, que podría representar a un goblin)
Mago: 🧙‍♂️ o 🧙‍♀️ (Representan a un mago masculino o femenino)
"""

import random

# Nombres de enanos
def nombre_enanos():
    prefijo = random.choice([
        "Bal", "Bjor", "Dwalin", "Gimli", "Thorin", "Durin", "Balin", "Thrain", 
        "Fundin", "Oin", "Glóin", "Nori", "Dori", "Thrar", "Vili", "Kili", "Fili", 
        "Dror", "Veigr", "Har", "Sindri", "Brokk", "Eitri", "Vestri", "Noddi", 
        "Alviss", "Modi", "Skor", "Rúni", "Grundi"
    ])

    sufija = random.choice([
        "son", "dson", "in", "bor", "ir", "und", "dur", "th", "f", "grim", 
        "rik", "dan", "mir", "zorn", "gar", "gund", "had", "ri", "od", "zor", 
        "rok", "mar", "bel", "gar", "fir", "bor", "red", "var", "ron", "gun"
    ])

    raiz = random.choice([
        "bar", "grim", "durin", "azog", "bald", "zorn", "mund", "brand", 
        "fang", "thrak", "kar", "gund", "ir", "od", "mod", "krag", "vur", 
        "fund", "nak", "thrund", "dor", "mod", "bron", "vek", "rag", 
        "grod", "bold", "tror", "bard", "snor"
    ])

    return prefijo + raiz + sufija

# Nombres de elfos
def nombre_elfos():
    prefijo = random.choice([
        'Aeril', 'Laer', 'Galad', 'Elowen', 'Silvan', 'Faer', 'Eldar', 
        'Anor', 'Luth', 'Melian', 'Nimrodel', 'Cala', 'Alatar', 'Alfirin', 
        'Celeb', 'Finduilas', 'Haldir', 'Lorien', 'Thranduil', 'Aredhel', 
        'Eärendil', 'Amroth', 'Thingol', 'Yavanna', 'Glorfindel', 'Tauriel', 
        'Voronwe', 'Ecthelion', 'Curufin', 'Gildor'
    ])

    sufija = random.choice([
        'ion', 'el', 'yn', 'ar', 'en', 'il', 'dor', 'uil', 'as', 'las', 
        'iel', 'ien', 'dae', 'mir', 'nor', 'ros', 'an', 'ion', 'iel', 
        'ser', 'reth', 'los', 'ion', 'ri', 'wen', 'gal', 'thir', 'fin', 'ion'
    ])

    raiz = random.choice([
        'thal', 'sil', 'quen', 'mir', 'riel', 'gil', 'gal', 'nion', 'las', 
        'an', 'nor', 'iel', 'fin', 'duin', 'ven', 'cel', 'bel', 'los', 'nen', 
        'mar', 'fëa', 'tir', 'bor', 'nir', 'oth', 'dir', 'wen', 'lor', 'dal', 'lam'
    ])

    return prefijo + raiz + sufija

# Nombres de humanos
def nombre_humanos():
    nombre = random.choice([
        'Aragorn', 'Eowyn', 'Boromir', 'Cersei', 'Tyrion', 'Jon', 'Daenerys', 
        'Ned', 'Sansa', 'Arya', 'Robb', 'Renly', 'Margaery', 'Brienne', 'Davos', 
        'Samwell', 'Rhaegar', 'Viserys', 'Oberyn', 'Gregor', 'Sandor', 'Jorah', 
        'Khal', 'Joffrey', 'Loras', 'Theon', 'Aegon', 'Aerys', 'Bran', 'Meera'
    ])

    apellido = random.choice([
        'Stark', 'Lannister', 'Baratheon', 'Tully', 'Greyjoy', 'Martell', 'Targaryen', 
        'Tyrell', 'Bolton', 'Arryn', 'Frey', 'Seaworth', 'Mormont', 'Harlaw', 'Florent', 
        'Blackwood', 'Royce', 'Dayne', 'Hightower', 'Tarly', 'Dondarrion', 'Qorgyle', 
        'Redwyne', 'Reyne', 'Drumm', 'Karstark', 'Clegane', 'Bracken', 'Vaith', 'Velaryon'
    ])

    return nombre + " " + apellido

# Nombres de goblins
def nombre_goblins():
    prefijo = random.choice([
        'Gork', 'Mork', 'Snagg', 'Grok', 'Snik', 'Grubb', 'Skarsnik', 'Flog', 
        'Scragg', 'Zog', 'Grot', 'Snarl', 'Splut', 'Bork', 'Rug', 'Blug', 
        'Narg', 'Krug', 'Skag', 'Gub', 'Snit', 'Znit', 'Nob', 'Slog', 'Skrag', 
        'Wug', 'Tug', 'Grak', 'Nog', 'Trug'
    ])

    sufija = random.choice([
        'it', 'og', 'ug', 'ig', 'og', 'ak', 'ik', 'uk', 'ag', 'ur', 'ob', 'ok', 
        'ig', 'ir', 'ug', 'un', 'ur', 'iz', 'uk', 'uz', 'op', 'oz', 'ox', 'ix', 
        'az', 'ix', 'ul', 'uz', 'or', 'ix'
    ])

    raiz = random.choice([
        'snap', 'grot', 'snarl', 'slit', 'spik', 'nash', 'krug', 'frot', 
        'snit', 'thrak', 'smash', 'bash', 'splat', 'grot', 'skrag', 'snik', 
        'splut', 'trog', 'blok', 'brak', 'krut', 'grug', 'knut', 'zrak', 'snub', 
        'grub', 'zog', 'gnub', 'zlat', 'grit'
    ])

    return prefijo + raiz + sufija

# Nombres de orcos
def nombre_orcos():
    prefijo = random.choice([
        'Gruk', 'Gor', 'Mork', 'Ugluk', 'Thrak', 'Shagrat', 'Azog', 'Gorgor', 
        'Bagdush', 'Lurtz', 'Krogg', 'Skog', 'Uzgash', 'Borak', 'Grishnakh', 
        'Mauhur', 'Turg', 'Bruk', 'Zarg', 'Fash', 'Morg', 'Ghash', 'Rug', 'Flog', 
        'Skarn', 'Brug', 'Thurg', 'Durg', 'Uruk', 'Krug'
    ])

    sufija = random.choice([
        'og', 'ug', 'ak', 'uk', 'ik', 'osh', 'ash', 'usk', 'rak', 'rok', 'zog', 
        'mog', 'zag', 'gash', 'bog', 'shag', 'zag', 'rog', 'mok', 'grok', 
        'skak', 'glok', 'zok', 'brak', 'ruk', 'rug', 'mog', 'zak', 'ug'
    ])

    raiz = random.choice([
        'bash', 'smash', 'gash', 'slash', 'crush', 'throg', 'krag', 'drak', 
        'gruk', 'blok', 'krag', 'glok', 'krash', 'rug', 'snak', 'grog', 
        'fash', 'grag', 'rung', 'snug', 'brug', 'thrash', 'drash', 'grub', 
        'blok', 'ghash', 'grosh', 'blok', 'trak', 'flog'
    ])

    return prefijo + raiz + sufija

# Nombres de trolls
def nombre_trols():
    prefijo = random.choice([
        'Throm', 'Blarg', 'Gorog', 'Throg', 'Gnarl', 'Snarg', 'Blug', 'Flog', 
        'Grog', 'Krag', 'Grag', 'Thrag', 'Brag', 'Clog', 'Smash', 'Thorg', 
        'Grum', 'Mug', 'Wug', 'Krunk', 'Ulg', 'Zrag', 'Trog', 'Skrog', 'Gron', 
        'Frog', 'Thrug', 'Frak', 'Brug', 'Snag'
    ])

    sufija = random.choice([
        'um', 'og', 'ug', 'ak', 'uk', 'uz', 'ur', 'og', 'uk', 'az', 'ak', 'oz', 
        'ok', 'ag', 'ag', 'ik', 'iz', 'uk', 'ok', 'az', 'os', 'ox', 'om', 
        'ux', 'um', 'ig', 'ik', 'iz', 'ux', 'ok'
    ])

    raiz = random.choice([
        'stone', 'rock', 'bone', 'crag', 'peak', 'snag', 'clog', 'krag', 'thrag', 
        'throg', 'slag', 'knob', 'smash', 'bash', 'snap', 'crash', 'boulder', 
        'gnash', 'mount', 'ridge', 'thorn', 'slag', 'thud', 'grit', 'grind', 
        'lurk', 'dread', 'skrag', 'nash', 'crank'
    ])

    return prefijo + raiz + sufija

# Nombres de magos
def nombre_magos():
    nombre = random.choice([
        'Gandalf', 'Merlin', 'Saruman', 'Elminster', 'Morgoth', 'Radagast', 
        'Malfurion', 'Rincewind', 'Raistlin', 'Ged', 'Allanon', 'Brom', 
        'Belgarath', 'Zeddicus', 'Albus', 'Severus', 'Gellert', 'Yennefer', 
        'Ainz', 'Drizzt', 'Kelsier', 'Dumbledore', 'Riftan', 'Matrim', 
        'Kelban', 'Mordenkainen', 'Voldemort', 'Gorion', 'Elric', 'Takhisis'
    ])

    apellido = random.choice([
        'el Gris', 'el Blanco', 'el Negro', 'el Rojo', 'el Sabio', 'el Oscuro', 
        'el Dorado', 'el Violeta', 'el Pálido', 'el Místico', 'el Antiguo', 
        'el Supremo', 'el Siniestro', 'el Sabio', 'el Fuerte', 'el Mago', 
        'el Hechicero', 'el Anciano', 'el Temido', 'el Poderoso', 'el Severo', 
        'el Extraño', 'el Desterrado', 'el Visionario', 'el Arcano', 
        'el Profundo', 'el Terrible', 'el Alto', 'el Despiadado', 'el Silencioso'
    ])

    return nombre + " " + apellido


# Generador de nombres basado en la raza (enanos)
def generador_nombres(raza):
    if 'enano' in str(raza).lower():    
        nombre = nombre_enanos()
    elif 'humano' in str(raza).lower():
        nombre = nombre_humanos()
    elif 'elfo' in str(raza).lower():
        nombre = nombre_elfos()
    elif 'mago' in str(raza).lower():
        nombre = nombre_magos()
    elif 'orco' in str(raza).lower():
        nombre = nombre_orcos()
    elif 'goblin' in str(raza).lower():
        nombre = nombre_goblins()
    elif 'trol' in str(raza).lower():
        nombre = nombre_trols()
    
    return nombre

# Generador de edad basado en la raza
def generador_edad(raza):
    edad = 0
    
    if 'enano' in str(raza).lower():    
        edad = random.randint(15, 150)  # Edad de 15 a 150 años
    elif 'humano' in str(raza).lower():
        edad = random.randint(10, 50)  # Edad de 15 a 150 años
    elif 'elfo' in str(raza).lower():
        edad = random.randint(30, 2000)  # Edad de 15 a 150 años
    elif 'mago' in str(raza).lower():
        edad = random.randint(7000, 80000)  # Edad de 15 a 150 años
    elif 'orco' in str(raza).lower():
        edad = random.randint(30, 300)  # Edad de 15 a 150 años
    elif 'goblin' in str(raza).lower():
        edad = random.randint(5, 80)  # Edad de 15 a 150 años
    elif 'trol' in str(raza).lower():
        edad = random.randint(600, 2500)  # Edad de 15 a 150 años

    return edad

# Generador de género
def generador_genero():
    return random.choices(['♂', '♀'], weights=[50, 50], k=1)[0]

# Generador de salud del enano
def generador_salud():
    estados = ['Saludable', 'Herido', 'Enfermo', 'Lisiado']
    return random.choices(estados, weights=[70, 15, 10, 5], k=1)[0]

# Generador de posición social
def generador_posicion_social():
    posiciones = ['Ciudadano', 'Soldado', 'Capataz', 'Noble', 'Rey/Reina']
    return random.choices(posiciones, weights=[70, 10, 10, 5, 5], k=1)[0]

# Genera las características físicas y mentales del enano
def generar_caracteristicas_ser_racional(raza):
    caracteristicas = None
    
    if 'enano' in str(raza).lower():    
        caracteristicas = {'fuerza': random.randint(1, 7), 
                           'resistencia': random.randint(1, 5),
                           'agilidad': random.randint(1, 5),
                           'intelecto': random.randint(1, 8),
                           'voluntad': random.randint(1, 10)}
    elif 'humano' in str(raza).lower():
        caracteristicas = {'fuerza': random.randint(1, 6), 
                           'resistencia': random.randint(1, 7),
                           'agilidad': random.randint(1, 7),
                           'intelecto': random.randint(1, 8),
                           'voluntad': random.randint(1, 10)}
    elif 'elfo' in str(raza).lower():
        caracteristicas = {'fuerza': random.randint(1, 8), 
                           'resistencia': random.randint(1, 8),
                           'agilidad': random.randint(1, 10),
                           'intelecto': random.randint(1, 10),
                           'voluntad': random.randint(1, 10)}
    elif 'mago' in str(raza).lower():
        caracteristicas = {'fuerza': random.randint(1, 10), 
                           'resistencia': random.randint(1, 5),
                           'agilidad': random.randint(1, 5),
                           'intelecto': random.randint(1, 10),
                           'voluntad': random.randint(1, 10)}
    elif 'orco' in str(raza).lower():
        caracteristicas = {'fuerza': random.randint(1, 8), 
                           'resistencia': random.randint(1, 8),
                           'agilidad': random.randint(1, 7),
                           'intelecto': random.randint(1, 7),
                           'voluntad': random.randint(1, 5)}
    elif 'goblin' in str(raza).lower():
        caracteristicas = {'fuerza': random.randint(1, 2), 
                           'resistencia': random.randint(1, 2),
                           'agilidad': random.randint(1, 3),
                           'intelecto': random.randint(1, 5),
                           'voluntad': random.randint(1, 3)}
    elif 'trol' in str(raza).lower():
        caracteristicas = {'fuerza': random.randint(8, 10), 
                           'resistencia': random.randint(6, 10),
                           'agilidad': random.randint(1, 3),
                           'intelecto': random.randint(1, 3),
                           'voluntad': random.randint(1, 5)}
        
    return caracteristicas

class Personaje:
    def __init__(self, tipo, edad_max, genero, oficios, simbolo):
        self.nombre = generador_nombres(tipo)
        self.edad = generador_edad(tipo)
        self.edad_max = edad_max
        self.genero = generador_genero() if not genero else genero
        self.salud_estado = generador_salud()
        self.posicion_social = generador_posicion_social() if 'mago' not in str(tipo).lower() else None
        self.oficios = oficios
        self.oficio_principal = self.oficios[0] if self.oficios else None  # Primer oficio como principal
        self.caracteristicas = generar_caracteristicas_ser_racional(tipo)
        self.mascota = None
        self.simbolo = simbolo 
        self.disponibilidad = [True, None]
        self.info = self.__repr__()
        self.amigos = set() #Guarda el nombre de los enanos con los que guarda amistad
        self.enemigos = set() #Guarda el nombre de los enanos con los que guarda rivalidad
        self.friends = {}#Un mapa vacio para ver los amigos que puede tener un cierto personaje
        #Y mapearlo segun el tipo de amistad que tienen.
        if "enano" in str(tipo).lower():
            self.tipo = "enano"
        if "humano" in str(tipo).lower():
            self.tipo = "humano"
        if "elfo" in str(tipo).lower():
            self.tipo = "elfo"
        if "orco" in str(tipo).lower():
            self.tipo = "orco"
        if "goblin" in str(tipo).lower():
            self.tipo = "goblin"
        if "trol" in str(tipo).lower():
            self.tipo = "trol"
        if "mago" in str(tipo).lower():
            self.tipo = "mago"
        
    def __repr__(self):
        tipo = str(type(self)).split('.')[1][:-2]
        info = (
            f"{self.simbolo} {tipo} : "
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Género: {self.genero}\n"
            f"Estado de Salud: {self.salud_estado}\n"
            f"Posición Social: {self.posicion_social}\n"
            f"Oficio Principal: {self.oficio_principal[0] if self.oficio_principal else 'Ninguno'}\n"
            f"Oficios: {', '.join([f'{oficio[0]} ({oficio[1]})' for oficio in self.oficios])}\n"
            f"Características: {self.caracteristicas}\n"
        )
        return info
    def show_info(self):
        tipo = str(type(self)).split('.')[1][:-2]
        info = (
        f"{self.simbolo} {tipo} : "
        f"Nombre: {self.nombre}\n"
        f"Edad: {self.edad} años\n"
        f"Género: {self.genero}\n"
        f"Estado de Salud: {self.salud_estado}\n"
        f"Posición Social: {self.posicion_social}\n"
        f"Oficio Principal: {self.oficio_principal[0] if self.oficio_principal else 'Ninguno'}\n"
        f"Oficios: {', '.join([f'{oficio[0]} ({oficio[1]})' for oficio in self.oficios])}\n"
        f"Características: {self.caracteristicas}\n" 
        
        )
        return info
    
    def show_name(self):
        tipo = str(type(self)).split('.')[1][:-2]
        info = (
        f"{self.simbolo} {tipo} : "
        f"Nombre: {self.nombre}\n"
        )
        return info
    
    def show_amigos(self):
        info = ""
        if self.amigos:
            info += "Amigos: \n"
            for amigo in self.amigos:
                info += amigo.show_name() +  "--------------------------------\n"
        else:
            info += f"{self.nombre} aun no tiene amigos"
        
        return info
            
    def show_enemigos(self):
        info = ""
        if self.enemigos:
            info += "Enemigos: \n"
            for enemigo in self.enemigos:
                info += enemigo.show_name() + "--------------------------------\n"
        else:
            info += f"{self.nombre} aun no tiene enemigos"
        
        return info
       
        
    

class Enano(Personaje):
    def __init__(self):
        edad_max = 453
        oficios = self.generador_oficios()
        simbolo = '🧔' 
        super().__init__(type(self), edad_max, None, oficios, simbolo)
        
    def generador_oficios(self):
        niveles = ['Pobre', 'Aprendiz', 'Adecuado', 'Muy Adecuado', 'Experto']
        oficios = ['Minero', 'Albañil', 'Carnicero', 'Cazador', 'Pescador', 
                   'Herrero', 'Joyero', 'Granjero', 'Veterinario', 'Medico', 
                   'Artesano', 'Militar', 'Cocinero', 'Carpintero']
        probabildad_oficios = [30, 20, 10, 20, 15, 10, 5, 15, 3, 3, 10, 10, 15, 10]
        
        p_oficios = []
        
        cant_oficios = random.randint(1, 4)  # Número de oficios
        tempo_oficios = random.choices(oficios, probabildad_oficios, k=cant_oficios)
        tempo_oficios = list(set(tempo_oficios))  # Evitar oficios duplicados
        for of in tempo_oficios:
            nivel = random.choice(niveles)
            p_oficios.append([of, nivel])
        
        return p_oficios      

class Humano(Personaje):
    def __init__(self):
        edad_max = 150
        oficios = self.generador_oficios()
        simbolo = '🙍‍' 
        super().__init__(type(self), edad_max, None, oficios, simbolo)
    
    def generador_oficios(self):
        niveles = ['Pobre', 'Aprendiz', 'Adecuado', 'Muy Adecuado', 'Experto']
        oficios = ['Minero', 'Albañil', 'Carnicero', 'Cazador', 'Pescador', 
                   'Herrero', 'Joyero', 'Granjero', 'Veterinario', 'Medico', 
                   'Artesano', 'Militar', 'Cocinero', 'Carpintero']
        probabildad_oficios = [5, 20, 15, 20, 20, 15, 3, 25, 5, 10, 10, 20, 5, 10]
        
        p_oficios = []
        
        cant_oficios = random.randint(1, 4)  # Número de oficios
        tempo_oficios = random.choices(oficios, probabildad_oficios, k=cant_oficios)
        tempo_oficios = list(set(tempo_oficios))  # Evitar oficios duplicados
        for of in tempo_oficios:
            nivel = random.choice(niveles)
            p_oficios.append([of, nivel])
        
        return p_oficios   
    
class Elfo(Personaje):    
    def __init__(self):
        edad_max = 7000
        oficios = self.generador_oficios()
        simbolo = '🧝‍'  
        super().__init__(type(self), edad_max, None, oficios, simbolo)
    
    def generador_oficios(self):
        niveles = ['Aprendiz', 'Adecuado', 'Muy Adecuado', 'Experto']
        oficios = ['Minero', 'Albañil', 'Carnicero', 'Cazador', 'Pescador', 
                   'Herrero', 'Joyero', 'Granjero', 'Veterinario', 'Medico', 
                   'Artesano', 'Militar', 'Cocinero', 'Carpintero']
        probabildad_oficios = [0, 10, 5, 0, 0, 5, 25, 15, 20, 30, 15, 35, 5, 20]
        
        p_oficios = []
        
        cant_oficios = random.randint(1, 4)  # Número de oficios
        tempo_oficios = random.choices(oficios, probabildad_oficios, k=cant_oficios)
        tempo_oficios = list(set(tempo_oficios))  # Evitar oficios duplicados
        for of in tempo_oficios:
            nivel = random.choice(niveles)
            p_oficios.append([of, nivel])
        
        return p_oficios 

class Mago(Personaje):
    def __init__(self):
        edad_max = 100000
        oficios = self.generador_habilidades()
        simbolo = '🧙‍'  
        super().__init__(type(self), edad_max, '♂', oficios, simbolo)
    
    def generador_habilidades(self):
        niveles = ['Pobre', 'Adecuado', 'Muy Adecuado', 'Experto']
        habilidades = [['Lluvia', 'Granizo', 'Meteoro'], 
                       ['Terremoto', 'Tormenta de Arena', 'Fallas Tectónicas', 'Deslabe'],
                       ['Fuego', 'Iluminar', 'Aliento de Dragón', 'Nube de Humo'],
                       ['Peste', 'Escases de Recursos', 'Envenamiento', 'Control Lunar'],
                       ['Invocar Bestias', 'Tranformación en Bestia', 'Antidotos', 'Sanar']]
        
        tempo_habilidades = []
        for h in habilidades:
            for l in h:
                tempo_habilidades.append(l)
                        
        for i in range(random.randint(2, 3)):
            habilidades = random.choice(tempo_habilidades)
            
        tempo_habilidades = list(set(habilidades))  # Evitar oficios duplicados
        habilidades = []
        for h in tempo_habilidades:
            nivel = random.choice(niveles)
            habilidades.append([h, nivel])
        
        return habilidades    

class Orco(Personaje):
    def __init__(self):
        edad_max = 1000
        oficios = self.generador_oficios()
        simbolo = '👹'  
        super().__init__(type(self), edad_max, None, oficios, simbolo)
    
    def generador_oficios(self):
        niveles = ['Aprendiz', 'Adecuado', 'Muy Adecuado', 'Experto']
        oficios = ['Minero', 'Albañil', 'Carnicero', 'Cazador', 'Pescador', 
                   'Herrero', 'Joyero', 'Granjero', 'Veterinario', 'Medico', 
                   'Artesano', 'Militar', 'Cocinero', 'Carpintero']
        probabildad_oficios = [0, 20, 25, 30, 30, 5, 0, 0, 0, 10, 0, 40, 5, 5]
        
        p_oficios = []
        
        cant_oficios = random.randint(1, 4)  # Número de oficios
        tempo_oficios = random.choices(oficios, probabildad_oficios, k=cant_oficios)
        tempo_oficios = list(set(tempo_oficios))  # Evitar oficios duplicados
        for of in tempo_oficios:
            nivel = random.choice(niveles)
            p_oficios.append([of, nivel])
        
        return p_oficios     
    
class Goblin(Personaje):
    def __init__(self):
        edad_max = 200
        oficios = self.generador_oficios()
        simbolo = '👺'  
        super().__init__(type(self), edad_max, None, oficios, simbolo)
     
    def generador_oficios(self):
        niveles = ['Aprendiz', 'Adecuado']
        oficios = ['Minero', 'Albañil', 'Carnicero', 'Cazador', 'Pescador', 
                   'Herrero', 'Joyero', 'Granjero', 'Veterinario', 'Medico', 
                   'Artesano', 'Militar', 'Cocinero', 'Carpintero']
        probabildad_oficios = [10, 10, 10, 3, 3, 3, 0, 10, 0, 5, 0, 15, 5, 5]
        
        p_oficios = []
        
        cant_oficios = random.randint(1, 3)  # Número de oficios
        tempo_oficios = random.choices(oficios, probabildad_oficios, k=cant_oficios)
        tempo_oficios = list(set(tempo_oficios))  # Evitar oficios duplicados
        for of in tempo_oficios:
            nivel = random.choice(niveles)
            p_oficios.append([of, nivel])
        
        return p_oficios        

class Trol(Personaje):
    def __init__(self):
        edad_max = 5000
        oficios = self.generador_oficios()
        simbolo = '🧌'   
        super().__init__(type(self), edad_max, None, oficios, simbolo)
    
    def generador_oficios(self):
        niveles = ['Muy Adecuado', 'Experto']
        oficios = ['Minero', 'Albañil', 'Carnicero', 'Cazador', 'Pescador', 
                   'Herrero', 'Joyero', 'Granjero', 'Veterinario', 'Medico', 
                   'Artesano', 'Militar', 'Cocinero', 'Carpintero']
        probabildad_oficios = [0, 0, 30, 30, 0, 15, 0, 0, 0, 10, 0, 40, 5, 5]
        
        p_oficios = []
        
        cant_oficios = random.randint(1, 4)  # Número de oficios
        tempo_oficios = random.choices(oficios, probabildad_oficios, k=cant_oficios)
        tempo_oficios = list(set(tempo_oficios))  # Evitar oficios duplicados
        for of in tempo_oficios:
            nivel = random.choice(niveles)
            p_oficios.append([of, nivel])
        
        return p_oficios    
 
def valor_nivel_oficio(oficio):
    niveles = {'Pobre': 1, 
               'Aprendiz': 2, 
               'Adecuado': 3, 
               'Muy Adecuado': 4, 
               'Experto': 5}
    
    oficio, nivel = oficio[0], oficio[1]
    
    return niveles[nivel]    

def lista_personajes():
    return [Enano(), Humano(), Elfo(), Mago(), Orco(), Goblin(), Trol()]


if __name__ == "__main__":
    # Crear un enano y mostrar su información
    personajes = lista_personajes()
    
    for p in personajes:
        print(p, end="\n-----------------------------------\n")

    e = Enano()
    print(type(e))