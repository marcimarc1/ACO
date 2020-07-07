import numpy as np
import networkx as nx
import matplotlib
from visualization import *

from AntColony import *


distance = np.array( [[0, 1, 5, 0, 0, 0], #Tübingen
                      [1, 0, 2, 0, 0, 0], #Stuttgart
                      [5, 2, 0, 4, 3, 0], #Ulm
                      [0, 0, 4, 0, 2, 2], #Memmingen
                      [0, 0, 3, 2, 0, 2], #Augsburg
                      [0, 0, 0, 2, 2, 0]])#München

pheromone = np.ones(distance.shape)/len(distance) #initialize the pheromones constant over the graph
all_inds = range(len(distance))
decay = 0.9
alpha = 1
beta = 1
update_factor = 1/len(distance)

Colony = AntColony(distance=distance, n_iterations=100, n_ants=100, alpha=1, beta=1, rho=0.5)
#Start: Tübingen , Goal: München
Colony.run(start=0, goal=5)
print(Colony.pheromone_path(0,5))
