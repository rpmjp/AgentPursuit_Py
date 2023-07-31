from Agent import Agent


class Agent3(Agent):
    def __init__(self, start_node):
        super().__init__(start_node)
        self.belief_state = [1.0 / 40] * 41
        self.examined_node = start_node
        self.steps_taken = 0
        self.successful_captures = 0

    def move(self, env, target):
        found_target = self.examine_node(target, self.examined_node)
        self.update_belief_state(env, found_target)

    def examine_node(self, target, node):
        return node == target.get_current_node()

    def update_belief_state(self, env, found_target):
        if found_target:
            self.belief_state = [0] * 41
            self.belief_state[self.examined_node] = 1.0
            self.successful_captures += 1
        else:
            new_belief_state = [0] * 41
            for i in range(1, 41):
                neighbors = env.get_neighbors(i)
                for neighbor in neighbors:
                    new_belief_state[neighbor] += self.belief_state[i] / len(neighbors)
            new_belief_state[self.examined_node] = 0
            self.belief_state = new_belief_state

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
        return Agent3(start_node)
