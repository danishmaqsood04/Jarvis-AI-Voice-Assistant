import subprocess
import os
from voice.speak import speak

def open_app(app_name):

    if app_name == "notepad":
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")

    elif app_name == "calculator":
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")

    elif app_name == "chrome":
        speak("Opening Chrome")
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen(chrome_path)

    elif app_name == "explorer":
        speak("Opening File Explorer")
        subprocess.Popen("explorer.exe")

    elif app_name == "vscode":
        speak("Opening Visual Studio Code")
        vscode_path = r"C:\Users\danis\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        subprocess.Popen(vscode_path)

    else:
        speak("Application not found.")
        
        print("apps.py loaded successfully")