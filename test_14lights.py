# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 58

#sleep time
wait = 0.03

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
colors = [white, red, green, blue, black]

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,pixel_order=ORDER)



while True:
    
    i=0
    for i in range(num_pixels)[::2]:
        #print(i)
        pixels[i] = (255, 255, 255)
        #pixels[i] = (0, 0, 0)
    pixels.show()
    

# --- turn on all lights and change from 5 different colors
while True:
    for i in range(len(colors)):
        pixels.fill((colors[i]))
        pixels.show()
        time.sleep(wait)



