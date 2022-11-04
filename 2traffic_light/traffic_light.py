from microbit import *

while True:
    pin0.write_digital(1) #첫 시작은 빨간불(0번핀 빨간 불 켜기)
    sleep(5000) #5초 대기
    pin0.write_digital(0) #빨간불 끄기
    pin1.write_digital(1) #녹색 불 켜기(1번(초록불)핀 켜기)
    for a in range(5): #for문을 사용하여 a에 값을 더해 5초 카운트함
        display.show(5-a) #숫자 세는 것 보여줌
        sleep(1000) #1초 대기
    pin1.write_digital(0)#녹색 불 끄기
   #노란불을 만들려면 빨간색과 녹색 LED를 동시에 켜야함
    pin0.write_digital(1) #빨간색 불 켜기
    pin1.write_digital(1) #초록색 불 끄기
    display.clear()#초기화
    sleep(2000)#2초 대기
    pin0.write_digital(0) #빨간 불 끄기
    pin1.write_digital(0) #초록 불 끄기
