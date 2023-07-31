from Agent import Agent


import random

class Agent4(Agent):
    def __init__(self, start_node):
        super().__init__(start_node)
        self.belief_state = [1.0 / 40] * 41
        self.rand = random.Random()
        self.steps_taken = 0
        self.successful_captures = 0
        self.env = None

    def move(self, env, target):
        self.env = env
        self.steps_taken += 1
        self.current_node = self.best_move()

    def best_move(self):
        best_nodes = []
        max_belief = 0
        for i in range(1, 41):
            if self.belief_state[i] > max_belief:
                best_nodes.clear()
                best_nodes.append(i)
                max_belief = self.belief_state[i]
            elif self.belief_state[i] == max_belief:
                best_nodes.append(i)
        return best_nodes[self.rand.randint(0, len(best_nodes) - 1)]

    def capture(self, target):
        self.env = target.get_environment()
        captured = target.get_current_node() == self.current_node
        if captured:
            self.belief_state = [0] * 41
            self.belief_state[self.current_node] = 1
            self.successful_captures += 1
            return True
        else:
            self.belief_state[self.current_node] = 0
            for neighbor in self.env.get_neighbors(self.current_node):
                self.belief_state[neighbor] += 1.0 / len(self.env.get_neighbors(neighbor))
            return False

    def get_steps_taken(self):
        return self.steps_taken

    def get_successful_captures(self):
        return self.successful_captures

    def reset(self, start_node):
        return Agent4(start_node)
