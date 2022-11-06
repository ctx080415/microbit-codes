from microbit import *

while True:
    sound = pin0.read_analog()
    display.show(sound)
    if sound > 100:
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)
    sleep(1000)
    display.clear()

