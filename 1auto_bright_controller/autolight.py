from microbit import *
light1 = Image("99999:99999:99999:99999:99999")
light2 = Image("55555:55555:55555:55555:55555")
light3 = Image("00000:00000:00000:00000:00000")

while True:
    level = display.read_light_level() #밝기 측정
    if level < 10: # 10보다 작다면
        display.show(light1) #제일 밝게
    elif level >= 10 and level < 100: #10보다 크거나 같고, 100보다 작으면
        display.show(light2) #중간 밝기
    else:
        display.show(light3) #출력하지 않음
