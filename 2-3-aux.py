import RPi.GPIO as g


list = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3,2]

g.setmode(g.BCM)
g.setup(list,g.OUT)
g.setup(aux,g.IN)

g.output(list,1)

while (1):
    for i in range(8):
        g.output(list[i],g.input(aux[i]))
        i=i+1



