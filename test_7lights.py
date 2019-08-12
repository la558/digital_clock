# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 7

#sleep time
wait = 0.3

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,pixel_order=ORDER)

pixels.fill((255, 255, 255))
pixels.show()
time.sleep(wait)

pixels.fill((0, 0, 0))
pixels.show()
time.sleep(wait)

print("pixel 0")
pixels[0] = (255, 0, 0)
pixels.show()
time.sleep(wait)

print("pixel 1")
pixels[1] = (255, 255, 0)
pixels.show()
time.sleep(wait)

print("pixel 2")
pixels[2] = (255, 0, 255)
pixels.show()
time.sleep(wait)


print("pixel 3")
pixels[3] = (255, 0, 0)
pixels.show()
time.sleep(wait)

print("pixel 4")
pixels[4] = (255, 255, 0)
pixels.show()
time.sleep(wait)

print("pixel 5")
pixels[5] = (255, 0, 255)
pixels.show()
time.sleep(wait)

print("pixel 6")
pixels[6] = (255, 0, 0)
pixels.show()
time.sleep(wait)
