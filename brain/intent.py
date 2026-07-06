def get_intent(command):

    command = command.lower()

    if "search google" in command:
        return "google_search"

    if "youtube" in command or "play" in command:
     return "youtube"

    elif "google" in command:
        return "google"
    
    elif "calculator" in command:
     return "calculator"
    
    elif "chrome" in command:
     return "chrome"
    
    elif "vs code" in command or "visual studio code" in command:
     return "vscode"
    
    elif "notepad" in command:
        return "notepad"

    elif "volume up" in command or "increase volume" in command:
     return "volume_up"

    elif "volume down" in command or "decrease volume" in command:
     return "volume_down"

    elif "unmute" in command:
     return "unmute"

    elif "mute" in command and "unmute" not in command:
     return "mute"