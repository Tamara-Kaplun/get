import RPi.GPIO as g
import time
import random

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number =  []
for i in range(8):
    number.append(random.randint(0,1))

g.setmode(g.BCM)
g.setup(dac,g.OUT)

g.output(dac,number)

time.sleep(5)
g.output(dac,0)
g.cleanup()
