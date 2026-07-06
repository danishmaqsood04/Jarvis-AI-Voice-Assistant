import webbrowser
from voice.speak import speak

def youtube_search(command):

    search = command.replace("search youtube for", "")
    search = search.replace("youtube", "").strip()

    if search:
        speak(f"Searching YouTube for {search}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
    else:
        speak("What should I search on YouTube?")
        from skills.weather import weather
from skills.news import get_news
from skills.google_search import search_google

