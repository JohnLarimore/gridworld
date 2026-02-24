This repository contains Laramie County Community College's (LCCC) implementation of the Grid World environment, designed for experimenting with Reinforcement Learning algorithms.

# Project Structure:
* **`environment.py`**: The grid logic. Sets the goal at `(4,4)` and hazardous lava at `(1,3)`.
* **`agent.py`**: The Q-Learning agent. Implements the Q-table update logic and $\epsilon$-greedy action selection.
* **`train.py`**: Logic for running training episodes to let the agent learn from rewards.
* **`visualize.py`**: Renders the $5 \times 5$ grid in the console/notebook and animates the agent's path.
* **`main_game.ipynb`**: The main notebook to run training and watch the agent play.

# Usage:
For now, [Download Project as ZIP](https://github.com/JohnLarimore/gridworld/archive/refs/heads/main.zip) and upload into either JupyterLab or Google Colab. 

We can build out a bit better, then we'll be able to just clone the repository:
* git clone https://github.com/JohnLarimore/gridworld.git
* cd gridworld
* (Optional) Create a virtual environment:
* python -m venv venv
* source venv/bin/activate 
* Off to the racees

# How to Run
From your preferred Notebook environment, open 'main_game.ipynb' and run the lone cell. 

* Details to be more carefully specified in the next club meeting. 

# Contributing
This is a collaborative project for the LCCC AI Club.
License: GPL-3.0
