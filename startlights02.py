#import libraries
import board
import neopixel
import array as arr

import datetime
import time
from time import gmtime, strftime

print("starting lights")

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
digit = ((1, 2, 3, 4, 5, 6), (1, 6), (0, 2, 3, 5, 6), (0, 1, 2, 5, 6), (0, 1, 4, 6), (0, 1, 2, 4, 5), (0, 1, 2, 3, 4, 5), (1, 5, 6), (0, 1, 2, 3, 4, 5, 6), (0, 1, 4, 5, 6))

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
        startcountdown = 7
    elif (weekday == 4):
        startcountdown = 1
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
        """             
        if (d3%2 == 0):
            #blinking_dots_on()
            blinking_dots("on")
        else:
            #blinking_dots_off()
            blinking_dots("on")  
        """
        # dots always on
        pixels[14] = white
        pixels[15] = white   
        pixels.show()
        secsleep = get_time_to_sleep()
        time.sleep(secsleep)
        display_current_time(d0, d1, d2, d3)

        
# --- check digit lights - show each number (0-9) in each of digit (0-3)
def check_digits():
    for n in range(len(digit)):
        time.sleep(wait*3)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(wait)
        a = str(n) + ") -- ("
        for m in range(len(digit[n])):
            a= a + str((digit[n][m])) + ","
            pixels[digit[n][m]] = white
            pixels.show()
        a = a + ")"
        print(a)

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
    pixels.fill((0,0,0))
    pixels.show()
    for n in range(len(currTime)):
        numdig = d[n][1]
        for m in range(len(digit[currTime[n]])):
            if (n==0 and d0 ==0):
                pixels[digit[currTime[n]][m]+ numdig] = black
            else:
                pixels[digit[currTime[n]][m]+ numdig] = white
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
    print(datetime.datetime.now().time())    

def blinking_dots_on():        
    # turn on
    pixels[14] = (255, 255, 255)
    pixels[15] = (255, 255, 255)
    pixels.show()
    secsleep = get_time_to_sleep()
    time.sleep(secsleep)
    print(datetime.datetime.now().time())    

def blinking_dots_off():  
    # turn off
    pixels[14] = (0, 0, 0)
    pixels[15] = (0, 0, 0)
    pixels.show()
    secsleep = get_time_to_sleep()
    time.sleep(secsleep)  
    print(datetime.datetime.now().time())       

# --- get the number of miliseconds that needs to be paused until the next full second
def get_time_to_sleep():
    milisec = get_current_time()
    ttsleep = (999990 - milisec[5])*.000001
    return ttsleep
    

# Returns current time as an array of values: 
#           currentDT, weekday, hours, minutes, seconds, milsec
#              0         1        2       3        4       5
currentTime = get_current_time()

# setting time to sleep until next second
timetosleep = (999990 - currentTime[5])*.000001
time.sleep(timetosleep)

# Just for testing purposes; the line below can be commented out
print(datetime.datetime.now().time())

# Currently not being used
trigger = True

# Just for testing purposes; the line below can be commented out
print("setting digit values")            
set_digit_values(currentTime[2], currentTime[3], currentTime[4])

# set counter as the number of seconds in the current time
counter = int(datetime.datetime.now().strftime('%S'))
check = 59

# --- blinking dots & updating digits
print(datetime.datetime.now().time())
while True:   
    if (counter > check):
        getHMS = get_current_time()
        print(getHMS[2])
        print(startcountdownat)
        print(getHMS[3])
        
        if (getHMS[2] == startcountdownat and getHMS[3] == 58 ):
            count_down()        
        else:
            counter = set_digit_values(getHMS[2], getHMS[3], getHMS[4]) 
    # turn on
    pixels[14] = (255, 255, 255)
    pixels[15] = (255, 255, 255)
    pixels.show()
    secsleep = get_time_to_sleep()
    time.sleep(secsleep)
    counter += 1
    #print(counter)
    #print(datetime.datetime.now().time())    

    # turn off
    pixels[14] = (0, 0, 0)
    pixels[15] = (0, 0, 0)
    pixels.show()
    secsleep = get_time_to_sleep()
    time.sleep(secsleep)  
    counter += 1
    #print(counter)
    #print(datetime.datetime.now().time())       


quit()
   

    


