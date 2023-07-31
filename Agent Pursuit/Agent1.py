from Agent import Agent


class Agent1(Agent):
    def __init__(self, start_node):
        super().__init__(start_node)
        self.environment = None
        self.steps_taken = 0
        self.successful_captures = 0

    def move(self, env, target):
        self.steps_taken += 1
        next_node = self.calculate_best_next_node(env, target.get_current_node())
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

    def calculate_best_next_node(self, env, target_position):
        neighbors = env.get_neighbors(self.current_node)
        best_next_node = -1
        min_distance = float('inf')

        for neighbor in neighbors:
            distance = self.distance_to_target(neighbor, target_position)
            if distance < min_distance:
                min_distance = distance
                best_next_node = neighbor

        return best_next_node

    def distance_to_target(self, node, target_position):
        return abs(node - target_position)

    def reset(self, start_node):
        return Agent1(start_node)
