import random


class Target:
    def __init__(self, environment, start_node):
        self.current_node = start_node  # The current node where the target is located
        self.rand = random.Random()  # Random object used to select the next move
        self.steps_taken = 0  # Step counter
        self.environment = environment  # The environment in which the target is moving

    def move(self, env):
        # Moves the target to a randomly selected neighboring node
        # Increments the step counter every time the target moves
        neighbors = env.get_neighbors(self.current_node)
        self.current_node = neighbors[self.rand.randint(0, len(neighbors) - 1)]
        self.steps_taken += 1  # Increment the step counter every time the target moves

    def get_current_node(self):
        # Returns the current node where the target is located
        return self.current_node

    def get_steps_taken(self):
        # Returns the number of steps taken by the target
        return self.steps_taken

    def get_environment(self):
        # Returns the environment in which the target is moving
        return self.environment
