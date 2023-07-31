from Agent import Agent


class Agent0(Agent):
    def __init__(self, start_node):
        super().__init__(start_node)
        self.steps_taken = 0
        self.successful_captures = 0
        self.environment = None  # Add a class member to store the Environment instance

    def move(self, env, target):
        # note Agent 0 does not move
        pass

    def capture(self, target):
        captured = self.current_node == target.get_current_node()
        if captured:
            # Increment successful captures
            self.successful_captures += 1
        return captured

    def get_steps_taken(self):
        return self.steps_taken

    def get_successful_captures(self):
        return self.successful_captures

    def reset(self, start_node):
        return Agent0(start_node)
