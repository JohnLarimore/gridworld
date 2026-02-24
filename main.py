from environment import GridWorld
from agent import QAgent
from train import train
env = GridWorld()
agent = QAgent(state_size = 5, action_size = 4)
train(env, agent, episodes=2000)
