import os
import openai


class GPT:
    def __init__(self) -> None:
        openai.api_key = os.environ["OPENAI_KEY"]

    def query(self, context, question):
        prompt = f"""
Please answer the question exclusively using the given context.
Question: {question}
Context: {' '.join(context)}

Please answer using the below format:
Response:
"""
        
        completion = openai.Completion.create(
            max_tokens=1000,
            deployment_id=os.environ.get("OPENAI_API_DEPLOYMENT"),
            prompt=prompt,
        )

        return completion.choices[0].text
