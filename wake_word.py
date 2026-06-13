import speech_recognition as sr
import threading
from config import WAKE_WORD, LANGUAGE

class WakeWordListener:
    def __init__(self,callback):
        self.callback = callback
        self.running = False
        self.recognizer = sr.Recognizer()
        self._thread = None

    def start(self):
        self.running = True
        self._thread = threading.Thread(target=self._listen_loop, daemon=True)
        self._thread.start()
        print(f'[Steve] Wake word listener started. Say "{WAKE_WORD}"!')
        
    def stop(self):
        self.running = False

    def _listen_loop(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.running:
                try:
                    audio = self.recognizer.listen(source, timeout=3)
                    text = self.recognizer.recognize_google(audio, language=LANGUAGE).lower()
                    if WAKE_WORD in text:
                        self.callback()
                except Exception:
                    pass