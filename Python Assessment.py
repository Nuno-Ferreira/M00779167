import opc
import time
import random

leds = [(255,255,255)]*360 #white for every pixel

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

value = input("Welcome to the show! What would you like to see first? \n Choose from the options below:")

print("What show would you like to see first? \n Answer:", value)

