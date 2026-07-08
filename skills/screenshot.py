import os
import datetime
import mss

from voice.speak import speak


def take_screenshot():

    speak("Taking screenshot.")

    folder = "screenshots"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    filepath = os.path.join(folder, filename)

    with mss.mss() as sct:
        sct.shot(output=filepath)

    speak("Screenshot has been saved.")