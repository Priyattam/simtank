import pyvjoy
import pygame
import time
import os 
import random

pygame.joystick.init()
pygame.init()

HW_JOY = pygame.joystick.Joystick(0)  # The joystick plugged into the computer
HW_JOY.init()

SW_JOY = pyvjoy.VJoyDevice(1)

TOP = 0x8000
BOTTOM = 0x1
class AXISMAP:
    LEFTY = 1
    RIGHTY = 3
    LEFTX = 0
    TRIGGER = 2
    RIGHTX = 4

def _computeTank():
    left = -HW_JOY.get_axis(AXISMAP.LEFTY)
    right = -HW_JOY.get_axis(AXISMAP.RIGHTY)

    print(left, right)

    avgSpeed = (left + right) / 2
    moment = (right - left) / 2
    
    return (_toHex(moment), _toHex(avgSpeed))

def _toHex(num):
    num += 1
    num *= TOP / 2
    return int(hex(int(num + 0.5)), 16)

def _toInt(boolean):
    if(boolean):
        return 1
    return 0

if __name__ == "__main__":
    print(pygame.joystick.get_count())
    print(HW_JOY.get_numaxes())
    time.sleep(0.5)
    while True:
        pygame.event.pump()  # update joystick data
        target_x, target_y = _computeTank()
        
        SW_JOY.data.wAxisXRot = target_x  # intentionally on other joystick
        SW_JOY.data.wAxisY = target_y

        # SW_JOY.set_axis(pyvjoy.HID_USAGE_Y, target_y)  # left y
        # SW_JOY.set_axis(pyvjoy.HID_USAGE_RX, target_x)  # right x

        button6 = _toInt(HW_JOY.get_button(6))
        print(button6)
        print()

        SW_JOY.update()
        SW_JOY.set_button(6, button6)



        