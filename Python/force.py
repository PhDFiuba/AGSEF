import json
import networkx as nx
import matplotlib.pyplot as plt

json_data = {}
labeldict = {}

criterio_vecinos = {1:'Extreme',2:'Simple',3:'Switch',4:'Crossing'}
criterio_colores = {1:'red',2:'grey',3:'green',4:'yellow',5:'pink',6:'cyan'}

G = nx.Graph()

#%%
def cargar_json(data):

    with open(data) as f:
        json_data = json.loads(f.read())

    i = 0
    for topology in json_data:
        i = i + 1
        print(f'Topologia numero {i}')
        for item in topology:       
            detectar_switch(item)

        agregar_semaforos(topology)

        for item in topology:        
            imprimir_resultados(item)


#%%
def detectar_switch(item):
    vecinos = 0

    if "prev" in item:      
        vecinos += 1
    if "post" in item:
        vecinos += 1
    if "prev_up" in item:
        vecinos += 1
    if "prev_down" in item:
        vecinos += 1
    if "post_up" in item:
        vecinos += 1
    if "post_down" in item:
        vecinos += 1

    item['vecinos'] = vecinos

    if vecinos == 1:
        item['tipo'] = criterio_vecinos[1]
    if vecinos == 2:  
        item['tipo'] = criterio_vecinos[2]    
    if vecinos > 2:  
        item['tipo'] = criterio_vecinos[3]

#%%
def agregar_semaforos(topology):

    #print(topology[0])
    for item in topology:
        print(item)
        if item['tipo'] == criterio_vecinos[3]:
            if "prev" in item:
                topology[item['prev']-1]['semaforo'] = ['>>>','>>']
                topology[item['post']-1]['semaforo'] = ['<<<']
                #topology[item['prev_up']-1]['semaforo'] = ['<<']

    #print(item)        

#%%
def imprimir_resultados(item):
    node_id = item['id']

    labeldict[node_id] = node_id

    prev = "-"
    post = "-"
    prev_up = "-"
    prev_down = "-"
    post_up = "-"
    post_down = "-"
    
    tipo = "-"

    semaforos = "NULL"

    vecinos = 0

    if "prev" in item:
        prev = item['prev']           
        G.add_edge(node_id,prev)
        vecinos += 1
    if "post" in item:
        post = item['post']
        G.add_edge(node_id,post)
        vecinos += 1
    if "prev_up" in item:
        prev_up = item['prev_up']
        G.add_edge(node_id,prev_up)
        vecinos += 1
    if "prev_down" in item:
        prev_down = item['prev_down']
        G.add_edge(node_id,prev_down)
        vecinos += 1
    if "post_up" in item:
        post_up = item['post_up']
        G.add_edge(node_id,post_up)
        vecinos += 1
    if "post_down" in item:
        post_down = item['post_down']
        G.add_edge(node_id,post_down)
        vecinos += 1
    if "semaforo" in item:
        semaforos = item['semaforo']
    if "tipo" in item:
        tipo = item['tipo']

    print(f'[{node_id}]:|{prev}|{post}|{post_up}|{post_down}|{prev_down}|{prev_up}|-> {vecinos} |{tipo}| {semaforos}')  


#%%#%%
def analizar_grafo():
    
    print('Nodos:',G.nodes()) 
    print('Aristas:',G.edges())  

    N_vecinos = {}
    N_color = []
    Nodos = []
    cambios = []
    
    for i in G.nodes():
        cantidad = len([n for n in G.neighbors(i)])
        N_vecinos[i] = cantidad
        Nodos.append(i)
        
        N_color.append(criterio_colores[N_vecinos[i]])
        
        if cantidad == 3:
            cambios.append(i)    

    for i in cambios:
        criticos = [n for n in G.neighbors(i)]
            
        N_color[Nodos.index(criticos[0])] = criterio_colores[4]
        N_color[Nodos.index(criticos[1])] = criterio_colores[5]
        N_color[Nodos.index(criticos[2])] = criterio_colores[6] 
      
    for i in cambios:
        N_color[Nodos.index(i)] = criterio_colores[3]
        
    for i in G.nodes():
        print(f'Nodo {i}: tipo {criterio_vecinos[N_vecinos[i]]}') 
        
    return N_color
    

    
#%%
cargar_json('solucion.json')
#N_color = analizar_grafo()
    
#plt.subplot(121)
#nx.draw(G , labels = labeldict, with_labels=True, node_size=1000, node_color=N_color )

nx.draw(G , labels = labeldict , with_labels=True, node_size=1000)

plt.show()




    




    

