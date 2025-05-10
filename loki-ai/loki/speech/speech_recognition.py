import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def capture_speech(self):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Sorry, I couldn't understand that."
            except sr.RequestError:
                return "Speech recognition service is unavailable."
            except sr.WaitTimeoutError:
                return "No speech detected."

    def process_speech(self, audio_data):
        
        pass

    def recognize_speech(self):
        
        pass