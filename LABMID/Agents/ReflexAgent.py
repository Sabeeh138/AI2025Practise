class Environment:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state
    
    def update_state(self, action):
        if action == "clean":
            self.state = "clean"

class ReflexAgent:
    def __init__(self):
        self.rules = {"dirty": "clean", "clean": "do_nothing"}
    
    def act(self, environment):
        state = environment.get_state()
        return self.rules.get(state, "do_nothing")
    
env = Environment("dirty")
agent = ReflexAgent()

action = agent.act(env)
print(f"Reflex Agent action: {action}")
env.update_state(action)