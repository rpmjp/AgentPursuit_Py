from Agent import Agent

from collections import deque


class Agent2(Agent):
    def __init__(self, start_node):
        super().__init__(start_node)
        self.steps_taken = 0
        self.successful_captures = 0

    def move(self, env, target):
        self.steps_taken += 1
        shortest_path = self.find_shortest_path(env, target.get_current_node())
        if len(shortest_path) > 1:
            next_node = shortest_path[1]
            self.current_node = next_node

    def capture(self, target):
        captured = self.get_current_node() == target.get_current_node()
        if captured:
            self.successful_captures += 1
        return captured

    def get_steps_taken(self):
        return self.steps_taken

    def get_successful_captures(self):
        return self.successful_captures

    def get_current_node(self):
        return self.current_node

    def find_shortest_path(self, env, target_node):
        queue = deque()
        visited = set()
        queue.append([self.current_node])
        visited.add(self.current_node)

        while queue:
            path = queue.popleft()
            current_node = path[-1]

            if current_node == target_node:
                return path

            for neighbor in env.get_neighbors(current_node):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    visited.add(neighbor)

        return []

    def reset(self, start_node):
        return Agent2(start_node)
