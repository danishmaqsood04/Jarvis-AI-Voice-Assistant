import requests
from voice.speak import speak

API_KEY = "13d1ca0796014c72b040b87a6cf96198"


def news():

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "apiKey": API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("status") == "ok":

            articles = data.get("articles", [])[:5]

            if not articles:
                speak("Sorry Boss, I couldn't find any news.")
                return

            speak("Here are today's top headlines.")

            for i, article in enumerate(articles, start=1):
                title = article.get("title", "No title available")
                speak(f"Headline {i}. {title}")

        else:
            speak("Sorry Boss, I couldn't get the latest news.")

    except requests.exceptions.RequestException:
        speak("Sorry Boss, I couldn't connect to the news service.")

    except Exception:
        speak("Sorry Boss, something went wrong while getting the news.")