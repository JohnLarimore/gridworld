This repository contains Laramie County Community College's (LCCC) implementation of the Grid World environment, designed for experimenting with Reinforcement Learning algorithms.

🛠 Project Structure
environment.py: The Markov Decision Process (MDP) logic (states, actions, rewards).

agent.py: The RL agent (e.g., Q-Learning, SARSA, or Deep Q-Network).

train.py: Script to run training loops and save models.

visualize.py: Tools for rendering the grid and plotting learning curves.

main_game.ipynb: An interactive notebook to demonstrate the agent's performance.

🚀 Getting Started
Prerequisites
Ensure you have Python 3.x installed. You will likely need numpy and matplotlib.

Installation
Clone the repository:

Bash
git clone https://github.com/JohnLarimore/gridworld.git
cd gridworld
(Optional) Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
🎮 How to Run
To see a pre-trained agent or run a basic simulation:

Bash
python main.py
To train a new agent from scratch:

Bash
python train.py
🤝 Contributing
This is a collaborative project for the LCCC AI Club.

Fork the repo.

Create a feature branch (git checkout -b feature/AmazingFeature).

Commit your changes.

Open a Pull Request!

License: GPL-3.0
