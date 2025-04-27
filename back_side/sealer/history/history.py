from back_side.sealer.cipher.cipher_key import Sealer
from sealpy.cipher import Enigma
import json

class History:
    DEFAULT_STRUCTURE = {
        "role": None,
        "content": None,
    }

    DEFAULT_USER_STRUCTURE = {
        "password": None,
        "history": []
    }

    def __init__(self, login, password):
        self.login = login
        sealer = Sealer(password)
        self.private_key = sealer.get_private_key()
        self.server_key = sealer.get_server_type()
        self.enigma = Enigma(self.private_key)
        self.history = []

    def load_history(self):
        with open("history.json", "r") as file:
            data = json.load(file)

        if data.get(self.login) is None:
            data = []
        else:
            data = data.get(self.login)["history"]

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
            all_data = json.load(file)

        if all_data.get(self.login) is None:
            all_data[self.login] = self.DEFAULT_USER_STRUCTURE.copy()
            all_data[self.login]["password"] = self.server_key
            all_data[self.login]["history"] = history
        
        else:
            data: list = all_data.get(self.login)["history"]

            for el in history:
                data.append(el)

            all_data[self.login]["history"] = data

        with open("history.json", "w") as file:
            json.dump(all_data, file, indent=4)

    def add_history(self, role, content):
        new_data = self.DEFAULT_STRUCTURE.copy()
        new_data["role"] = role
        new_data["content"] = content
        self.history.append(new_data)

    

    def get_history(self):
        return self.history
    



        
        
    