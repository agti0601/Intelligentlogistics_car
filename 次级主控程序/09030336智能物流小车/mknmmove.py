import machine
from TB6612Motor import *
import time
class MOVE:
    def __init__(self, pwm_pins, pin1s, pin2s):
        self.motors = []
        for pwm_pin, pin1, pin2 in zip(pwm_pins, pin1s, pin2s):
            motor = TB6612Motor(pwm_pin, pin1, pin2)
            self.motors.append(motor)

    def move(self, vx, vy, omega):
        speeds = [
            vx - vy - omega,
            vx + vy + omega,
            vx + vy - omega,
            vx - vy + omega
        ]

        max_speed = max(map(abs, speeds))
        if max_speed > 1023:
            factor = 1023 / max_speed
            speeds = [int(speed * factor) for speed in speeds]

        for i, speed in enumerate(speeds):
            self.motors[i].forward(speed) if speed > 0 else self.motors[i].backward(-speed)

    def stop(self):
        for motor in self.motors:
            motor.stop()

    def close(self):
        for motor in self.motors:
            motor.close()

# 配置引脚
pwm_pins = [16, 9, 46, 14]  # 更换为实际的PWM引脚
pin1s = [15, 10, 8, 12]   # 更换为实际的引脚号
pin2s = [7, 11, 3, 13]  # 更换为实际的引脚号

# 创建一个麦克纳姆轮小车对象
car = MOVE(pwm_pins, pin1s, pin2s)

# 前进
car.move(vx=0, vy=0, omega=0)

# 等待一段时间
time.sleep(0.5)  # 延时2秒
print("move.py OK")
# 停止
car.stop()
# 
# # 关闭小车对象
# car.close()
def test():
    while 1:
        x = int(input("x"))
        y = int(input("y"))
    #     z = int(input("z"))
        z = 0
        t = int(input("t"))
        car.move(vx=x, vy=y, omega=z)
        time.sleep(t)
        car.stop()
def zhiling(x,y,z,t):
        car.move(vx=x, vy=y, omega=z)
        time.sleep(t)
        car.stop()
def zhuanpanwei():
    zhiling(0,-300,0,2)
    zhiling(500,0,0,6)
    
def chushi():
    zhiling(0,-600,0,1)
    time.sleep(1.2)
    zhiling(465,0,0,6)
    time.sleep(1.2)
    zhiling(465,0,0,2)
    zhiling(0,-580,0,4)
    
def chushi1():
    zhiling(0,-600,0,1)
    time.sleep(1.2)
    zhiling(465,0,0,6)
    time.sleep(1.2)
    zhiling(465,0,0,2)
    zhiling(0,-580,0,4)
    zhiling(0,-550,10,3)
    zhiling(0,0,480,1)
    zhiling(0,-494,20,4)
    
    
   #hui 
    zhiling(0,494,-17,4)
    
   #hui 
    zhiling(0,-500,10,7)