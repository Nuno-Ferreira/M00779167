import opc
import time
import random

leds = [(255,255,255)]*360 #white for every pixel

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#value = input("Welcome to the show! What would you like to see first? \n Choose from the options below:")

#print("What show would you like to see first? \n Answer:", value)


#for led in range(60):
#    leds[led] = (255,0,0)
#    time.sleep(.1)
#   client.put_pixels(leds)

#led = 0
#while led<60: #scroll all rows at the same time
#    for rows in range(3): #first three rows left to right
#        leds[led + rows*60] = (0,0,255)
#    for rows in range(3,6): #last three rows reversed (right to left)
#        leds[59-led + rows*60] = (50,50,255)
#    client.put_pixels(leds)
#    time.sleep(.1)
#    led = led + 1

led = 0
while led<60:
    for rows in range(6):
        leds[led + rows*60] = (255,0,0) #add one led in front
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
