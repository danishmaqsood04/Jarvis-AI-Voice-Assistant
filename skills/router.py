from skills.apps import open_app
from skills.screenshot import take_screenshot


def run_command(intent):

    commands = {
        "calculator": lambda: open_app("calculator"),
        "chrome": lambda: open_app("chrome"),
        "vscode": lambda: open_app("vscode"),
        "notepad": lambda: open_app("notepad"),
        "screenshot": take_screenshot,
    }

    if intent in commands:
        commands[intent]()
        return True

    return False