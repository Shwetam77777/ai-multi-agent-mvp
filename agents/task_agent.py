from llm_client import client

class TaskAgent:
    def run(self, user_input):
        prompt = f"""
        You are a task planning AI.
        Break the following goal into small, clear, actionable steps.
        Keep it simple and structured.

        Goal: {user_input}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
