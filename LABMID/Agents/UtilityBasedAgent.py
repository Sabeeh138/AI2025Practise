class EnergyEnvironment:
    def __init__(self, energy_level):
        self.energy_level = energy_level

    def get_energy_level(self):
        return self.energy_level

    def update_energy(self, action):
        if action == "recharge":
            self.energy_level = 100


class UtilityBasedAgent:
    def __init__(self):
        self.threshold = 30

    def act(self, environment):
        energy = environment.get_energy_level()
        return "recharge" if energy < self.threshold else "keep_working"

energy_env = EnergyEnvironment(20)
utility_agent = UtilityBasedAgent()
print(f"UtilityBasedAgent action: {utility_agent.act(energy_env)}")
