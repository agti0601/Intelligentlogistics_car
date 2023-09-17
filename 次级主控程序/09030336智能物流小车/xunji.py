# main.py -- put your code her
from machine import Pin
import time

#定义引脚
sw7 = Pin(46,Pin.IN)
sw6 = Pin(9,Pin.IN)
sw5 = Pin(10,Pin.IN)

# sw6 = Pin(3,Pin.IN)
# sw7 = Pin(46,Pin.IN)
# sw8 = Pin(9,Pin.IN)
# 返回电平值
while True:
    time.sleep(1)  
    print('sw7:%d,sw5:%d,sw6:%d' %(sw7.value(),sw5.value(),sw6.value()))
