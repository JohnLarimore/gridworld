import numpy as np
class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.goal = (4,4)
        self.lava = [(1,3)]
        self.reset()

    def reset(self):
        self.agent_pos = (0, 0)
        return self.agent_pos

    def step(self, action):
        x, y = self.agent_pos
        if action == 0:
            x = max(x - 1, 0)  
        elif action == 1:
            x = min(x + 1, self.size - 1)
        elif action == 2:
            y = max(y - 1, 0)
        elif action == 3:
            y = min(y + 1, self.size - 1)
        self.agent_pos = (x, y)
        reward = -0.1
        done = False
        if self.agent_pos == self.goal:
            reward = 10
            done = True
        elif self.agent_pos in self.lava:
            reward = -10
            done = True
        return self.agent_pos, reward, done

    