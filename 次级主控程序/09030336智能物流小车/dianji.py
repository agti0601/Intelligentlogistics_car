import math
import time
from machine import SoftI2C,Pin,PWM
speed = 600

a = 250
pin1=PWM(Pin(4),freq=1000)  #左前 红1
pin2=PWM(Pin(5),freq=1000)
pin3=PWM(Pin(6),freq=1000)  #左后 红3
pin4=PWM(Pin(7),freq=1000)
pin5=PWM(Pin(15),freq=1000)  #右前 黑5
pin6=PWM(Pin(16),freq=1000)
pin7=PWM(Pin(17),freq=1000)  #左前 红1
pin8=PWM(Pin(18),freq=1000)

def back(speed):
    pin1.duty(0)
    pin2.duty(speed)
    pin3.duty(0)
    pin4.duty(speed)
    pin5.duty(speed + a)
    pin6.duty(0)
    pin7.duty(speed)
    pin8.duty(0)
def forward(speed):
    pin1.duty(speed)
    pin2.duty(0)
    pin3.duty(speed)
    pin4.duty(0)
    pin5.duty(0)
    pin6.duty(speed + a)
    pin7.duty(0)
    pin8.duty(speed)
def pleft(speed):
    pin1.duty(speed)
    pin2.duty(0)
    pin3.duty(0)
    pin4.duty(speed)
    pin5.duty(speed + a)
    pin6.duty(0)
    pin7.duty(0)
    pin8.duty(speed)
def pright(speed):
    pin1.duty(0)
    pin2.duty(speed)
    pin3.duty(speed)
    pin4.duty(0)
    pin5.duty(0)
    pin6.duty(speed + a)
    pin7.duty(speed)
    pin8.duty(0)
def left(speed):
    pin1.duty(speed)
    pin2.duty(0)
    pin3.duty(0)
    pin4.duty(speed)
    pin5.duty(0)
    pin6.duty(speed + a)
    pin7.duty(speed)
    pin8.duty(0)
def right(speed):
    pin1.duty(0)
    pin2.duty(speed)
    pin3.duty(speed)
    pin4.duty(0)
    pin5.duty(speed + a)
    pin6.duty(0)
    pin7.duty(0)
    pin8.duty(speed)
def stop():
    pin1.duty(0)
    pin2.duty(0)
    pin3.duty(0)
    pin4.duty(0)
    pin5.duty(0)
    pin6.duty(0)
    pin7.duty(0)
    pin8.duty(0)

def qian(speed):
    pin1.duty(speed)
    pin2.duty(0)
    pin3.duty(speed)
    pin4.duty(0)
    pin5.duty(0)
    pin6.duty(speed + a)
    pin7.duty(0)
    pin8.duty(speed)
def zuoqian(speed):
    pin1.duty(speed)
    pin2.duty(0)
    pin3.duty(0)
    pin4.duty(0)
    pin5.duty(0)
    pin6.duty(0)
    pin7.duty(0)
    pin8.duty(speed)
def youqian(speed):
    pin1.duty(0)
    pin2.duty(0)
    pin3.duty(speed)
    pin4.duty(0)
    pin5.duty(0)
    pin6.duty(speed + a)
    pin7.duty(0)
    pin8.duty(0)
def zuohou(speed):
    pin1.duty(0)
    pin2.duty(0)
    pin3.duty(0)
    pin4.duty(speed)
    pin5.duty(speed + a)
    pin6.duty(0)
    pin7.duty(0)
    pin8.duty(0)
def youhou(speed):
    pin1.duty(0)
    pin2.duty(speed)
    pin3.duty(0)
    pin4.duty(0)
    pin5.duty(0)
    pin6.duty(0)
    pin7.duty(speed)
    pin8.duty(0)



