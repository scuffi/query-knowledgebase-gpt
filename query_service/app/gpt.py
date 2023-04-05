import os
import openai


class GPT:
    def __init__(self) -> None:
        openai.api_type = os.environ["OPENAI_TYPE"]
        openai.api_key = os.environ["OPENAI_KEY"]
        openai.api_base = os.environ["OPENAI_BASE"]
        openai.api_version = os.environ["OPENAI_VERSION"]

    def query(self, context, question):
        prompt = f"""
Please answer the question exclusively using the given context.
Question: {question}
Context: {' '.join(context)}

Please answer using the below format:
Response:
"""
        
        print(prompt)
        
        completion = openai.Completion.create(
            max_tokens=1000,
            deployment_id=os.environ["OPENAI_DEPLOYMENT"],
            prompt=prompt,
        )

        return completion.choices[0].text
