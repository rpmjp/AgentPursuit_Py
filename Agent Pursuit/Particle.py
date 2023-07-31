import random
import numpy as np


class Particle:
    def __init__(self, position):
        self.position = position
        self.weight = 1.0

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def update(self, likelihoods, transition_matrix, particles, NUM_PARTICLES):
        # Particle Filter update step
        new_position = self.predict_next_position(transition_matrix)
        weight = likelihoods[new_position]
        self.set_weight(weight)
        self.set_position(new_position)

        # Resampling: Replacing particles based on their weights (likelihoods)
        weights = np.array([particle.get_weight() for particle in particles])
        self.resample(particles, NUM_PARTICLES, weights)

    def resample(self, particles, NUM_PARTICLES, weights):
        # Normalize the weights
        weights /= np.sum(weights)

        # Systematic resampling
        u0 = np.random.uniform(0, 1 / NUM_PARTICLES)
        indexes = np.arange(NUM_PARTICLES)
        u = (u0 + indexes) / NUM_PARTICLES
        cum_weights = np.cumsum(weights)
        j = 0
        for i in range(NUM_PARTICLES):
            while u[i] >= cum_weights[j]:
                j += 1
            self.position = particles[j].get_position()

        self.set_weight(1.0)  # Reset the weight after resampling

    def predict_next_position(self, transition_matrix):
        # Use the transition probabilities to predict the next position of the particle
        probabilities = np.array(transition_matrix[self.position][1:41]) * 200
        return np.random.choice(range(1, 41), p=probabilities/np.sum(probabilities))
