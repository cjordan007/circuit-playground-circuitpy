#runs a light show
#last edit: 8/1/20

import time
import random
from adafruit_circuitplayground import cp

random.seed(0)
cp.pixels.brightness = 0.1
cp.pixels.fill((0, 0, 0))
cp.pixels.show()

RED = (255, 0, 0)
ORANGE = (255, 102, 0)
YELLOW = (252, 235, 3)
GREEN = (26, 255, 0)
BLUE = (0, 204, 255)
PURPLE = (177, 3, 252)
PINK = (255, 0, 89)
NEO_OFF = (0, 0, 0)

counter = 0

while True:

    if cp.button_a:

        if counter == 0:
            cp.pixels.fill(RED)
            time.sleep(2)
            cp.pixels.fill(NEO_OFF)
            time.sleep(0.1)
            counter = counter + 1
        elif counter == 1:
            cp.pixels.fill(ORANGE)
            time.sleep(2)
            cp.pixels.fill(NEO_OFF)
            counter = counter + 1
        elif counter == 2:
            cp.pixels.fill(YELLOW)
            time.sleep(2)
            cp.pixels.fill(NEO_OFF)
            counter = counter + 1
        elif counter == 3:
            cp.pixels.fill(GREEN)
            time.sleep(2)
            cp.pixels.fill(NEO_OFF)
            counter = counter + 1
        elif counter == 4:
            cp.pixels.fill(BLUE)
            time.sleep(2)
            cp.pixels.fill(NEO_OFF)
            counter = counter + 1
        elif counter == 5:
            cp.pixels.fill(PURPLE)
            time.sleep(2)
            cp.pixels.fill(NEO_OFF)
            counter = counter + 1
        elif counter == 6:
            cp.pixels.fill(PINK)
            time.sleep(2)
            cp.pixels.fill(NEO_OFF)
            counter = counter + 1
        elif counter > 6:
            counter = 0

    if cp.touch_A1:

        for x in range(4):
            cp.pixels[x] = PINK  # pink on
            time.sleep(0.25)
        cp.pixels[4] = PURPLE  # purple on
        time.sleep(0.25)
        cp.pixels[5] = PURPLE  # purple on
        time.sleep(0.25)

        for y in range(6, 10):
            cp.pixels[y] = BLUE  # blue on
            time.sleep(0.25)

        time.sleep(1)

        for x in range(10):
            cp.pixels[x] = NEO_OFF  # off
            time.sleep(0.25)

    if cp.touch_A6:
        cp.pixels[1] = RED
        time.sleep(0.25)
        cp.pixels[2] = ORANGE
        time.sleep(0.25)
        cp.pixels[3] = YELLOW
        time.sleep(0.25)
        cp.pixels[6] = GREEN
        time.sleep(0.25)
        cp.pixels[7] = BLUE
        time.sleep(0.25)
        cp.pixels[8] = PURPLE
        time.sleep(2)

        for x in range(10):
            cp.pixels[x] = NEO_OFF
            time.sleep(0.25)

    if cp.touch_A4:
        i = 0
        pixel_on = random.randrange(0, 10)
        x = random.randrange(0, 256)
        y = random.randrange(0, 256)
        z = random.randrange(0, 256)
        cp.pixels[pixel_on] = (x, y, z)
        time.sleep(1)
        for x in range(10):
            cp.pixels[x] = NEO_OFF  # off
            time.sleep(0.1)

    if cp.switch:
        for x in range(4):
            cp.pixels[x] = PINK
            time.sleep(0.1)
        cp.pixels[4] = PURPLE
        time.sleep(0.1)
        cp.pixels[5] = PURPLE
        time.sleep(0.1)

        for y in range(6, 10):
            cp.pixels[y] = BLUE
            time.sleep(0.1)

        time.sleep(3)

        for x in range(10):
            cp.pixels[x] = NEO_OFF
            time.sleep(0.1)

        time.sleep(1)

        cp.pixels[1] = RED
        time.sleep(0.1)
        cp.pixels[2] = ORANGE
        time.sleep(0.1)
        cp.pixels[3] = YELLOW
        time.sleep(0.1)
        cp.pixels[6] = GREEN
        time.sleep(0.1)
        cp.pixels[7] = BLUE
        time.sleep(0.1)
        cp.pixels[8] = PURPLE
        time.sleep(2)

        for x in range(10):
            cp.pixels[x] = NEO_OFF
            time.sleep(0.1)