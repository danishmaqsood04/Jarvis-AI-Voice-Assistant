import subprocess
from voice.speak import speak


def empty_recycle_bin():
    try:
        speak("Emptying the Recycle Bin.")

        subprocess.run(
            [
                "powershell",
                "-Command",
                "Clear-RecycleBin -Force"
            ],
            check=True,
        )

        speak("Recycle Bin has been emptied successfully.")

    except Exception as e:
        print(e)
        speak("Sorry Boss, I couldn't empty the Recycle Bin.")