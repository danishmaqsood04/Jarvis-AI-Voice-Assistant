from skills.youtube_search import youtube_search
import webbrowser
import datetime

from voice.speak import speak
from skills.screenshot import take_screenshot
from skills.google_search import google_search
from skills.apps import open_app
from skills.router import run_command
from skills.weather import weather
from brain.intent import get_intent


def execute(command):

    intent = get_intent(command)
    print("Intent:", intent)

    if intent == "google_search":
        google_search(command)
        return

    if run_command(intent):
        return

    elif intent == "youtube":
        youtube_search(command)

    elif intent == "weather":
        city = "Srinagar" 

        if "in" in command.lower():
            city = command.lower().split("in", 1)[1].strip()
        if city.lower() == "kashmir":
         city = "Srinagar"

        weather(city)


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