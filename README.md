# Agent Pursuit Simulation 🕵️‍♂️🤖

## 📝 Project Overview

**Agent Pursuit Simulation** is a complex AI-driven simulation where eight different agents attempt to capture a target within a dynamically structured 40-node graph environment. Each agent employs unique search strategies, ranging from deterministic algorithms to advanced probabilistic models, including particle filters and Hidden Markov Models (HMM). The agents’ performances are evaluated based on the number of steps taken to capture the moving target.

## 🚀 Features

- **Graph-Based Environment**: A dynamically generated 40-node graph where agents and targets move. Each node has up to three connections to neighboring nodes.
- **Diverse Agent Strategies**: Eight agents with unique strategies, including deterministic algorithms, probabilistic reasoning, belief states, particle filters, and HMM.
- **Performance Evaluation**: The simulation runs over 100 trials, and each agent’s performance is analyzed based on the average number of steps required to capture the target.
  
## 🧠 Agent Strategies

Each agent in the simulation uses a different algorithm or technique to pursue the target:

### Agent 0: Lazy Agent
- **Strategy**: Remains stationary at the starting node. This agent is used as a control to compare other agents' performances.
- **Expected Outcome**: Does not capture the target.

### Agent 1: Breadth-First Search (BFS)
- **Strategy**: Moves towards the target using BFS. At each step, the agent calculates the shortest path to the target.
- **Expected Outcome**: Effective in relatively small environments due to BFS’s complete exploration.

### Agent 2: Dijkstra’s Algorithm
- **Strategy**: Implements Dijkstra's algorithm to find the shortest path to the target, taking into account the dynamic nature of the environment.
- **Expected Outcome**: Efficient in larger graphs, improving upon BFS by considering the least-cost path.

### Agent 3: Belief State with Node Monitoring
- **Strategy**: Uses belief states to track the target's potential locations and updates the belief based on the examination of each node.
- **Expected Outcome**: Performs well by continuously narrowing down the target's position using probabilistic reasoning.

### Agent 4: Belief State with Random Movement
- **Strategy**: Moves towards nodes with the highest belief probability and randomly selects one if multiple nodes share the same probability.
- **Expected Outcome**: Less effective than deterministic approaches but introduces randomness to avoid local minima.

### Agent 5: BFS with Belief State
- **Strategy**: Combines BFS and belief state updates to calculate the shortest path while simultaneously refining the target's potential location.
- **Expected Outcome**: Combines efficiency with improved targeting through belief updates.

### Agent 6: Belief State with Heuristic Movement
- **Strategy**: Similar to Agent 4 but uses a heuristic to improve movement decisions by analyzing distances to high-belief nodes.
- **Expected Outcome**: More refined and effective version of Agent 4, with enhanced heuristic reasoning.

### Agent 7: Particle Filter and Hidden Markov Model (HMM)
- **Strategy**: Utilizes particle filtering and HMM to predict the target’s movements. Updates particles based on likelihoods and resamples them for improved accuracy.
- **Expected Outcome**: The most advanced agent in terms of probabilistic tracking, excels in capturing highly dynamic targets.

## 📊 Performance Evaluation

Each agent’s performance is evaluated by calculating the average number of steps taken to capture the target across 100 trials. The target moves randomly within the environment, and agents pursue it using their respective strategies.

### Key Metrics:
- **Average Steps**: The number of steps required by each agent to capture the target.
- **Successful Captures**: How often each agent successfully captures the target.

| **Agent**  | **Algorithm**                              | **Average Steps** |
|------------|--------------------------------------------|-------------------|
| Agent 0    | Stationary                                 | N/A               |
| Agent 1    | Breadth-First Search                       | ~7.53             |
| Agent 2    | Dijkstra’s Algorithm                       | ~5.36             |
| Agent 3    | Belief State (Node Monitoring)             | ~50.52            |
| Agent 4    | Belief State with Random Movement          | ~47.4             |
| Agent 5    | BFS with Belief State                      | ~4.93             |
| Agent 6    | Belief State with Heuristic Movement       | ~50.52            |
| Agent 7    | Particle Filter & Hidden Markov Model (HMM)| ~47.4             |

## 🛠️ Technologies Used

- **Python**: Core language for the simulation logic.
- **Search Algorithms**: BFS, Dijkstra's algorithm, and heuristic-based movement strategies.
- **Particle Filtering & Hidden Markov Models**: Used by Agent 7 for advanced tracking and prediction.
- **Random Graph Generation**: The environment dynamically generates a random graph for each trial.
  
## 🎮 How to Run the Simulation

1. Clone this repository:
   ```bash
   git clone https://github.com/rpmjp/agent-pursuit.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulation:
   ```bash
   python main.py
   ```
4. View the results after 100 trials for each agent, including the average steps taken for successful captures.

## 📂 Project Structure

```bash
agent-pursuit/
│
├── Agent0.py              # Stationary agent
├── Agent1.py              # BFS agent
├── Agent2.py              # Dijkstra's agent
├── Agent3.py              # Belief state agent with node monitoring
├── Agent4.py              # Belief state with random movement
├── Agent5.py              # BFS with belief state
├── Agent6.py              # Belief state with heuristic
├── Agent7.py              # Particle filter & HMM agent
├── Environment.py         # Graph-based environment
├── Particle.py            # Particle class for Agent 7
├── Target.py              # Target movement logic
├── main.py                # Main simulation loop
└── README.md              # Project documentation
```

## 🧑‍💻 Screenshots & Algorithms

Particle Filtering: In Agent7, I use a particle filtering algorithm to predict the target's next move. 
The algorithm updates particle positions based on the transition matrix and likelihoods, followed by resampling based on their weights. This helps Agent7 refine its belief about where the target might be. The screenshot shows the process of updating the belief state and resampling particles to improve accuracy.

- **Particle Filtering Process**:
  ![Screenshot 2024-10-17 052910](https://github.com/user-attachments/assets/fbc1374e-f90a-4b4c-9a43-4e08e08374f9)

  
BFS (Breadth-First Search): For Agent5, I implemented the BFS algorithm to calculate the shortest path to the target. The BFS explores the graph by traversing through neighboring nodes, backtracking when necessary, to ensure the optimal route is followed. This method helps the agent reach the target more efficiently.
- **Breadth-First Search (BFS)**:
  ![Screenshot 2024-10-17 053047](https://github.com/user-attachments/assets/3d734df6-587c-4edb-9bee-eea30f252b61)

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests for improvements, optimizations, or bug fixes.

## 📝 License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

For more information, please refer to <https://unlicense.org>.
