import numpy as np
import random

class QAgent:
    def __init__(self, state_size, action_size, alpha = 0.1, gamma = 0.0, epsilon = 0.1):
        self.q_table = np.zeros((state_size, state_size, action_size))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.action_size = action_size

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)
        x, y = state
        return np.argmax(self.q_table[x, y])

    def update(self, state, action, reward, next_state):
        x, y = state
        nx, ny = next_state
        best_next = np.max(self.q_table[nx, ny])
        #best_next = np.max(self.q_table[x, y])
        self.q_table[x, y, action] += self.alpha * (
            reward + self.gamma * best_next -self.q_table[x, y, action]
        )