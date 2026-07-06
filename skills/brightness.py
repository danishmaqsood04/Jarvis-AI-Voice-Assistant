import screen_brightness_control as sbc
from voice.speak import speak


def brightness_up():
    try:
        current = sbc.get_brightness()[0]
        new = min(current + 10, 100)
        sbc.set_brightness(new)
        speak(f"Brightness increased to {new} percent.")
    except Exception:
        speak("Sorry Boss, I couldn't change the brightness.")


def brightness_down():
    try:
        current = sbc.get_brightness()[0]
        new = max(current - 10, 10)
        sbc.set_brightness(new)
        speak(f"Brightness decreased to {new} percent.")
    except Exception:
        speak("Sorry Boss, I couldn't change the brightness.")