import datetime
import webbrowser
import os
import wikipedia
import random
import sys

class Skills:
    def __init__(self, tts):
        self.tts = tts

    def tell_time(self):
        now = datetime.datetime.now().strftime('%I:%M %p')
        self.tts.speak(f'The current time is {now}')

    def tell_date(self):
        today = datetime.datetime.now().strftime('%B %d, %Y')
        self.tts.speak(f'Today is {today}')

    def web_search(self, query: str):
        if not query:
            self.tts.speak('What should I search for?')
            return
        url = f'https://google.com/search?q={query.replace(" ", "+")}'
        webbrowser.open(url)
        self.tts.speak(f'Searching for {query}')

    def wiki_search(self, query: str):
        try:
            result = wikipedia.summary(query, sentences=2)
            self.tts.speak(result)
        except Exception:
            self.tts.speak('I could not find that on Wikipedia.')

    def greet(self):
        hour = datetime.datetime.now().hour
        if hour < 12:
            greeting = 'Good morning!'
        elif hour < 17:
            greeting = 'Good afternoon!'
        else:
            greeting = 'Good evening!'
        self.tts.speak(greeting + ' How can I assist you?')

    def open_application(self, app: str):
        apps = {
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'paint': 'mspaint.exe',
        }
        exe = apps.get(app.lower())
        if exe:
            os.system(exe)
            self.tts.speak(f'Opening {app}')
        else:
            self.tts.speak(f'I do not know how to open {app}')

    def tell_joke(self):
        jokes = [
            'Why do programmers prefer dark mode? Lights attract bugs!',
            'Why did the dev go broke? He used up all his cache.',
            'I told my PC I needed a break. Now it sends Kit Kat ads.',
        ]
        self.tts.speak(random.choice(jokes))

    def goodbye(self):
        self.tts.speak('Goodbye! Have a great day!')
        sys.exit(0)