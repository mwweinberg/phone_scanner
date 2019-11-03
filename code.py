import time
import board
from analogio import AnalogIn
import neopixel
import random

NUMPIXELS = 8  # Circuit Playground Express has 10 pixels
ORDER = neopixel.RGBW
pixels = neopixel.NeoPixel(board.D13, NUMPIXELS, auto_write=False)  # CPX NeoPixels
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground


state_tracker = 0



def init_sequence(light):
    for i in range (1, 255, 5):
            pixels[light] = (i, i, 0)
            pixels.show()
            time.sleep(0.05)
            print("phase 1 " + str(i))
        #dim briefly
    for i in range (255, 50, -5):
        pixels[light] = (i,i,0)
        pixels.show()
        time.sleep(0.01)
        print("phase 2 " + str(i))
    #fully initialize
    for i in range (50, 255, 5):
        pixels[light] = (i, i, 0)
        pixels.show()
        time.sleep(0.1)
        print("phase 3 " + str(i))

def red_pixel(val):
    pixels[val] = (50, 0, 0)
    pixels.show()
    time.sleep(0.1)

def final_light(val):
    picker = random.randint(1, 3)
    #1/3 of the time the final light turns yellow istead of red  - you are in trouble
    if picker == 3:
        pixels[val] = (50, 50, 0)
    else:
        pixels[val] = (50, 0, 0)
    pixels.show()

def shutdown_sequence():
    for i in range (255, 0, -10):
        #makes all of the pixels red and then slowly turns then off
        RED = (0, 0, 0)
        pixels.fill(RED)
        pixels.show()
        print(i)
        time.sleep(0.5)
    state_tracker = 0

while True:

    #potentiometer values are between like 50 and 64000
    if potentiometer.value > 30000:
        #if this is the first time the state has switched
        if state_tracker == 0:
            init_sequence(0)
            for i in range (1, 4):
                red_pixel(i)
            final_light(5)
            state_tracker = 1
        #just more of the same
        else:
            pass

    #turn off the lights (lit pixels stay lit until told otherwise)
    else:
        if state_tracker == 1:
            shutdown_sequence()
        else:
            pass

    print((potentiometer.value,))
    time.sleep(0.25)