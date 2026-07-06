import webbrowser
from voice.speak import speak

def youtube_search(command):

    search = command.replace("search youtube for", "")
    search = search.replace("play", "")
    search = search.replace("youtube", "").strip()

    if search:
        speak(f"Searching YouTube for {search}")
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={search}"
        )
    else:
        speak("What do you want me to search on YouTube?")