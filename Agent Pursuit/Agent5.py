from Agent import Agent

from collections import deque
import random


class Agent5(Agent):
    def __init__(self, start_node):
        super().__init__(start_node)
        self.belief_state = [1.0 / 40] * 41
        self.visited_nodes = {start_node}
        self.rand = random.Random()
        self.steps_taken = 0
        self.successful_captures = 0

    def move(self, env, target):
        target_node = target.get_current_node()
        for i in range(1, 41):
            transition_prob = 0.8 if i == target_node else 0.2 / 39
            self.belief_state[i] *= transition_prob

        total_belief = sum(self.belief_state)
        for i in range(1, 41):
            self.belief_state[i] /= total_belief

        shortest_path_node = self.bfs_shortest_path(env, self.current_node, target_node)
        self.current_node = shortest_path_node
        self.belief_state[self.current_node] = 0
        for neighbor in env.get_neighbors(self.current_node):
            self.belief_state[neighbor] += 1.0 / len(env.get_neighbors(neighbor))
        self.steps_taken += 1

    def bfs_shortest_path(self, env, start_node, target_node):
        queue = deque([start_node])
        visited = [False] * 41
        visited[start_node] = True
        parent = [-1] * 41

        while queue:
            current_node = queue.popleft()
            if current_node == target_node:
                next_node = target_node
                while parent[next_node] != start_node:
                    next_node = parent[next_node]
                return next_node

            for neighbor in env.get_neighbors(current_node):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current_node

        return start_node

    def capture(self, target):
        captured = self.get_current_node() == target.get_current_node()
        if captured:
            self.successful_captures += 1
            self.belief_state = [0] * 41
            self.belief_state[target.get_current_node()] = 1
        return captured

    def get_steps_taken(self):
        return self.steps_taken

    def get_successful_captures(self):
        return self.successful_captures

    def reset(self, start_node):
        return Agent5(start_node)

    def get_current_node(self):
        return self.current_node
