import music
from microbit import *

song_hello = ["C4:4", "D", "E", "C", "C", "D", "E", "C", "E", "F", "G:8", "E:4", "F", "G:8"] #동요 '안녕'재생(출처: https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/music.html)

carol =  [ 'e:2','e:2','e:4', 'e:2','e:2','e:4', 'e:2','g:2','c','d', 'e:8'] #크리스마스 캐롤

while True:
    if button_a.is_pressed():
        music.play(carol)
    elif button_b.is_pressed():
        music.play(song_hello)
