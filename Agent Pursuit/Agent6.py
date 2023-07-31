from Agent import Agent


import random

class Agent6(Agent):
    def __init__(self, start_node):
        super().__init__(start_node)
        self.belief_state = [1.0 / 40] * 41
        self.rand = random.Random()
        self.steps_taken = 0
        self.successful_captures = 0

    def move(self, env, target):
        self.update_belief_state_and_best_move(env, target)

    def update_belief_state_and_best_move(self, env, target):
        examined_node = self.examine_node()
        self.update_belief_state(env, target, examined_node)
        next_node = self.best_move(env, examined_node)
        if next_node != self.current_node:
            self.steps_taken += 1
            self.current_node = next_node

    def examine_node(self):
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

    def update_belief_state(self, env, target, examined_node):
        if target.get_current_node() == examined_node:
            self.belief_state = [0] * 41
            self.belief_state[examined_node] = 1
        else:
            self.belief_state[examined_node] = 0
            for neighbor in env.get_neighbors(examined_node):
                self.belief_state[neighbor] += 1.0 / len(env.get_neighbors(neighbor))

    def best_move(self, env, examined_node):
        neighbors = env.get_neighbors(self.current_node)
        best_node = self.current_node
        current_distance = abs(self.current_node - examined_node)
        for neighbor in neighbors:
            new_distance = abs(neighbor - examined_node)
            if new_distance < current_distance:
                best_node = neighbor
                current_distance = new_distance
        return best_node

    def capture(self, target):
        captured = self.current_node == target.get_current_node()
        if captured:
            self.successful_captures += 1
        return captured

    def get_steps_taken(self):
        return self.steps_taken

    def get_successful_captures(self):
        return self.successful_captures

    def reset(self, start_node):
        return Agent6(start_node)
