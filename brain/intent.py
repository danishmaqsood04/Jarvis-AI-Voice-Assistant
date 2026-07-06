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
    
    elif "increase brightness" in command or "brightness up" in command:
     return "brightness_up"

    elif "decrease brightness" in command or "brightness down" in command:
        return "brightness_down"
    
    elif "open downloads" in command or "downloads" in command:
     return "open_downloads"

    elif (
    "open document" in command
    or "open documents" in command
    or "document" in command
    or "documents" in command
):
     return "open_documents"

    elif "open desktop" in command or "desktop" in command:
     return "open_desktop"
    
    elif "recycle bin" in command:
     return "empty_recycle_bin"

    elif "weather" in command:
     return "weather"

    elif "battery" in command or "charge" in command:
     return "battery"

    elif "time" in command:
     return "time"