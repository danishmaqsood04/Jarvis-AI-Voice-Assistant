from skills.volume import (
    volume_up,
    volume_down,
    mute_volume,
    unmute_volume,
)
from skills.battery import battery_status
from skills.apps import open_app
from skills.screenshot import take_screenshot
from skills.brightness import brightness_up, brightness_down

def run_command(intent):

    commands = {
        "calculator": lambda: open_app("calculator"),
        "chrome": lambda: open_app("chrome"),
        "vscode": lambda: open_app("vscode"),
        "notepad": lambda: open_app("notepad"),

        "screenshot": take_screenshot,
        "battery": battery_status,
        "volume_up": lambda: volume_up(),
        "volume_down": lambda: volume_down(),
        "brightness_up": brightness_up,
        "brightness_down": brightness_down,
        
        "mute": lambda: mute_volume(),
        "unmute": lambda: unmute_volume(),
        "volume_up": volume_up,
        "volume_down": volume_down,
        "mute": mute_volume,
        "unmute": unmute_volume,
    }

    if intent in commands:
        commands[intent]()
        return True

    return False