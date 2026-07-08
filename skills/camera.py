import cv2
from voice.speak import speak

import os
from datetime import datetime


def open_camera():

    speak("Opening camera.")

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        speak("Sorry Boss, I couldn't open the camera.")
        return

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        cv2.imshow("Jarvis Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    speak("Camera closed.")


import os
from datetime import datetime


def take_photo():

    speak("Taking photo.")

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        speak("Sorry Boss, I couldn't open the camera.")
        return

    ret, frame = camera.read()

    if ret:

        os.makedirs("data/photos", exist_ok=True)

        filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")

        filepath = os.path.join("data/photos", filename)

        cv2.imwrite(filepath, frame)

        speak("Photo saved successfully.")

    else:
        speak("Sorry Boss, I couldn't capture the photo.")

    camera.release()