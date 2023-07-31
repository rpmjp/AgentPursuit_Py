from Agent import Agent
import random
from Particle import Particle

import heapq
from collections import defaultdict


class Agent7(Agent):
    def __init__(self, start_node):
        super().__init__(start_node)
        self.NUM_PARTICLES = 200
        self.particles = [Particle(random.randint(1, 40)) for _ in range(self.NUM_PARTICLES)]
        self.rand = random.Random()
        self.steps_taken = 0
        self.successful_captures = 0
        self.last_known_target_position = start_node
        self.transition_matrix = [[0.0] * 41 for _ in range(41)]
        self.observation_counts = [[0] * 41 for _ in range(41)]
        self.belief_state = [1.0 / 40] * 41
        self.initialize_particles()
        self.initialize_transition_matrix()

    def move(self, env, target):
        self.steps_taken += 1
        predicted_position = self.predict_next_position()
        examined_node = self.get_highest_probability_node()
        if target.get_current_node() == examined_node:
            self.update_particles(target.get_current_node())
        else:
            self.update_belief_state(env, examined_node)

        dist = defaultdict(lambda: float('inf'))
        prev = {}
        dist[self.current_node] = 0.0
        queue = [(0.0, self.current_node)]

        while queue:
            _, node = heapq.heappop(queue)
            for neighbor in env.get_neighbors(node):
                new_dist = dist[node] + self.distance_to_target(node, neighbor)
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = node
                    heapq.heappush(queue, (new_dist, neighbor))

        self.current_node = self.get_closest_neighbor(env, self.get_highest_probability_node())

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
        return Agent7(start_node)

    def update_belief_state(self, env, examined_node):
        likelihoods = [1.0 / (self.distance_to_target(examined_node, i) + 1) for i in range(41)]
        self.observation_counts[self.last_known_target_position][examined_node] += 1

        for i in range(1, 41):
            total_count = sum(self.observation_counts[self.last_known_target_position])
            if total_count > 0:
                self.transition_matrix[self.last_known_target_position][i] = \
                self.observation_counts[self.last_known_target_position][i] / total_count

        self.update_belief_state_with_hmm(examined_node)
        self.last_known_target_position = examined_node

    def update_belief_state_with_hmm(self, examined_node):
        new_belief_state = [0.0] * 41
        for i in range(1, 41):
            prob = sum(self.belief_state[j] * self.transition_matrix[j][i] for j in range(1, 41))
            new_belief_state[i] = prob

        self.belief_state = new_belief_state
        total_belief = sum(self.belief_state)
        self.belief_state = [belief / total_belief for belief in self.belief_state]

    def predict_next_position(self):
        return sum(particle.get_position() for particle in self.particles) // self.NUM_PARTICLES

    def distance_to_target(self, node, target_position):
        return abs(node - target_position)

    def initialize_transition_matrix(self):
        initial_prob = 0.025
        for i in range(1, 41):
            for j in range(1, 41):
                if i == j:
                    self.transition_matrix[i][j] = initial_prob
                elif abs(i - j) == 1:
                    self.transition_matrix[i][j] = (1.0 - initial_prob) / 3

    def initialize_particles(self):
        pass  # Particles are already initialized in the constructor

    def update_particles(self, target_position):
        for particle in self.particles:
            particle.set_position(target_position)

    def get_closest_neighbor(self, env, target_position):
        neighbors = env.get_neighbors(self.current_node)
        closest_neighbor = min(neighbors, key=lambda neighbor: self.distance_to_target(neighbor, target_position))
        return closest_neighbor

    def get_highest_probability_node(self):
        return max(range(1, 41), key=lambda i: self.belief_state[i])
