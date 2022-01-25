import time
import opc
import random
import tkinter as tk

#leds = [(255,255,255)]*360 #white

#client = opc.Client('localhost:7890')
#client.put_pixels(leds)
#client.put_pixels(leds)

window = tk.Tk()
window.title('The Greatest Show')

text = tk.Label(text = 'Which show would you like to watch first?')
text.pack()

text = tk.Label2(text = 'Show 1')
text.pack()

text = tk.Label3(text = 'Show 2')
text.pack()

text = tk.Label4(text = 'Show 3')
text.pack()

#text = tk.Label5(text = 'Show 4')
#text.pack()

#text = tk.Label6(text = 'Random show')
#text.pack()

#def start_animation():

button = tk.Button1(text ='start', width = 10, height = 1,)
#                   command = start_animation)
button.pack(padx = 5, pady = 5)

button = tk.Button2(text ='start', width = 10, height = 1,)
#                   command = start_animation)
button.pack(padx = 5, pady = 5)

button = tk.Button3(text ='start', width = 10, height = 1,)
#                   command = start_animation)
button.pack(padx = 5, pady = 5)

#button = tk.Button4(text ='start', width = 10, height = 1,
#                    command = start_animation)
#button.pack(padx = 5, pady = 5)

#button = tk.Button5(text ='start', width = 10, height = 1,
#                   command = start_animation )
#button.pack(padx = 5, pady = 5)

frame = tk.Frame(master = window)
label = tk.Label(master = window, text = 'Frame!', bg = 'black', fg = 'white')

frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 3)

#text.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'n')
#button.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = 'se')
#label.grid(column = 1, row = 1, padx = 5, pady = 5, sticky = 'nsew')




#for i in range(3):
#   window.columnconfigure(i, weight = 1, minsize=75)
#  window.rowconfigure(i, weight = 1, minsize=75)

#for row in range(3):
#    for col in range(3):
#        frame = tk.Frame(master = window, relief = tk.RAISED, borderwidth = 1)
#        frame.grid(row = row, column = col, padx = 5, pady = 5)
#        label = tk.Label(master = frame, text = f"{row}, {col}")
#        label.pack()


window.mainloop()
