from llm_client import client

class EmailAgent:
    def run(self, user_input):
        prompt = f"""
        You are a professional email writing assistant.
        Write a polite, clear, and professional email for the following request:
        {user_input}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
