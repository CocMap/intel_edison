import mraa
import time

x = mraa.Gpio(9)            #x = led, put in Gpio 8 in the board
x.dir(mraa.DIR_OUT)

while True: 
    x.write(1)
    time.sleep(1)
    x.write(0)
    time.sleep(1)

