from .history import History
from abc import ABC, abstractmethod


class Session:
    DEFAULT_PROMPT = """Ты должен быть психологом который помагает клиенту в его проблемах."""

    def __init__(self, login, password):
        self.history = History(login, password)
        self.session_number = self.history.load_history()
        self.history.add_history("system", f"{self.DEFAULT_PROMPT}")
        self.history.add_history("system", f"{self.session_number} started")

    @abstractmethod
    def request_to_gpt(self):
        pass


    def send_message(self, message):
        self.history.add_history("user", message)
        self.history.get_history()

        answer = self.request_to_gpt()
        self.history.add_history("assistant", answer)
        
        return answer
    
    def close_session(self):
        self.history.add_history("system", f"{self.session_number} closed")
        self.history.save_history()
        