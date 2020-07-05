import json
import networkx as nx



with open('data.json') as f:
    json_data = json.loads(f.read())

G = nx.Graph()


labeldict = {}
for item in json_data['secciones']:
    
    central = item['id']
    vecinos = item['vecino']
    
    print(central,vecinos)
    
    labeldict[central] = item['nombre']
    
    if isinstance(vecinos,list):
        for i in vecinos:
            G.add_edge(central,i,labels="cacho")


nx.draw(G , labels = labeldict, with_labels=True)