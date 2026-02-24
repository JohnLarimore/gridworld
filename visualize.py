import time
import numpy as np
from IPython.display import clear_output

def render(env):
    grid = np.full((env.size, env.size), ".")
    gx, gy = env.goal
    grid[gx, gy] = "G"
    for lx, ly in env.lava:
        grid[lx, ly] = "L"
    ax, ay = env.agent_pos
    grid[ax, ay] = "A"
    print("\n".join(" ".join(row) for row in grid))

def watch_episode(env, agent, delay = 0.3):
    state = env.reset()
    done = False
    clear_output(wait = True)
    render(env)
    time.sleep(delay)
    while not done:
        x, y = state
        #action = np.argmax(agent.q_table[x, y])
        q_vals = agent.q_table[x, y]
        max_q = np.max(q_vals)
        best_actions = np.where(q_vals == max_q)[0]
        action = np.random.choice(best_actions)
        next_state, reward, done = env.step(action)
        state = next_state
        clear_output(wait = True)
        render(env)
        time.sleep(delay)
    print("\nEpisode finished.")