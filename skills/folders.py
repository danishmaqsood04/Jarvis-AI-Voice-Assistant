import os
import subprocess

from voice.speak import speak


def open_downloads():
    speak("Opening Downloads.")

    path = os.path.join(os.path.expanduser("~"), "Downloads")
    subprocess.Popen(f'explorer "{path}"')


def open_documents():
    speak("Opening Documents.")

    path = os.path.join(os.path.expanduser("~"), "Documents")
    subprocess.Popen(f'explorer "{path}"')


def open_desktop():
    speak("Opening Desktop.")

    path = os.path.join(os.path.expanduser("~"), "Desktop")
    subprocess.Popen(f'explorer "{path}"')