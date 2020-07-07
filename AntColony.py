import numpy as np 
class AntColony():

    def __init__(self, distance, n_ants=1, n_iterations=100, rho=0.5, alpha= 1, beta = 1):
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.rho = rho
        self.alpha, self.beta = alpha, beta

        self.distance = distance
        self.pheromone = np.ones(distance.shape)/len(distance) #initialize the pheromones constant over the graph
        self.all_inds = range(len(distance))
        self.update_factor = 1/len(distance)    # could also be altered, but is constant in this colony
        self.ants = [Ant(rho, alpha, beta) for i in range(n_ants)]

    
    def run(self, start, goal):
        ph = np.zeros_like(self.pheromone)
        for ant in self.ants:
            ph += ant.run(start, goal, self.pheromone, self.distance)
        self.pheromone = ph/len(self.ants) 
    
    def pheromone_path(self,start, goal):
        state = start
        path = list()
        while state != goal:
            path.append(state)
            state = np.argmax(self.pheromone[state])
        path.append(goal)
        return path
    

    

class Ant():
    def __init__(self,rho = 0.5, alpha = 1, beta = 1):
        self.rho, self.alpha, self.beta = rho, alpha, beta
        self.update_factor = 1/5

    def run(self, start, goal, pheromone, dist):
        state = start
        visited = []
        while state != goal:
            _, move, Flag = self.probabilities(pheromone, dist, state, visited)
            if Flag == True:
                return np.zeros_like(pheromone)
            visited.append(state)
            state = move
            pheromone = self.update_pheromones(pheromone, visited[-1], state)

        return pheromone
    
    def probabilities(self, pheromone, dist, state, visited):
        dist = 1/dist
        all_inds = range(len(dist))
        pheromone = np.copy(pheromone)
        d = dist[state]
        d[list(visited)] = 0
        d[d == np.inf] = 0
        row = pheromone[state] ** self.alpha * (d ** self.beta)
        row[row == np.inf] = 0
        norm_row = row / row.sum()
        try:
            move = np.random.choice(all_inds, 1, p=norm_row)[0]
            Flag = False
        except:
            move = 0
            Flag = True
        return norm_row, move, Flag

    def update_pheromones(self, pheromones, last_state, state):
        up = np.zeros(pheromones[state].shape)
        up[state] = 1*self.update_factor
        pheromones[last_state] = (1-self.rho)*pheromones[state] + self.rho * up
        return pheromones