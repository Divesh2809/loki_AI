import pygame
from gtts import gTTS
import os
import time
import threading
import re  

class SpeechSynthesizer:
    def __init__(self):
        pygame.mixer.init()

    def sanitize_text(self, text):
        
        return re.sub(r"[^a-zA-Z0-9.,!? ]+", "", text)

    def speak(self, text):
        def play_audio():
            
            sanitized_text = self.sanitize_text(text)

            
            audio_file = f"temp_audio_{int(time.time() * 1000)}.mp3"
            
            
            tts = gTTS(text=sanitized_text, lang='en')
            tts.save(audio_file)

           
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            
            pygame.mixer.music.unload()

            
            os.remove(audio_file)

        
        threading.Thread(target=play_audio, daemon=True).start()