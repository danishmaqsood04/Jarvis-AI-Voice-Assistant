import os
import subprocess

from voice.speak import speak


def open_downloads():
    path = os.path.join(os.path.expanduser("~"), "Downloads")
    subprocess.Popen(f'explorer "{path}"')
    speak("Opening Downloads")


def open_documents():
    path = os.path.join(os.path.expanduser("~"), "Documents")
    subprocess.Popen(f'explorer "{path}"')
    speak("Opening Documents")


def open_desktop():
    path = os.path.join(os.path.expanduser("~"), "Desktop")
    subprocess.Popen(f'explorer "{path}"')
    speak("Opening Desktop")