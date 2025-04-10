import RPi.GPIO as g
leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
g.setmode(g.BCM)
g.setup(leds, g.OUT)
g.setup(aux, g.IN)
g.output(leds, 0)
g.cleanup()