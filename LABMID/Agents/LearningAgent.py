class LearningEnvironment:
    def __init__(self, task):
        self.task = task

    def get_task(self):
        return self.task

    def update_task(self, action):
        if action == "practice":
            self.task = "learned"


class LearningAgent:
    def __init__(self):
        self.experiences = {}

    def act(self, environment):
        task = environment.get_task()
        if task not in self.experiences:
            self.experiences[task] = "practice"
        return self.experiences[task]



learning_env = LearningEnvironment("new skill")
learning_agent = LearningAgent()
print(f"LearningAgent action: {learning_agent.act(learning_env)}")
