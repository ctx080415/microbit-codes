from microbit import *
import neopixel
from random import randint
np = neopixel.NeoPixel(pin0, 24)

while True:
    light_level = display.read_light_level()
    display.scroll(light_level)
    sleep(1000)
    
    if light_level >= 50:
        np.clear()
    else:
        for pixel_id in range(0, len(np)):
            color1 = randint(0, 255)
            color2 = randint(0, 255)
            color3 = randint(0, 255)
            
            np[pixel_id] = (color1, color2, color3)
            np.show()
            sleep(100)
