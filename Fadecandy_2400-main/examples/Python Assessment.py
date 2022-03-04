import opc
import time
import random
import tkinter as tk

leds = [(0,0,0)]*360 #black for every pixel

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

window = tk.Tk()
window.title('Game')

def redcolor(): #create a function for the red color
    leds = [(255,0,0)]*360

def greencolor(): #create a function for the green color
    leds = [(0,255,0)]*360

def bluecolor(): #create a function for the blue color
    leds = [(0,0,255)]*360
    
color_list = [redcolor, greencolor, bluecolor] #creating a list with all the colors


def firstanim(): #defining what the first animation is
    led = 0
    while led<60:
        for rows in range(3):   #adding rows
            leds[led + rows*60] = (255,0,0)
        for rows in range(3,6):
            leds[59-led + rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.05)
        led = led + 1
    
    led = 0
    while led<60:
        for rows in range(3):   #adding rows
            leds[led + rows*60] = (0,0,0)
        for rows in range(3,6):
            leds[59-led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        time.sleep(.05)
        led = led + 1

    led = 0
    while led<30:
        for rows in range(6):   #adding rows
            leds[led + rows*60] = (255,0,0)
            leds[59-led + rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(.05)
        led = led + 1

    led = 0
    while led<30:
        for rows in range(6):   #adding rows
            leds[led + rows*60] = (0,0,0)
            leds[59-led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        time.sleep(.05)
        led = led + 1

def secondanim():
    
    
"""     
    led = 0
    leds = [(255,0,0)]*360
    client.put_pixels(leds)
    time.sleep(.05)
    led = led + 1
    
    led = 0
    leds = [(0,0,0)]*360
    client.put_pixels(leds)
    time.sleep(.05)
    led = led + 1

    led = 0
    leds = [(255,0,0)]*360
    client.put_pixels(leds)
    time.sleep(.05)
    led = led + 1
"""
#--------------------------------------------------------------------------------------
#gemoetry of the pop-up window

window.rowconfigure(1, minsize = 20, weight = 1)
window.rowconfigure(2, weight = 3)

#---------------------------------------------------------------------------------------
#buttons of the window for the animations

anim1_button = tk.Button(window, text = 'first anim', command = firstanim)
anim2_button = tk.Button(window, text = 'second anim', command = secondanim)
anim3_button = tk.Button(window, text = 'third anim', command = thirdanim)
anim4_button = tk.Button(window, text = 'fourth anim', command = fourthanim)
anim5_button = tk.Button(window, text = 'fifth anim', command = fifthanim)
exit_button = tk.Button(window, text = 'Exit', command = window.destroy)

#---------------------------------------------------------------------------------------
#layout of the buttons inside of the window


anim1_button.grid(column = 0, row = 1, padx = 5, pady = 5)
anim2_button.grid(column = 1, row = 1, padx = 5, pady = 5)
anim3_button.grid(column = 2, row = 1, padx = 5, pady = 5)
anim4_button.grid(column = 3, row = 1, padx = 5, pady = 5)
anim5_button.grid(column = 4, row = 1, padx = 5, pady = 5)
exit_button.grid(column = 2, row = 3, sticky = 'e', padx = 5, pady = 5)

window.mainloop()

"""
for led in range(60):
    leds[led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)

led = 0
while led<60: #scroll all rows at the same time
    for rows in range(3): #first three rows left to right
        leds[led + rows*60] = (0,0,255)
    for rows in range(3,6): #last three rows reversed (right to left)
        leds[59-led + rows*60] = (50,50,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1


 RED COLOUR

led = 0
while led<30:
    for rows in range(6):   #adding rows
        leds[led + rows*60] = (255,0,0)
        leds[59-led + rows*60] = (255,0,0)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

#GREEN COLOUR
led = 0
while led<30:
    for rows in range(6):
        leds[led + rows*60] = (0,255,0)
        leds[59-led + rows*60] = (0,255,0)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

#BLUE COLOUR
led = 0
while led<30:
    for rows in range(6):
        leds[led + rows*60] = (0,0,255)
        leds[59-led + rows*60] = (0,0,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
"""
