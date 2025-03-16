class MazeEnvironment:
    def __init__(self, position, goal):
        self.position = position
        self.goal = goal

    def get_position(self):
        return self.position

    def update_position(self, action):
        if action == "move_forward":
            self.position += 1


class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def act(self, environment):
        position = environment.get_position()
        return "goal_achieved" if position == self.goal else "move_forward"

maze_env = MazeEnvironment(0, 5)
goal_agent = GoalBasedAgent(5)
print(f"GoalBasedAgent action: {goal_agent.act(maze_env)}")

