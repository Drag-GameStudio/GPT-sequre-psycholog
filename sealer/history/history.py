from sealer.cipher.cipher_key import Sealer
from sealpy.cipher import Enigma
import json

class History:
    DEFAULT_STRUCTURE = {
        "role": None,
        "content": None,
    }
    def __init__(self, password):
        self.private_key = Sealer(password).get_private_key()
        self.enigma = Enigma(self.private_key)
        self.history = []

    def load_history(self):
        with open("history.json", "r") as file:
            data = json.load(file)["history"]

        self.load_history_from_data(data)

    def load_history_from_data(self, history_data):
        history = []
        for el in history_data:
            new_data = self.DEFAULT_STRUCTURE.copy()
            new_data["role"] = el["role"]
            new_data["content"] = self.enigma.anti_cipher_text(el["content"])
            history.append(new_data)

        self.history = history

    def cipher_history(self):
        history = []
        for role in self.history:
            new_data = self.DEFAULT_STRUCTURE.copy()
            new_data["role"] = role["role"]
            new_data["content"] = self.enigma.cipher_text(role["content"])
            history.append(new_data)

        return history

    def save_history(self):
        history = self.cipher_history()
        with open("history.json", "r") as file:
            data = json.load(file)["history"]

        for el in history:
            data.append(el)

        with open("history.json", "w") as file:
            json.dump({"history": data}, file, indent=4)

    def add_history(self, role, content):
        new_data = self.DEFAULT_STRUCTURE.copy()
        new_data["role"] = role
        new_data["content"] = content
        self.history.append(new_data)

    

    def get_history(self):
        return self.history
    



        
        
    