import numpy as np 
import networkx as nx
import matplotlib

class Visualization():
    def __init__(self, cities, mapping):
        self.cities = cities
        self.mapping = mapping
        self.overlay = np.zeros((len(cities),len(cities)))
        
    
    def show_distances(self, distance):
        self.overlay[distance != 0 ] = 1 
        self.G = nx.from_numpy_matrix(distance)
        for n,city in zip(range(len(self.G.nodes)),self.cities):
            self.G.nodes[n]['city'] = city
        self.G = nx.relabel_nodes(self.G, self.mapping)
        self.pos = nx.planar_layout(self.G)
        self.dlabels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx(self.G, self.pos)
        self.network_edge_labels = nx.draw_networkx_edge_labels(self.G,self.pos,edge_labels=self.dlabels)
    
    def show_pheromones(self, pheromones, state = -1):
        pheromones = pheromones*self.overlay
        pheromone_graph = nx.from_numpy_matrix(pheromones)
        color_map = []
        if state != -1:
            for node in pheromone_graph:
                if node == state:
                    color_map.append('red')
                else: 
                    color_map.append('blue')
        else: 
            for node in pheromone_graph:
                color_map.append('blue')
        pheromone_graph= nx.relabel_nodes(pheromone_graph, self.mapping)
        labels = nx.get_edge_attributes(pheromone_graph,'weight')
        labels = {(key1,key2): "{:.2f}".format(mes) for (key1,key2), mes in labels.items()}
        pos=nx.planar_layout(pheromone_graph)
        nx.draw_networkx(pheromone_graph,pos,node_color=color_map)

        self.network_edge_labels = nx.draw_networkx_edge_labels(pheromone_graph,pos,edge_labels=labels)
        print('Updated pheromones')