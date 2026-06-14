from skills import Skills

class CommandHandler:
    def __init__(self, tts):
        self.tts = tts
        self.skills = Skills(tts)

    def handle(self, command: str):
        if not command:
            self.tts.speak('I did not catch that. Please try again.')
            return

        if 'time' in command:
            self.skills.tell_time()
        elif 'date' in command:
            self.skills.tell_date()
        elif 'open' in command:
            app = command.replace('open', '').strip()
            self.skills.open_application(app)
        elif 'search' in command or 'google' in command:
            query = command.replace('search', '').replace('google', '').strip()
            self.skills.web_search(query)
        elif 'wikipedia' in command or 'who is' in command:
            query = command.replace('wikipedia', '').replace('who is', '').strip()
            self.skills.wiki_search(query)
        elif any(w in command for w in ['hello', 'hi', 'hey']):
            self.skills.greet()
        elif 'joke' in command:
            self.skills.tell_joke()
        elif any(w in command for w in ['exit', 'quit', 'bye', 'goodbye']):
            self.skills.goodbye()
        else:
            self.tts.speak(f'I heard {command} but I do not know how to do that yet.')

