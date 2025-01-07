import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches
def plot_social_net(todos):
    # Crear un grafo
    G = nx.Graph()
    # Agregar nodos (enanos) con sus razas
    
    
    # Agregar aristas con tipos de amistad
    #las aristas las iremos agregando del diccionario "Friends" de los personajes
    # se va a intentar crear un set para evitar amistades duplicadas
    # amistades = [
    #     ("Thorin", "Balin", "hermandad"),
    #     ("Thorin", "Dwalin", "alianza"),
    #     ("Balin", "Dwalin", "hermandad"),
    #     ("Kili", "Fili", "familiar"),
    #     ("Oin", "Gloin", "familiar"),
    #     ("Dori", "Nori", "amistad"),
    #     ("Nori", "Ori", "amistad"),
    #     ("Ori", "Dori", "amistad"),
    #     ("Gloin", "Thorin", "alianza"),
    #     ("Kili", "Thorin", "alianza")
    # ]
    # nodos = {
    #     "Thorin": "Humano",
    #     "Balin": "Enano",
    #     "Dwalin": "Enano",
    #     "Kili": "Enano",
    #     "Fili": "Enano",
    #     "Oin": "Enano",
    #     "Gloin": "Enano",
    #     "Dori": "Enano",
    #     "Nori": "Enano",
    #     "Ori": "Enano"
    # }
    
    
    # # Agregar nodos al grafo
    # for nodo in nodos:
    #     G.add_node(nodo, raza=nodos[nodo])
    nodos = {}
    conexiones = set()
    amistades = []
    for personaje in todos:
        nodos[personaje.nombre] = personaje.tipo #agregar nuevo nodo del personaje
        for key, amigo in personaje.friends.items():
            if ((personaje.nombre, amigo[0], amigo[1]) not in conexiones): #se agrega una tupla de la amistad entre 2 enanos 
                amistades.append((personaje.nombre, amigo[0].nombre, amigo[1]))
                conexiones.add((personaje.nombre, amigo[0].nombre, amigo[1]))
                conexiones.add((amigo[0].nombre, personaje.nombre, amigo[1]))
    #print(nodos)
    
    # Agregar nodos al grafo
    for nodo in nodos:
        G.add_node(nodo, raza=nodos[nodo])
            
    # Agregar aristas al grafo
    for nodo1, nodo2, tipo in amistades:
        G.add_edge(nodo1, nodo2, tipo=tipo)
        
    #print(G.nodes(data=True))
    #print(G.edges(data=True))
    # Definir colores según el tipo de amistad
    colores_aristas = {
        "Amistad cercana": "blue",
        "Amistad amorosa": "green",
        "Amistad de conveniencia": "red",
        "Amistad de oficio": "orange",
        "Amistad casual": "pink"
    }
    
    # Crear una lista de colores para las aristas
    colores = [colores_aristas[G[u][v]['tipo']] for u, v in G.edges]
    
    # Definir colores para las razas
    colores_raza = {
        "enano": "lightblue",
        "humano": "yellow",  # Puedes agregar más razas aquí
        "elfo": "lime",
        "mago": "black",
        "orco": "grey",
        "goblin": "brown",
        "trol": "violet",
    }
    
    # Crear una lista de colores para los nodos basados en su raza
    colores_nodos = [colores_raza[G.nodes[nodo]['raza']] for nodo in G.nodes]
    
    # Crear una lista de etiquetas para los nodos que incluya la raza
    etiquetas = {nodo: f"{nodo}\n({G.nodes[nodo]['raza']})" for nodo in G.nodes}
    
    # Dibujar el grafo
    plt.figure(figsize=(100, 100))
    pos = nx.spring_layout(G, seed=100, k=0.5)  # Disposición de nodos
    
    # Dibujar nodos con colores según su raza
    nx.draw_networkx_nodes(G, pos, node_color=colores_nodos, node_size=500)
    # Dibujar etiquetas con el nombre del enano y su raza
    nx.draw_networkx_labels(G, pos, labels=etiquetas, font_size=10, font_weight="bold")
    # Dibujar aristas con colores según el tipo de amistad
    nx.draw_networkx_edges(G, pos, edge_color=colores, width=2)
    
    # Título
    plt.title("Grafo de Amistades entre Enanos con Razas")
    
    # Mostrar leyenda de razas y tipos de amistad
    leyenda_aristas = [mpatches.Patch(color=color, label=tipo) for tipo, color in colores_aristas.items()]
    leyenda_raza = [mpatches.Patch(color=color, label=raza) for raza, color in colores_raza.items()]
    plt.legend(handles=leyenda_aristas + leyenda_raza, loc="upper left")
    
    plt.show()
    
    
