import RPi.GPIO as g
import time

list = [21, 20, 16, 12, 7, 8, 25, 24]

g.setmode(g.BCM)
g.setup(list,g.OUT)

for k in range(3):
    for i in list:
        g.output(i,1)
        time.sleep(0.5)
        g.output(i,0)
        i = i + 1
g.output(list,0)
g.cleanup()


