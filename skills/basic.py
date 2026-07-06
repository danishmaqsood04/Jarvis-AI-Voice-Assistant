from skills.youtube_search import youtube_search
import webbrowser
import datetime

from voice.speak import speak
from skills.screenshot import take_screenshot
from skills.google_search import google_search
from skills.apps import open_app
from brain.intent import get_intent


def execute(command):

    intent = get_intent(command)

    if intent == "google_search":
        google_search(command)

    elif intent == "youtube":
        youtube_search(command)

    elif intent == "google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif intent == "screenshot":
        speak("Taking screenshot")
        take_screenshot()

    elif intent == "time":
        current = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current}")

    elif intent == "calculator":
        open_app("calculator")

    elif intent == "chrome":
        open_app("chrome")

    elif intent == "vscode":
        open_app("vscode")

    elif intent == "notepad":
        open_app("notepad")

    else:
        speak("Sorry Boss, I don't know that command.")