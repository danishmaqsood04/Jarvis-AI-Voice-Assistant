import pyttsx3

def speak(text):
    engine = pyttsx3.init()      # Har baar naya engine banao
    engine.setProperty("rate", 170)

    print("Assistant:", text)

    engine.say(text)
    engine.runAndWait()
    engine.stop()