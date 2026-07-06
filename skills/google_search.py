import webbrowser
from voice.speak import speak

def google_search(command):

    search = command.replace("search google for", "")
    search = search.replace("google", "").strip()

    if search:
        speak(f"Searching Google for {search}")
        webbrowser.open(f"https://www.google.com/search?q={search}")
    else:
        speak("What do you want me to search?")