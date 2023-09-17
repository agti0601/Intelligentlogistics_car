from machine import Pin, PWM
import time
 
# 创建引脚对象
led = Pin(48, Pin.OUT)
led.value(0)