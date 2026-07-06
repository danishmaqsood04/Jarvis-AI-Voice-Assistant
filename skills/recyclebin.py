import winshell

from voice.speak import speak


def empty_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin has been emptied.")
    except Exception:
        speak("Sorry Boss, I couldn't empty the Recycle Bin.")