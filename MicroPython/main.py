"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *


# Dimensions
display.scroll("A rectangle has dimensions 5 cm & 3 cm.")
sleep(1)
display.clear()

# Perimeter
display.scroll("The perimeter would be:" + str(2 * (5 + 3)) + "cm.")
sleep(1)
display.clear()

# Area
display.scroll("The area would be:" + str(5 * 3) + "cm ^ 2.")
display.show(Image.HAPPY)
sleep()
display.clear()
