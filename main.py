from speech_engine import SpeechEngine
from tts_engine import TTSEngine
from wake_word import WakeWordListener
from command_handler import CommandHandler
from config import GREET_MSG, WAKE_MSG

class Steve:
    def __init__(self):
        print('[Steve] Initializing...')
        self.tts = TTSEngine()
        self.stt = SpeechEngine()
        self.handler = CommandHandler(self.tts)
        self.wake = WakeWordListener(callback=self.on_wake)

    def on_wake(self):
        self.tts.speak(WAKE_MSG)
        self.active = True
        while self.active:
          command = self.stt.listen()
          if not command:
              continue
          if 'sleep' in command or 'go to sleep' in command:
              self.tts.speak('Okay, going to sleep. Say my name to wake me.')
              self.active = False
          else:
              self.handler.handle(command)

    def run(self):
        self.tts.speak(GREET_MSG)
        self.wake.start()
        print('[Steve] Ready! Waiting for wake word...')
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.wake.stop()
            self.tts.speak('Shutting down. Goodbye!')
            print('[Steve] Stopped.')

if __name__ == '__main__':
    steve = Steve()
    steve.run()