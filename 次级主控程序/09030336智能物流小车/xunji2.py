import dianji as dj
# main.py -- put your code her
from machine import Pin
import time

#定义引脚
sw7 = Pin(46,Pin.IN)
sw6 = Pin(9,Pin.IN)
sw5 = Pin(10,Pin.IN)
sw9 = Pin(37,Pin.IN)
sw10 = Pin(36,Pin.IN)
# sw6 = Pin(3,Pin.IN)
# sw7 = Pin(46,Pin.IN)
# sw8 = Pin(9,Pin.IN)
# 返回电平值
i = 0
speed = 600
while True:
    time.sleep_ms(1)
    dj.stop()
    print('i',i,'sw7:%d,sw5:%d,sw6:%d,sw9:%d,sw10:%d' %(sw7.value(),sw5.value(),sw6.value(),sw9.value(),sw10.value()))
    if i < 3:
        if sw6.value() == 1:
            dj.back(speed)
        elif sw7.value() == 1:
            dj.right(speed)
        elif sw5.value() == 1:
            dj.left(speed)
        elif sw10.value() == 1:
            time.sleep(2)
            i +=1
    else:
        dj.left(speed)
        time.sleep(3)
        i == 0
        dj.stop()
        break
        

