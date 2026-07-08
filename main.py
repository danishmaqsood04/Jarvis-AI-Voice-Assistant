from voice.speak import speak
from voice.listen import listen
from skills.basic import execute

def main():
    speak("Hello Boss. I am Jarvis.")

    while True:
        command = listen()

        if not command:
            continue

        if "exit " in command or "goodbye" in command or "stop" in command:
            speak("Goodbye Boss. Have a nice day.")
            break

        execute(command)

if __name__ == "__main__":
    main()