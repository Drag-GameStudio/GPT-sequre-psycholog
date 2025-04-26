import back_side.manage as back_manage
from front_side.audio.tts import text_to_speech

password = "123456"
session = back_manage.CustomSession(1, password)
while True:
    message = input("Enter your message: ")
    if message.lower() == "exit":
        session.close_session()
        break
    response = session.send_message(message)
    text_to_speech(response)
    print("GPT response:", response)