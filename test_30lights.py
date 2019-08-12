# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

#sleep time
wait = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

pixels.fill((0, 0, 0))
pixels.show()
time.sleep(wait)


pixels.fill((0, 255, 0))
pixels.show()
time.sleep(wait)

print("pixel 0")
pixels[0] = (255, 0, 0)
pixels.show()
time.sleep(wait)

print("pixel 7")
pixels[7] = (255, 0, 0)
pixels.show()
time.sleep(wait)

print("pixel 14")
pixels[14] = (255, 0, 0)
pixels.show()
time.sleep(wait)


print("pixel 16")
pixels[16] = (255, 0, 0)
pixels.show()
time.sleep(wait)

print("pixel 23")
pixels[23] = (255, 0, 0)
pixels.show()
time.sleep(wait)
