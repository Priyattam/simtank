# SimTank

A small python script that spoofs a joystick to turn tank drive input from a joystick into drive input usable for Euro Truck Simulator

## What is tank drive?

Tank drive is where the left joystick controls the wheels on the left, and the right joystick controls the wheels on the right. This is often used in FIRST Robotics Competition to drive the robot; however, it requires training to be good at using tank drive.

This application should lessen the amount of training required on a real robot by getting the user used to controlling 2 joysticks at once

## How do I use it?

1. Install [Python 3](https://www.python.org/downloads/)

1. Install [vjoy](http://vjoystick.sourceforge.net/site/index.php/download-a-install/download)

1. Put `vJoyInterface.dll` in `pyvjoy.`

    * `vJoyInterface.dll` is likely located in either `C:\Program Files\vJoy\x64` or `C:\Program Files\vJoy\x86` depending on whether your operating system is 32-bit or 64-bit

1. Install `pygame`

    * Open the terminal and type
    * `py -m pip install pygame`

1. Run this package

    * `py simtank`
    * Note that you must be in the directory above this directory (i.e you cannot be `cd`'d into `simtank\`)