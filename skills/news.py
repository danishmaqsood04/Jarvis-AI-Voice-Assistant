import requests
from voice.speak import speak

API_KEY = "13d1ca0796014c72b040b87a6cf96198"

def news():

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "ok":

            articles = data["articles"][:5]

            speak("Here are today's top headlines.")

            for i, article in enumerate(articles, start=1):
                title = article["title"]
                speak(f"News {i}. {title}")

        else:
            speak("Sorry Boss, I couldn't get the news.")

    except Exception:
        speak("Sorry Boss, something went wrong.")