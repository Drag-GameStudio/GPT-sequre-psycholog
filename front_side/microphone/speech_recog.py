import pyaudio
import vosk
import json
import time
from abc import ABC, abstractmethod

class VoiceRecognizer:
    def __init__(self, model_path, samplerate=16000, device_index=None):
        self.model_path = model_path
        self.samplerate = samplerate
        self.device_index = device_index
        self.model = vosk.Model(model_path)
        self.rec = vosk.KaldiRecognizer(self.model, samplerate)

    @abstractmethod
    def callback(self, text):
        pass

    def start_recognition(self):
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=self.samplerate,
                        input=True,
                        frames_per_buffer=8000,
                        input_device_index=self.device_index)

        self.stream.start_stream()

        print("Говорите...")
        buffer = []
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.rec.AcceptWaveform(data):
                result = json.loads(self.rec.Result())
                buffer.append(result.get('text', ''))
                print(buffer)
                if len(buffer) >= 2:
                    if buffer[-1]  == "":
                        prompt = ""
                        [prompt := prompt + " " + el for i, el in enumerate(buffer) if i < len(buffer)-2]
                        buffer = []
                        self.callback(prompt)
                


    


