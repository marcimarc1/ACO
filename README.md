# ACO
## Ant Colony Optimization

Ant Colony Optimization was introduced by Marco Dorigo in 1992. 
In the algorithm a population of artificial ants are used to find the shortest path in a Graph.
It is an algorithm inspired by nature and the mechanism of ants finding food and communicating their paths via pheromones.

## Requirements
The whole alogrithm is calculated with numpy and networkx and matplotlib are just needed for visualization

```
pip install numpy
pip install networkx
pip install matplotlib
```


## Functionality
Ant colony optimization have the working horse, that ants chose a random path first, and later due to the deposite of pheromone, which every other ant can access find an optimal path regarding the heuristic.

1. initialize the graph with 0 or constant pheromones.
2. calculate the transition probability with $ p(c_j|s) = \frac{t_{ij}^ \alpha \eta_{ij}^\beta}{\sum_i t_{ij}^ \alpha \eta_{ij}^\beta}$ from one node to the following nodes
3. update the pheromones on the path taken, with an optional decay factor $\tau_{ij} \leftarrow (1-\rho)* \tau_{ij} + \rho* \sum F(s)$
## Repo Information
- In the File AntColony.py are the classes for the ant colony optimization for finding a shortest path between 2 nodes (no parallelization yet)
- visualization.py has a visualization class for visualization the single steps of the ACO algorithm on a graph
- explain_the_algorithm contains the explanation of the algorithm
