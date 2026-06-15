import pyttsx3
from config import TTS_RATE, TTS_VOLUME

class TTSEngine:
    def __init__(self):
        self._rate = TTS_RATE
        self._volume = TTS_VOLUME

    def speak(self, text: str):
        print(f'[Steve] {text}')
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', self._rate)
            engine.setProperty('volume', self._volume)
            voices = engine.getProperty('voices')
            for voice in voices:
                if 'david' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f'[Steve] TTS Error: {e}')