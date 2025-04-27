import back_side.manage as back_manage
from front_side.audio.tts import text_to_speech
from front_side.microphone.speech_recog import VoiceRecognizer
from back_side.manage import CustomSession

class CustomVoiceRecognizer(VoiceRecognizer):
    def __init__(self, session: back_manage.CustomSession, custom_callback_method, model_path="vosk-model-small-ru-0.22", samplerate=16000, device_index=None):
        self.session = session
        self.custom_callback_method = custom_callback_method
        super().__init__(model_path, samplerate, device_index)

    def callback(self, text):
        print("Recognized:", text)
        response = self.session.send_message(text)
        print("GPT response:", response)
        self.custom_callback_method(response)


from abstacts import OutputType, InputType

class MicrophoneInput(InputType):
    def __init__(self, output_type: OutputType, session: back_manage.CustomSession):
        super().__init__(output_type, session)

    def start(self):
        cvr = CustomVoiceRecognizer(self.session, self.output_type.output)
        cvr.start_recognition()
        return super().start()

class TextInput(InputType):
    def __init__(self, output_type: OutputType, session: back_manage.CustomSession):
        super().__init__(output_type, session)

    def start(self):
        while True:
            text = input("Enter text: ")
            if text.lower() == "exit":
                break
            response = self.session.send_message(text)
            self.output_type.output(response)


class VoiceOutput(OutputType):
    def output(self, response):
        text_to_speech(response)

class TextOutput(OutputType):
    def output(self, response):
        print("GPT response:", response)