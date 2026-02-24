This repository contains Laramie County Community College's (LCCC) implementation of the Grid World environment, designed for experimenting with Reinforcement Learning algorithms.

#Project Structure:
*environment.py: The Markov Decision Process (MDP) logic (states, actions, rewards).
*agent.py: The RL agent (eventually to include, Q-Learning, SARSA, or Deep Q-Network).
*train.py: Script to run training loops and save models.
*visualize.py: Tools for rendering the grid and plotting learning curves.
*main_game.ipynb: An interactive notebook to demonstrate the agent's performance.

#Getting Started
Prerequisites:
Ensure you have Python 3.x installed. You will need numpy and matplotlib.

#Installation
Clone the repository:
*git clone https://github.com/JohnLarimore/gridworld.git
*cd gridworld
*(Optional) Create a virtual environment:
*python -m venv venv
*source venv/bin/activate  # On Windows: venv\Scripts\activate

#How to Run
Clone the folder into a Jupyter environment, and run the one cell in 'main_game.ipynb'. 

Contributing
This is a collaborative project for the LCCC AI Club.
License: GPL-3.0
