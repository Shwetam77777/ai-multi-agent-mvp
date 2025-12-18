from agents.task_agent import TaskAgent
from agents.research_agent import ResearchAgent
from agents.email_agent import EmailAgent
from agents.energy_agent import EnergyAgent

class ParentAgent:
    def __init__(self):
        self.task_agent = TaskAgent()
        self.research_agent = ResearchAgent()
        self.email_agent = EmailAgent()
        self.energy_agent = EnergyAgent()

    def handle(self, user_input, energy_level):
        decision = self.energy_agent.decide(energy_level, user_input)

        if decision == "task":
            return self.task_agent.run(user_input)

        elif decision == "research":
            return self.research_agent.run(user_input)

        elif decision == "email":
            return self.email_agent.run(user_input)

        return "No suitable agent found."
