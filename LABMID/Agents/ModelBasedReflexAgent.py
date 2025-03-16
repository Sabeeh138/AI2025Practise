class WeatherEnvironment:
    def __init__(self, condition):
        self.condition = condition

    def get_condition(self):
        return self.condition

    def update_condition(self, action):
        if action == "carry_umbrella":
            self.condition = "prepared"


class ModelBasedReflexAgent:
    def __init__(self):
        self.state = "unknown"

    def act(self, environment):
        self.state = environment.get_condition()
        return "carry_umbrella" if self.state == "rainy" else "do_nothing"

weather_env = WeatherEnvironment("rainy")
model_agent = ModelBasedReflexAgent()
print(f"ModelBasedReflexAgent action: {model_agent.act(weather_env)}")

