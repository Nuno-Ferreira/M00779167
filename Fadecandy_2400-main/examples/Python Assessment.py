import opc
import time
import random
import colorsys
import tkinter as tk

leds = [(0,0,0)]*360 #black for every pixel

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

window = tk.Tk()  
window.title('Game')

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness

#---------------------------------------------------------------------------------
#first animation

def firstanim(): #defining what the first animation is
    led = 0
    while led<60:
        for rows in range(3):   #adding rows
            leds[led + rows*60] = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #setting every led as a random color
        for rows in range(3,6):
            leds[59-led + rows*60] = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #setting every led as a random color
        client.put_pixels(leds)
        time.sleep(.05)
        led = led + 1
    
    led = 0
    while led<60:
        for rows in range(3):   #adding rows
            leds[led + rows*60] = (0,0,0) #setting the leds from the first 3 rows black to get swiping motion
        for rows in range(3,6):
            leds[59-led + rows*60] = (0,0,0) #setting the leds from the last 3 rows black to get swiping motion
        client.put_pixels(leds)
        time.sleep(.05)
        led = led + 1

    led = 0
    while led<30:
        for rows in range(6):   #adding rows
            leds[led + rows*60] = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #setting every led as a random color
            leds[59-led + rows*60] = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #setting every led as a random color
        client.put_pixels(leds)
        time.sleep(.05)
        led = led + 3

    led = 0
    while led<30:
        for rows in range(6):   #adding rows
            leds[led + rows*60] = (0,0,0) #setting every led as black
            leds[59-led + rows*60] = (0,0,0) #setting every led as black
        client.put_pixels(leds)
        time.sleep(.05)
        led = led + 3
        
#---------------------------------------------------------------------------------
#second animation
        
def secondanim(): #defining what the second animation is
    led_colour = [(0,0,0)]*360 #setting every led as black
    for item in enumerate(led_colour): 
        time.sleep(0.005)
        if item[0]%2 == 0: #making every even number the colour chosen next
            r, g, b = item[1]
            r = 155
            g = 211
            b = 221
            new_colour =(r,g,b) #making new tuple with values of rgb
            led_colour[item[0]] = new_colour #defining colour of even number led
        if item[0]%2 != 0: #making every odd number the colour chosen next
            r, g, b = item[1]
            r = 241
            g = 97
            b = 73
            new_colour2 =(r,g,b) #making new tuple with values of rgb
            led_colour[item[0]] = new_colour2 #defining colour of odd number led
            
        client.put_pixels(led_colour) #send the values
        client.put_pixels(led_colour)

    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

#---------------------------------------------------------------------------------
#third animation
    
def thirdanim(): #defining what the third animation is
    for hue in range(360):
        rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue-10, hue+10)/360.0, s, v) #colorsys returns floats between 0 and 1
        r_float = rgb_fractional[0] #extract floating point numbers mentioned before
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with new values
        leds[hue]=rgb
        client.put_pixels(leds)
        time.sleep(0.01) 

#--------------------------------------------------------------------------------------
#tkinter menu configuration
#gemoetry of the pop-up window

window.rowconfigure(1, minsize = 40, weight = 1) #configuring the size of the rows
window.rowconfigure(2, weight = 3)

#---------------------------------------------------------------------------------------
#buttons of the window for the animations

anim1_button = tk.Button(window, text = 'first anim', command = firstanim)
anim2_button = tk.Button(window, text = 'second anim', command = secondanim)
anim3_button = tk.Button(window, text = 'third anim', command = thirdanim)
exit_button = tk.Button(window, text = 'Exit', command = window.destroy)

#---------------------------------------------------------------------------------------
#layout of the buttons inside of the window


anim1_button.grid(column = 0, row = 1, padx = 5, pady = 5)
anim2_button.grid(column = 1, row = 1, padx = 5, pady = 5)
anim3_button.grid(column = 2, row = 1, padx = 5, pady = 5)
exit_button.grid(column = 1, row = 3, sticky = 'e', padx = 5, pady = 5)

window.mainloop()
