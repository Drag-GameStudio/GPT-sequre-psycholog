import edge_tts
import asyncio
from playsound import playsound
import pygame
import os
import time

async def text_to_speech_async(text, voice="ru-RU-SvetlanaNeural", output_file="front_side/audio/utils/output.mp3"):
    communicate = edge_tts.Communicate(text, voice=voice, rate="+15%")
    audio_data = b""
    async for message in communicate.stream():
        if message["type"] == "audio":
            audio_data += message["data"]

    with open(output_file, "wb") as f:
        f.write(audio_data)

    pygame.mixer.init()
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.quit()
    os.remove(output_file)

def text_to_speech(text, voice="ru-RU-SvetlanaNeural", output_file="./front_side/audio/utils/output.mp3"):
    asyncio.run(text_to_speech_async(text, voice, output_file))

# print("Text-to-Speech Conversion")
# while True:
#     text = input("Enter the text you want to convert to speech: ")
#     text_to_speech(text)