import cv2
from voice.speak import speak


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