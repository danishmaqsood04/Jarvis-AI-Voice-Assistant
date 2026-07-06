import requests
from voice.speak import speak

API_KEY = "893b336352f60199ea0f3f7368d5f817"


def weather(city):
    if not API_KEY:
        speak("Weather API key is missing.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        city = city.title()

        speak(f"The temperature in {city} is {temp} degrees Celsius.")
        speak(f"The weather is {desc}.")
        speak(f"Humidity is {humidity} percent.")

    except requests.exceptions.HTTPError:
        speak("Sorry Boss, I could not find that city.")

    except requests.exceptions.RequestException:
        speak("Sorry Boss, I couldn't connect to the weather service.")

    except Exception:
        speak("Sorry Boss, something went wrong while getting the weather.")


if __name__ == "__main__":
    weather("Srinagar")