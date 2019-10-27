import time
import board
from analogio import AnalogIn
import neopixel

NUMPIXELS = 8  # Circuit Playground Express has 10 pixels
pixels = neopixel.NeoPixel(board.D13, NUMPIXELS, auto_write=False)  # CPX NeoPixels
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

#this is a funciton from the demo that can be deleted
def show_value(val):            # Show value 0-9 on CPX NeoPixels
    for i in range(val):
        pixels[i] = (50, 0, 0)  # Red
    for i in range(val, NUMPIXELS):
        pixels[i] = (0, 0, 0)
    pixels.show()
    return

while True:

    #potentiometer values are between like 50 and 64000
    if potentiometer.value > 30000:
        #light up the first pixel
        pixels[0] = (50, 0, 0)
        pixels.show()
        #wait...
        time.sleep(0.5)

        #light up the second pixel
        pixels[3] = (0, 50, 0)
        pixels.show()
        time.sleep(0.5)

        #slowly light up the third pixel
        for i in range (1, 50):
            print(i)
            pixels[5] = (0, 0, i)
            pixels.show()
            time.sleep(0.1)
    #turn off the lights (lit pixels stay lit until told otherwise)
    else:
        pixels[0] = (0, 0, 0)
        pixels[3] = (0, 0, 0)
        pixels[5] = (0, 0, 0)
        pixels.show()
    print((potentiometer.value,))
    time.sleep(0.25)

    #this is also all from the demo and can probably be deleted

    #show_value(int(potentiometer.value / 65520 * NUMPIXELS))  # Show on NeoPixels
    #print((potentiometer.value,))                             # Print value

    #time.sleep(0.25)                   # Wait a bit before checking all again