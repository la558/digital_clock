#import libraries
import board
import neopixel
import array as arr

import datetime
import time
from time import gmtime, strftime

print("Starting Digital Clock")

# ---
global countdown # declaring Monday through Thursday variable as global
global seccounter   # declaring counter as global and setting its default value as 0
global counter 
global startcountdownat # to define the hour when the countdown shall start
# ---

# Choose an open pin connected to the Data In of the NeoPixel 
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

# Pause time
wait = 0.25

# The order of the pixel colors -
ORDER = neopixel.GRB

# Set attributes to pixels
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

# Initialize counter
counter = 0  

# define which segment needs to be illumnated in each digit (from 0 to 9)
# by status
digit = (("off", "on", "on", "on", "on", "on", "on"), 
("off", "on", "off", "off", "off", "off", "on"), 
("on", "off", "on", "on", "off", "on", "on"), 
("on", "on", "on", "off", "off", "on", "on"), 
("on", "on", "off", "off", "on", "off", "on"), 
("on", "on", "on", "off", "on", "on", "off"), 
("on", "on", "on", "on", "on", "on", "off"), 
("off", "on", "off", "off", "off", "on", "on"), 
("on", "on", "on", "on", "on", "on", "on"), 
("on", "on", "off", "off", "on", "on", "on"))


# Get the weekday in a digit 
weekday = datetime.datetime.today().weekday()

# Define the colors that we will be working with and set them in an array
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
colors = [white, red, green, blue, black]

# --- turn on all lights and change from 5 different colors
for i in range(len(colors)):
    pixels.fill((colors[i]))
    pixels.show()
    time.sleep(wait*3)

# --- returns at what time shall the countdown start
def check_weekday(weekday):
    if (weekday == 0 or weekday == 1 or weekday == 2 or weekday ==3):
        startcountdown = 3
    elif (weekday == 4):
        startcountdown = 4
    else:
        startcountdown = 0    
    return startcountdown;
    
# --- count down from 10 to 0 (to be displayed on the last 10 min of the last hour)
def count_down():         
    d0 = 1
    d1 = 0
    d2 = 0
    d3 = 0
    display_current_time(d0, d1, d2, d3)
    for r in range(599, 0, -1):
        minutes = r //60
        seconds = r % 60
        d0 = 0
        d1 = minutes     
        if (seconds < 10):
            d2 = 0
            d3 = seconds
        else:
            d2 = int(str(seconds)[0:1])
            d3 = int(str(seconds)[1:2])

        # dots always on
        pixels[14] = white
        pixels[15] = white   
        pixels.show()
        secsleep = get_time_to_sleep()
        time.sleep(secsleep)
        display_current_time(d0, d1, d2, d3)

        
# --- check digit lights - show each number (0-9) in each of digit (0-3)
def check_digits():
    for s in range(len(d)):
        for n in range(len(digit)):
            time.sleep(wait)
            pixels.fill((0, 0, 0))
            pixels.show()
            time.sleep(wait)
            for m in range(len(digit[n])):
                if(digit[n][m] == "on"):
                    pixels[m + d[s][1]] = white
                pixels.show()
        time.sleep(wait)
    time.sleep(wait*2)    

# Get the hour where the count down shall start at
startcountdownat = check_weekday(weekday)

# Initialize digit variables (index[0] is the number to be displayed, index [1] is the starting pixel number)
d = [[8,0], [8,7], [8,16], [8,23]]
# Make sure 'd' is treated as a list and not as a tuple, so we can change their values
d = list(d)

# --- light up all digits as number 8
def turn_all_digits_as_8():
    for s in range(len(d) ):
        numdig = d[s][1]
        for p in range(len(digit[8])):        
            pixels[digit[8][p]+ numdig] = white 
            pixels.show()


# --- get current time
def get_current_time():
    currentDT = datetime.datetime.now()
    weekday = int(datetime.datetime.today().weekday())
    hours = int(currentDT.strftime('%I'))
    minutes = int(currentDT.strftime('%M'))
    seconds = int(currentDT.strftime('%S'))
    milsec = int(currentDT.strftime('%f'))
    
    return [currentDT, weekday, hours, minutes, seconds, milsec];
    #          0         1        2       3        4       5

# --- display current time
def display_current_time(d0, d1, d2, d3):
    currTime = (d0, d1, d2, d3)
    for n in range(len(currTime)):
        numdig = d[n][1]
        for m in range(7):
            if (n==0 and d0 ==0):
                pixels[m + numdig] = black
            else:
                if(digit[currTime[n]][m] == "on"):
                    pixels[m + numdig] = white
                else:
                    pixels[m + numdig] = black
            pixels.show()
    


# --- set value for each digit with the current time
def set_digit_values(hours, minutes, seconds):
    #set digits 3 and 4 for minutes
    if (minutes < 10):
        d[2][0] = 0         
        d[3][0] = minutes
    else:
        d[2][0] = int(str(minutes)[0:1])
        d[3][0] = int(str(minutes)[1:2])
    #set digits 1 and 2 for hours       
    if (hours > 12):
        hours = hours - 12   
    if (hours < 10):
        d[0][0] = 0  
        d[1][0] = hours
    else:
        d[0][0] = 1
        d[1][0] = hours - 10  
    
    d0 = d[0][0]
    d1 = d[1][0]
    d2 = d[2][0]
    d3 = d[3][0]
    
    display_current_time(d0, d1, d2, d3)   
    
    return 0;

# --- blinking dots
def blinking_dots(state):  
    if(state == "on"):      
        # turn on
        pixels[14] = white
        pixels[15] = white
    else:
        # turn off
        pixels[14] = black
        pixels[15] = black    
    pixels.show()
    secsleep = get_time_to_sleep()
    time.sleep(secsleep)
    #print(datetime.datetime.now().time())    

# --- get the number of miliseconds that needs to be paused until the next full second
def get_time_to_sleep():
    milisec = get_current_time()
    ttsleep = (999990 - milisec[5])*.000001
    return ttsleep

# check all numbers (0-9) of the 4 digits
check_digits()    

# Returns current time as an array of values: 
#           currentDT, weekday, hours, minutes, seconds, milsec
#              0         1        2       3        4       5
currentTime = get_current_time()

# setting time to sleep until next second
timetosleep = (999990 - currentTime[5])*.000001
time.sleep(timetosleep)

# call function to start the clock           
set_digit_values(currentTime[2], currentTime[3], currentTime[4])

# set counter as the number of seconds in the current time
counter = int(datetime.datetime.now().strftime('%S'))
check = 59

# --- blinking dots & updating digits
#print(datetime.datetime.now().time())
while True:   
    if (counter > check):
        getHMS = get_current_time()
        
        if (getHMS[2] == startcountdownat and getHMS[3] == 35 ):
            count_down()        
        else:
            counter = set_digit_values(getHMS[2], getHMS[3], getHMS[4]) 
    # turn on
    blinking_dots("on")
    counter += 1

    # turn off
    blinking_dots("off")
    counter += 1


quit()
   

    


