from sealpy.cipher import Enigma
import hashlib


class Sealer:
    def __init__(self, password):
        self.password = password

    def get_server_type(self): #224
        hash_password = hashlib.sha224(self.password.encode()).hexdigest()
        return hash_password

    def get_private_key(self): #256
        hash_password = hashlib.sha256(self.password.encode()).hexdigest()
        private_key = Enigma.generate_key_from_hash(hash_password)

        return private_key


# sel = Sealer("password")
# print(sel.get_server_type())
# private_key = sel.get_private_key()
# print(Enigma().cipher_text(private_key, "Hello World"))