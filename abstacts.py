from abc import ABC, abstractmethod
from utils import CustomVoiceRecognizer
from front_side.audio.tts import text_to_speech
from back_side.manage import CustomSession

class OutputType:
    @abstractmethod
    def output(self, response):
        pass

class InputType:
    def __init__(self, output_type: OutputType, session):
        self.output_type = output_type
        self.session: CustomSession = session

    @abstractmethod
    def start(self):
        pass

