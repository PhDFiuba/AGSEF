import json
import networkx as nx



json_data = {}
labeldict = {}

criterio_vecinos = {1:'Extremo',2:'Simple',3:'Cambio',4:'Desvio'}
criterio_colores = {1:'red',2:'grey',3:'green',4:'yellow',5:'pink',6:'cyan'}

G = nx.Graph()

#%%
def cargar_json(data):

    with open(data) as f:
        json_data = json.loads(f.read())
        
    for item in json_data['secciones']:
    
        central = item['id']
        vecinos = item['vecino']
    
        #print(central,vecinos)
    
        labeldict[central] = item['nombre']
        #color_map[central] = 'blue'
    
        if isinstance(vecinos,list):
            for i in vecinos:
                G.add_edge(central,i)
   
#%%
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
cargar_json('data_1.json')
N_color = analizar_grafo()
    

nx.draw(G , labels = labeldict, with_labels=True, node_size=1000, node_color=N_color )









    




    

