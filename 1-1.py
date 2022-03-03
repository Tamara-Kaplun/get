import RPi.GPIO as bebra
import time

bebra.setmode(bebra.BCM)
bebra.setup(14, bebra.OUT )
bebra.setup(15,bebra.IN )
bebra.output(14,0)
while True:
    bebra.output(14,bebra.input(15))
