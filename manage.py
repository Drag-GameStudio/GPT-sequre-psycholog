import back_side.manage as back_manage
from front_side.audio.tts import text_to_speech
from front_side.microphone.speech_recog import VoiceRecognizer
from utils import MicrophoneInput, VoiceOutput, TextInput, TextOutput
from abstacts import OutputType, InputType

# mi = MicrophoneInput(VoiceOutput())
# mi.start()

class Pcyholog:
    def __init__(self, input_type, output_type, login, password):
        self.input_type: InputType = input_type
        self.output_type: OutputType = output_type
        self.password = password

        self.session = back_manage.CustomSession(login, self.password)
        self.controller = self.input_type(self.output_type(), self.session)

    def start_session(self):
        self.controller.start()
        self.close_session()

    def close_session(self):
        print("session was closed")
        self.session.close_session()


p = Pcyholog(MicrophoneInput, VoiceOutput, "loginTest", "password")
p.start_session()