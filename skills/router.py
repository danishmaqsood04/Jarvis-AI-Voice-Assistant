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
from skills.folders import (
    open_downloads,
    open_documents,
    open_desktop,
)
from skills.recyclebin import empty_recycle_bin
from skills.camera import open_camera


def run_command(intent):

    commands = {
        "calculator": lambda: open_app("calculator"),
        "chrome": lambda: open_app("chrome"),
        "vscode": lambda: open_app("vscode"),
        "notepad": lambda: open_app("notepad"),

        "screenshot": take_screenshot,
        "battery": battery_status,

        "volume_up": volume_up,
        "volume_down": volume_down,
        "mute": mute_volume,
        "unmute": unmute_volume,

        "brightness_up": brightness_up,
        "brightness_down": brightness_down,

        "open_downloads": open_downloads,
        "open_documents": open_documents,
        "open_desktop": open_desktop,

        "empty_recycle_bin": empty_recycle_bin,

        "camera": open_camera,
    }

    if intent in commands:
        commands[intent]()
        return True

    return False