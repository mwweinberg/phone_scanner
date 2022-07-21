"""This example lights up half the NeoPixels red while button A is being pressed, and half the
NeoPixels green while button B is being pressed."""
from adafruit_circuitplayground import cp
import time
from digitalio import DigitalInOut, Direction, Pull
import board

cp.pixels.brightness = 1
cp.pixels.fill((0, 0, 0))  # Turn off the NeoPixels if they're on!

button_g = DigitalInOut(board.A4)
button_g.direction = Direction.INPUT
button_g.pull = Pull.UP

def touch_g():
    return not button_g.value

def phone_sequence():
    #yellow sequence
    for i in range(0, 10, 1):
        cp.pixels[i] = (255, 255, 0)
        time.sleep(.2)
    cp.play_tone(282, .5)
    cp.pixels.fill((0, 0, 0))
    #blue sequence
    for i in range(0, 10, 1):
        cp.pixels[i] = (0, 0, 255)
        time.sleep(.2)
    cp.play_tone(282, .5)
    cp.pixels.fill((0, 0, 0))
    #green sequence
    for i in range(0, 10, 1):
        cp.pixels[i] = (0, 255, 0)
        time.sleep(.2)
    cp.play_tone(322, .2)
    cp.play_tone(322, .2)
    cp.pixels.fill((0, 0, 0))

while True:
    if cp.button_a:
        #cp.pixels[0:5] = [(255, 0, 0)] * 5
        phone_sequence()
    else:
        cp.pixels.fill((0, 0, 0))

    if cp.button_b:
        phone_sequence()
    else:
        cp.pixels.fill((0, 0, 0))
        
    if touch_g():
        phone_sequence()
    else:
        cp.pixels.fill((0, 0, 0))
