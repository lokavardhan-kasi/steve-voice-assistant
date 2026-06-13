import pyttsx3
from config import TTS_RATE, TTS_VOLUME
class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', TTS_RATE)
        self.engine.setProperty('volume', TTS_VOLUME)
        self._set_voice()
    def _set_voice(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            # Microsoft have inbuilt voices with names like 'David' and 'Zira'
            if 'male' in voice.name.lower() or 'David' in voice.name:
                self.engine.setProperty('voice', voice.id)
                break
    def speak(self, text):
        print(f'[Steve] {text}')
        self.engine.say(text)
        self.engine.runAndWait()