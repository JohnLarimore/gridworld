#def train(env, agent, episodes = 1000):
def train(env, agent, episodes = 2):
    #breakpoint()
    for episode in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state