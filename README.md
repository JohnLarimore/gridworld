This repository contains Laramie County Community College's (LCCC) implementation of the Grid World environment, designed for experimenting with Reinforcement Learning algorithms.

# Project Structure:

* **`environment.py`**: The grid logic. Sets the goal at `(4,4)` and hazardous lava at `(1,3)`.
* **`agent.py`**: The Q-Learning agent. Implements the Q-table update logic and $\epsilon$-greedy action selection.
* **`train.py`**: Logic for running training episodes to let the agent learn from rewards.
* **`visualize.py`**: Renders the $5 \times 5$ grid in the console/notebook and animates the agent's path.
* **`main_game.ipynb`**: The main notebook to run training and watch the agent play.

# Getting Started
Prerequisites:
Ensure you have Python 3.x installed. You will need numpy and matplotlib.

# Installation
Clone the repository:
* git clone https://github.com/JohnLarimore/gridworld.git
* cd gridworld
* (Optional) Create a virtual environment:
* python -m venv venv
* source venv/bin/activate  # On Windows: venv\Scripts\activate

# How to Run
Clone the folder into a Jupyter environment, and run the one cell in 'main_game.ipynb'. 

# Contributing
This is a collaborative project for the LCCC AI Club.
License: GPL-3.0
