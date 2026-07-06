from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

from voice.speak import speak


def get_volume_controller():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    return cast(interface, POINTER(IAudioEndpointVolume))


def volume_up():
    volume = get_volume_controller()

    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)

    speak("Volume increased")


def volume_down():
    volume = get_volume_controller()

    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)

    speak("Volume decreased")


def mute_volume():
    volume = get_volume_controller()

    volume.SetMute(1, None)

    speak("Volume muted")


def unmute_volume():
    volume = get_volume_controller()

    volume.SetMute(0, None)

    speak("Volume unmuted")