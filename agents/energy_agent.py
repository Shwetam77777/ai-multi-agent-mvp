class EnergyAgent:
    def decide(self, energy_level, user_input):
        text = user_input.lower()

        if energy_level == "Low":
            return "task"

        if "email" in text:
            return "email"

        if "research" in text or "learn" in text or "study" in text:
            return "research"

        return "task"
