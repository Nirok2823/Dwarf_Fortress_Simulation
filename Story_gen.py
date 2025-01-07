import random
import time

locations = {
    "Agua": ["un lago cristalino", "un pozo encantado", "una caverna húmeda"],
    "Talar": ["un bosque antiguo", "un claro maldito", "un bosque protegido por dríadas"],
    "Alimento": ["un campo fértil", "un huerto abandonado", "un mercado clandestino"],
    "Minar": ["una mina olvidada", "un túnel prohibido", "una cueva repleta de cristales"],
    "Comerciar": ["una feria bulliciosa", "un pueblo fronterizo", "un puerto lleno de piratas"],
    "Atacar": ["un campamento de goblins", "una guarida de bandidos", "un convoy de orcos"],
}

actions = {
    "aventura": {
        "verbos": ["exploran", "descubren", "enfrentan", "se adentran", "viajan"],
        "escenarios": ["una cueva oscura", "un bosque encantado", "un volcán activo", "un laberinto subterráneo"],
        "artefactos": ["un mapa antiguo", "una espada mágica", "una gema reluciente", "una brújula rota"],
        "enemigos": ["dragones", "trolls gigantes", "goblins malvados", "lobos feroces"],
    },
    "confrontacion": {
        "verbos": ["se desafían", "se atacan", "se enfrentan", "luchan", "se retan"],
        "escenarios": ["en un puente colgante", "en el bosque", "en el lago", "en un valle lleno de niebla"],
        "artefactos": ["hachas gemelas", "escudos pesados", "bombas de alquimia", "espadas de fuego"],
        "enemigos": [],
    },
    "evasión": {
        "verbos": ["escapan", "huyen", "se esconden", "se deslizan", "desaparecen"],
        "escenarios": ["en un túnel oscuro", "bajo la lluvia torrencial", "entre las rocas", "en una ciudad desierta"],
        "artefactos": ["una capa de invisibilidad", "un amuleto de sigilo", "un mapa secreto", "una piedra de teletransportación"],
        "enemigos": ["patrullas enemigas", "monstruos dormidos", "vigías vigilantes", "bandidos buscando presa"],
    },
    "hacer_amigos": {
        "verbos": ["comparten", "conversan", "se ayudan", "aprecian", "se cuidan mutuamente"],
        "escenarios": ["la iglesia", "junto a un fuego de campamento", "en una taberna local", "en un campo fértil"],
        "artefactos": ["Chaskas", "Doritos", "Cerveza de Raiz", "Monedas de Oro"],
        "enemigos": [],
    },
    "ignorar": {
        "verbos": ["evitan", "ignoran", "desaparecen", "no prestan atención", "se alejan"],
        "escenarios": ["en una calle concurrida", "en el mercado de una ciudad", "en un bosque lejano", "en una montaña remota"],
        "artefactos": [],
        "enemigos": [],
    },
}
personalities = [
    "es valiente pero impulsivo",
    "es astuto pero desconfiado",
    "es bondadoso pero ingenuo",
    "es reservado pero muy sabio",
    "es ambicioso pero orgulloso",
    "es generoso pero testarudo",
]

def adventure_story(enano_a, enano_b):
    action = actions["aventura"]
    verb = random.choice(action["verbos"])
    escenario = random.choice(action["escenarios"])
    artefacto = random.choice(action["artefactos"])
    enemigo = random.choice(action["enemigos"])
    
    return f"{enano_a} y {enano_b} {verb} {escenario} en busca de {artefacto}. Durante su viaje, se encuentran con un grupo de {enemigo}, pero logran salir victoriosos."

def confrontation_story(enano_a, enano_b):
    action = actions["confrontacion"]
    verb = random.choice(action["verbos"])
    escenario = random.choice(action["escenarios"])
    artefacto = random.choice(action["artefactos"])
    #enemigo = random.choice(action["enemigos"])
    
    print(f"{enano_a} y {enano_b} {verb} en {escenario}. Armados con {artefacto}, luchan ferozmente contra si mismos.")

def evade_story(enano_a, enano_b):
    action = actions["evasión"]
    verb = random.choice(action["verbos"])
    escenario = random.choice(action["escenarios"])
    artefacto = random.choice(action["artefactos"])
    
    print(f"{enano_a} y {enano_b} {verb} silenciosamente por {escenario}, usando {artefacto} para evitar ser detectados por sus perseguidores.")

def make_friend_story(enano_a, enano_b):
    action = actions["hacer_amigos"]
    verb = random.choice(action["verbos"])
    escenario = random.choice(action["escenarios"])
    artefacto = random.choice(action["artefactos"])
    
    print(f"{enano_a} y {enano_b} {verb} en {escenario}. Durante su tiempo juntos, comparten historias y tesoros como {artefacto}, creando una amistad verdadera.")

def ignore_story(enano_a, enano_b):
    action = actions["ignorar"]
    verb = random.choice(action["verbos"])
    escenario = random.choice(action["escenarios"])
    
    print(f"{enano_a} y {enano_b} se cruzan en {escenario}. Sin embargo, ambos deciden {verb} y continuar con sus caminos sin hablarse.")

# Generador de historia con decisiones dinámicas
def gen_story(accion, enano, todos):
    # Si son amigos
    enano_a = enano
    enano_b = todos
    while enano_a.nombre == enano_b.nombre:
        enano_b = random.choice(todos)
        
    if enano_b in enano_a.amigos:
        print(f"\nEl {enano_a.tipo} {enano_a.nombre} se encuentra con su amigo, el {enano_b.tipo} {enano_b.nombre}.")
        decision = random.randint(1, 2)
        print()
        if decision == 1:
            return adventure_story(enano_a.nombre, enano_b.nombre)
        else:
            return "Deciden seguir cada uno por su camino por ahora.\n"
            
    """ por el momento quitamos todos los demas casos de enemigos y se dejo el de aventura por cualquier cosa"""
    # # Si son enemigos
    # elif enano_b in enano_a.enemigos:
    #     print(f"\nEl Enano {enano_a.nombre} se encuentra con su enemigo, el Enano B {enano_b.nombre}.")
    #     decision = input("¿Quieres evadirlo o confrontarlo? (evadir/confrontar): ").strip().lower()
    #     print()
    #     if decision == "confrontar":
    #         confrontation_story(enano_a.nombre, enano_b.nombre)
    #     else:
    #         evade_story(enano_a.nombre, enano_b.nombre)
    # # Si no tienen relación previa
    # else:
    #     location = random.choice(locations.get(accion, ["un lugar misterioso"]))
    #     enano_a_personality = random.choice(personalities)
    #     enano_b_personality = random.choice(personalities)
        
    #     print(f"\nEl Enano {enano_a.nombre}, quien {enano_a_personality}, quien se encontraba en {location}.")
    #     print(f"Se encuentra con el Enano {enano_b.nombre}, quien {enano_b_personality}.\n")
    #     print(f"¿Cómo reaccionará el {enano_a.nombre}?")
    #     print(f"1. Ofrecer amistad a {enano_b.nombre}.")
    #     print(f"2. Desconfiar y enfrentarse a {enano_b.nombre}.")
    #     print(f"3. Ignorar a {enano_b.nombre} y continuar con su tarea.")
    #     choice = input("Elige una opción (1, 2, 3): ").strip()
    #     print()
    #     if choice == "1":
    #         enano.amigos.add(enano_b)
    #         if enano_b.amigos :
    #             for enanos in enano_b.amigos:
    #                 if enanos.nombre != enano.nombre:
    #                     enano.amigos.add(enanos)
                    
    #         enano_b.amigos.add(enano)       
    #         if enano.amigos :
    #             for enanos in enano.amigos:
    #                 if enanos.nombre != enano_b.nombre:
    #                     enano_b.amigos.add(enanos)
                    
    #         make_friend_story(enano_a.nombre, enano_b.nombre)
            
    #     elif choice == "2":
    #         enano.enemigos.add(enano_b)
    #         """
    #         if enano_b.enemigos :
    #             for enanos in enano_b.enemigos:
    #                 if enanos.nombre != enano_b.nombre:
    #                     enano.enemigos.add(enanos)
    #         """       
    #         enano_b.enemigos.add(enano) 
    #         """
    #         if enano.enemigos :
    #             for enanos in enano.enemigos:
    #                 if enanos.nombre != enano_b.nombre:
    #                     enano_b.enemigos.add(enanos)
    #         """
    #         confrontation_story(enano_a.nombre, enano_b.nombre)
    #     else:
    #         ignore_story(enano_a.nombre, enano_b.nombre)
        
    input("Press Enter to continue...")

# Simulación
"""
while True:
    accion = input("\nElige una acción: recolectar agua, talar, recolectar alimento, minar, comerciar, atacar: ").strip()
    enano_a = input("Introduce el nombre del Enano A: ").strip()
    enano_b = input("Introduce el nombre del Enano B: ").strip()
    
    interactive_story(accion, enano_a, enano_b)
    
    another = input("¿Quieres jugar otra ronda? (sí/no): ").strip().lower()
    if another != "sí":
        break
"""
