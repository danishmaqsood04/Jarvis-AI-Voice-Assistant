import psutil
from voice.speak import speak


def battery_status():
    battery = psutil.sensors_battery()

    if battery is None:
        speak("Sorry Boss, I cannot detect the battery.")
        return

    percent = battery.percent

    if battery.power_plugged:
        speak(f"Your battery is {percent} percent and charging.")
    else:
        speak(f"Your battery is {percent} percent.")