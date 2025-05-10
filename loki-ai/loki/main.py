# main.py

import tkinter as tk
from tkinter import scrolledtext
import threading
import speech.speech_recognition as sr
import speech.speech_synthesis as ss
import memory.memory_manager as mm
import responses.response_generator as rg

class LokiAI:
    def __init__(self):
        self.recognizer = sr.SpeechRecognizer()
        self.synthesizer = ss.SpeechSynthesizer()  
        self.memory_manager = mm.MemoryManager()
        self.response_generator = rg.ResponseGenerator(self.memory_manager, None)  

    def process_speech(self):
        user_input = self.recognizer.capture_speech()
        if user_input:
            response = self.response_generator.generate_response(user_input)
            self.synthesizer.speak(response)  
            return user_input, response
        return None, None

class LokiGUI:
    def __init__(self, root, loki_ai):
        self.loki_ai = loki_ai
        self.root = root
        self.root.title("Loki AI")
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20, width=50)
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Input field
        self.input_field = tk.Entry(root, width=40)
        self.input_field.grid(row=1, column=0, padx=10, pady=10)
        
        # Buttons
        self.send_button = tk.Button(root, text="Send", command=self.handle_text_input)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.speak_button = tk.Button(root, text="Speak", command=self.handle_speech_input)
        self.speak_button.grid(row=2, column=0, columnspan=2, pady=10)

    def handle_text_input(self):
        user_input = self.input_field.get()
        if user_input:
            self.display_message("You: " + user_input)
            response = self.loki_ai.response_generator.generate_response(user_input)
            self.display_message("Loki: " + response)
            self.loki_ai.synthesizer.speak(response)  
            self.input_field.delete(0, tk.END)

    def handle_speech_input(self):
        def process_speech():
            user_input, response = self.loki_ai.process_speech()
            if user_input and response:
                self.display_message("You (via speech): " + user_input)
                self.display_message("Loki: " + response)

        threading.Thread(target=process_speech).start()

    def display_message(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    loki_ai = LokiAI()
    root = tk.Tk()
    gui = LokiGUI(root, loki_ai)
    root.mainloop()