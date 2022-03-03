import RPi.GPIO as g
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]


g.setmode(g.BCM)
g.setup(dac,g.OUT)

number = [0, 0, 1, 0, 0, 0, 0, 0]
print (number)

g.output(dac,number)

time.sleep(15)
g.output(dac,0)
g.cleanup()
