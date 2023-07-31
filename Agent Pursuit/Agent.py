from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, start_node):
        self.current_node = start_node
        self.steps_taken = 0
        self.successful_captures = 0

    @abstractmethod
    def move(self, env, target):
        pass

    @abstractmethod
    def capture(self, target):
        pass

    def increment_steps_taken(self):
        self.steps_taken += 1

    def increment_successful_captures(self):
        self.successful_captures += 1

    @abstractmethod
    def get_steps_taken(self):
        pass

    def get_successful_captures(self):
        return self.successful_captures

    @abstractmethod
    def reset(self, start_node):
        pass
