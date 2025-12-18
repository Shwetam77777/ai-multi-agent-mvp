from llm_client import client

class ResearchAgent:
    def run(self, user_input):
        prompt = f"""
        You are a research assistant.
        Give a concise summary with key bullet points about:
        {user_input}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
