from g4f.client import Client
from g4f.Provider import ChatGLM, DDG, GizAI, Liaobots, PollinationsAI, Qwen_QVQ_72B, Yqcloud #PollinationsAI
import g4f
import time


class GPT:
    def __init__(self, provider=PollinationsAI, gpt_model: str = "gpt-4o"):
        self.client = Client(
            provider=provider,
        )
        self.gpt_model = gpt_model

    def get_answer(self, message):
        try:
            response = self.client.chat.completions.create(
                model=self.gpt_model,
                messages=message
            )
        except Exception as e:
            print(e)
            time.sleep(5)
            return self.get_answer(message)
    
        answer = response.choices[0].message.content
        return answer

