import pyvjoy
import pygame
import time

# Initialize pygame
pygame.joystick.init()
pygame.init()  # don't worry if your linter complains; this works.

# Initialize hardware joystick
HW_JOY_ID = 0
HW_JOY = pygame.joystick.Joystick(HW_JOY_ID)
HW_JOY.init()

# Initialize software joystick
SW_JOY = pyvjoy.VJoyDevice(1)

# Maximum joystick input that software joystick will accept
TOP = 0x8000

# Minimum joystick input that software joystick will accept
BOTTOM = 0x1


class AXISMAP:
    """ A class full of static constants identifying axis ID's"""

    LEFTX = 0
    LEFTY = 1
    TRIGGER = 2
    RIGHTY = 3
    RIGHTX = 4


def _computeTank() -> tuple:
    """
    Compute a joystick output to emulate, given the tank drive input on the
    real joystick

    Returns:
        tuple -- A tuple containing the hex values (x, y), where x and y are
        to be sent to the emulated joystick
    """

    left = -HW_JOY.get_axis(AXISMAP.LEFTY)
    right = -HW_JOY.get_axis(AXISMAP.RIGHTY)

    print("Left HW:", left, "Right HW", right)

    avgSpeed = (left + right) / 2
    moment = (left - right) / 2

    return (_toHex(moment), _toHex(avgSpeed))


def _toHex(num: float) -> int:
    """
    Converts a number between the range -1 and 1 inclusive to a hex number
    between 0x1 and 0x8000

    Arguments:
        num {float} -- A number that pygame read from the hardware joystick

    Returns:
        int -- A base-16 integer to send to the software joystick
    """

    num += 1
    num *= TOP / 2
    return int(hex(int(num + 0.5)), 16)


def _toInt(boolean: bool) -> int:
    """
    Converts a boolean to an integer

    Arguments:
        boolean {bool} -- A boolean

    Returns:
        int -- 1 if boolean is true, 0 if boolean is false
    """

    if(boolean):
        return 1
    return 0


if __name__ == "__main__":
    print("Pygame detects", pygame.joystick.get_count(), "joysticks connected")
    print("The joystick at", HW_JOY_ID, "has", HW_JOY.get_numaxes(), "axes")
    print("If the following numbers do not change when you move the joysticks, something is wrong . . .")
    # Let user glance at log info above
    time.sleep(0.5)

    while True:
        # update joystick data
        pygame.event.pump()

        # compute normal joystick input from tank drive input
        target_x, target_y = _computeTank()

        # send to software joystick
        SW_JOY.data.wAxisXRot = target_x  # intentionally on other joystick
        SW_JOY.data.wAxisY = target_y

        # Update software joystick
        SW_JOY.update()
