import pca9685
import math
import time
from machine import SoftI2C,Pin
i2c=SoftI2C(scl=Pin(39),sda=Pin(38))
a = 90
b = 90
c = 90
d = 90
e = 90

class Servos:
    def __init__(self, i2c, address=0x40, freq=50, min_us=600, max_us=2400,
                 degrees=180):
        self.period = 1000000 / freq
        self.min_duty = self._us2duty(min_us)
        self.max_duty = self._us2duty(max_us)
        self.degrees = degrees
        self.freq = freq
        self.pca9685 = pca9685.PCA9685(i2c, address)
        self.pca9685.freq(freq)

    def _us2duty(self, value):
        return int(4095 * value / self.period)

    def position(self, index, degrees=None, radians=None, us=None, duty=None):
        span = self.max_duty - self.min_duty
        if degrees is not None:
            duty = self.min_duty + span * degrees / self.degrees
        elif radians is not None:
            duty = self.min_duty + span * radians / math.radians(self.degrees)
        elif us is not None:
            duty = self._us2duty(us)
        elif duty is not None:
            pass
        else:
            return self.pca9685.duty(index)
        duty = min(self.max_duty, max(self.min_duty, int(duty)))
        self.pca9685.duty(index, duty)

    def release(self, index):
        self.pca9685.duty(index, 0)
def angle(pin, degree):
    servo.position(pin,degree)
def zhixing(pin,a,b,c):
    for i in range(a,b,c):
        servo.position(pin,degrees=i)  
        time.sleep_ms(3)
    

def biaoding():
    for i in range(0,18):
        servo.position(i,90)
        time.sleep_ms(1)
servo=Servos(i2c, address=0x40, freq=50, min_us=600, max_us=2400, degrees=180)
def test():
    while 1:
        a = int(input("串口"))
        b = int(input("角度"))
        servo.position(a,degrees=b)
        time.sleep_ms(1)
        
# for i in range(0,3):
#     for j in range(70,110):
#         servo.position(i,degrees=j)
#         time.sleep(1)


def chushi():
    servo.position(5,degrees=130)
    time.sleep_ms(500)
    servo.position(1,degrees=90)
    time.sleep_ms(500)
    servo.position(2,degrees=130)
    time.sleep_ms(500)
    servo.position(3,degrees=0)
    time.sleep_ms(500)
    servo.position(4,degrees=70)
    
    
 



def zhunbei():
    servo.position(1,degrees=45) 
    time.sleep(0.5)
    servo.position(2,degrees=90)
    time.sleep(0.5)
    servo.position(3,degrees=90)
    time.sleep(0.5)
    servo.position(4,degrees=35)
    time.sleep(0.5)
    servo.position(5,degrees=95)#min10 

def fangzhi():
    servo.position(5,degrees=60)
    time.sleep_ms(10)
    servo.position(1,degrees=125) 
    servo.position(3,degrees=150)
    servo.position(4,degrees=120)
    time.sleep_ms(10)
    servo.position(2,degrees=130)
    time.sleep_ms(10)
    servo.position(5,degrees=120)
    
def pchushi():
    zhixing(5,90,125,1)
    time.sleep_ms(10)
    zhixing(3,90,30,-1)
    zhixing(4,90,60,-1)
    time.sleep_ms(10)
#     zhixing(1,90,120,1)
    zhixing(2,90,0,-1)
   


def pfangzhi():
    zhixing(5,125,60,-1)
    time.sleep_ms(20)
    zhixing(1,90,80,-1)
    zhixing(3,30,100,1)
    zhixing(4,60,120,1)
    zhixing(2,0,140,1)
    time.sleep_ms(30)
    zhixing(5,60,125,1)

    
    #2 140    3 120
    
