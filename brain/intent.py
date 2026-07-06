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

    elif "time" in command:
        return "time"

    elif "screenshot" in command or "take screenshot" in command:
     return "screenshot"

    elif "exit" in command:
        return "exit"

    return "unknown"
