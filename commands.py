import os
import subprocess
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "sure", "do it", "yeah", "confirm", "si", "consider it done", "ok soldier"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("you haven't told me your name yet!")
            else:
                self.respond("my name is shanta. How are you deer?")

        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

        # if "launch" or "open" in text:
        #     app = text.split(" ", 1)[-1]
        #     self.respond("Opening "+ app)
        #     os.system("open -a "+ app + ".app")

    def respond(self, response):
        response = "Ratul Hasan"
        print(response)
        subprocess.call("say " + response, shell=True)