from machine import Pin
import time

#defines pins for deciding recieve pin
rfPin = Pin(16, Pin.IN, Pin.PULL_DOWN)
irPin = Pin(17, Pin.IN, Pin.PULL_DOWN)

#set default mode to null until decided later to avoid error
recieveMode = -1

if rfPin.value == 1:
    #set recieve mode to rf
    recieveMode = 1
elif irPin.value == 0:
    #set recieve mode to ir
    recieveMode = 0

