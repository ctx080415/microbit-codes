from microbit import *
import neopixel
from random import randint
neo = neopixel.NeoPixel(pin0, 30) # 30개의 전구를 사용함

while True:
    light = display.read_light_level() # 빛의 값을 측정하여 light라는 변수에 저장
    display.scroll(light) # 마이크로비트 디스플레이에 값 출력
    sleep(1000)
    
    if light >= 20: # 만약 빛 값이 20이 넘는다면
        neo.clear() # 불 끄기
    else: #그 외(20 이하)
        for pixel_id in range(0, len(neo)): # 픽셀 개수(30)만큼 반복
            color1 = randint(0, 255) # 0부터 255의 숫자를 color1에 저장
            color2 = randint(0, 255)# 0부터 255의 숫자를 color2에 저장
            color3 = randint(0, 255)# 0부터 255의 숫자를 color3에 저장
            color4 = randint(0, 255)# 0부터 255의 숫자를 color4에 저장
            
            neo[pixel_id] = (color1, color2, color3) # 세개의의 숫자중 랜덤으로 출력
            neo.show() # 불 켜기기
            sleep(100)
