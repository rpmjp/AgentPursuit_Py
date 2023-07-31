import random
from Agent0 import Agent0
from Agent1 import Agent1
from Agent2 import Agent2
from Agent3 import Agent3
from Agent4 import Agent4
from Agent5 import Agent5
from Agent6 import Agent6
from Agent7 import Agent7
from Environment import Environment
from Target import Target


class Main:
    def __init__(self):
        self.num_trials = 100  # Number of trials to run for each agent
        self.seed = 42  # Use any seed value you prefer (e.g., 42)
        self.env = Environment()  # Initialize the environment

        # Initialize the agents
        self.agents = [
            Agent0(random.randint(1, 40)),
            Agent1(random.randint(1, 40)),
            Agent2(random.randint(1, 40)),
            Agent3(random.randint(1, 40)),
            Agent4(random.randint(1, 40)),
            Agent5(random.randint(1, 40)),
            Agent6(random.randint(1, 40)),
            Agent7(random.randint(1, 40))
        ]

    def run_simulation(self):
        # Run trials for each agent individually
        for agent in self.agents:
            total_steps = 0

            for trial in range(self.num_trials):
                # Reset the agent for a new trial
                agent = agent.reset(random.randint(1, 40))

                # Run the simulation until the target is captured
                game_over = False
                target = Target(self.env, random.randint(1, 40))
                while not game_over:
                    # Move the target
                    target.move(self.env)

                    # Move the agent and check if it captures the target
                    if not agent.capture(target):
                        agent.move(self.env, target)

                    # Check if the agent captured the target
                    if agent.capture(target):
                        game_over = True

                # Record the number of steps taken for the agent in this trial
                total_steps += agent.get_steps_taken()

            # Calculate the average number of steps taken for the agent across all trials
            avg_steps = total_steps / self.num_trials

            # Print the results
            print(agent.__class__.__name__, "Average Steps:", avg_steps)


if __name__ == "__main__":
    main = Main()
    main.run_simulation()
