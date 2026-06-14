import speech_recognition as sr
from config import  LANGUAGE, TIMEOUT, PHRASE_LIMIT 

class SpeechEngine:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
    # making  private by convention - method to reduce noise and calibrate the microphone
    def _calibrate(self):
        with self.mic as source:
            print('[Steve] Calibrating microphone...')
            self.recognizer.adjust_for_ambient_noise(source,duration = 1)
    # listening for user input and converting it to text using Google's STT 
    def listen(self) ->str:
        with self.mic as source:
            print('[Steve] Listening...')
            #recording the source from mic into Audio
            audio = self.recognizer.listen(source, timeout=TIMEOUT, phrase_time_limit=PHRASE_LIMIT)
        try:
            text = self.recognizer.recognize_google(audio, language=LANGUAGE)
            print(f'[Steve] Heard: {text}')
            return text.lower()
        except sr.UnknownValueError:
            print('[Steve] Sorry, I could not understand the audio.')
            return ''
        except sr.RequestError as e:
            print(f'[Steve] STT Error: {e}')
            return ''
        except sr.WaitTimeoutError:
            print('[Steve] Listening timed out.')
            return ''