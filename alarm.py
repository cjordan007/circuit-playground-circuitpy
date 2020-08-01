import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.02

def neo_sequence_on_long():
    for x in range(10):
        cpx.pixels[x] = (255, 0, 0)
        time.sleep(1)

def neo_sequence_on_short():
    for x in range(10):
        cpx.pixels[x] = (255, 0, 0)
        time.sleep(0.05)

def neo_sequence_on_green():
    for x in range(10):
        cpx.pixels[x] = (0, 255, 0)
        time.sleep(0.05)

def neo_sequence_off():
    for x in range(10):
        cpx.pixels[x] = (0, 0, 0)
        time.sleep(0.05)

def light_monitor():
    print((cpx.light,))
    time.sleep(0.1)
    return cpx.light

while True:
    print((cpx.light,))
    time.sleep(0.1)
    if (cpx.light > 250):
        neo_sequence_on_long()

        if (cpx.switch):
            neo_sequence_off()
            neo_sequence_on_green()
            neo_sequence_off()
        else:
            neo_sequence_off()
            neo_sequence_on_short()
            neo_sequence_off()
            neo_sequence_on_short()