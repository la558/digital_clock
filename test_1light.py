# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 1

#sleep time
wait = 1

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,pixel_order=ORDER)

pixels.fill((255, 255, 255))
pixels.show()
time.sleep(wait)


pixels.fill((0, 0, 0))
pixels.show()
time.sleep(wait)

print("blinking")

for n in range(10):
    if (n%2 == 0):
        print("white")
        pixels[0] = (255, 0, 0)
    else:
        print("color")
        pixels[0] = (0, 0, 255)    
    pixels.show()
    time.sleep(wait)       

