import os
import openai

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .prompt import Prompt

class GPT:
    def __init__(self) -> None:
        openai.api_key = os.environ["OPENAI_KEY"]

    def query(self, prompt: "Prompt"):
        completion = openai.Completion.create(
            max_tokens=1000,
            deployment_id=os.environ.get("OPENAI_API_DEPLOYMENT"),
            prompt=prompt.build(),
        )

        return completion.choices[0].text
