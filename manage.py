from gpt.gpt import GPT
from sealer.history.sessions import Session



class CustomSession(Session):
    def request_to_gpt(self):
        # Here you can implement the logic to send the message to GPT and get the response
        # For example, using the GPT class defined above
        gpt = GPT()
        response = gpt.get_answer(self.history.get_history())
        return response


password = "admin"
session = CustomSession(1, password)
while True:
    message = input("Enter your message: ")
    if message.lower() == "exit":
        session.close_session()
        break
    response = session.send_message(message)
    print("GPT response:", response)