from back_side.gpt.gpt import GPT
from back_side.sealer.history.sessions import Session



class CustomSession(Session):
    def request_to_gpt(self):
        gpt = GPT()
        response = gpt.get_answer(self.history.get_history())
        return response


