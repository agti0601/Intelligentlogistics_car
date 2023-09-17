import machine

class TB6612Motor:
    def __init__(self, pwm_pin, pin1, pin2):
        self.motor_pwm = machine.PWM(machine.Pin(pwm_pin, machine.Pin.OUT))
        self.motor_pwm.freq(1000)
        
        self.motor_pin1 = machine.Pin(pin1, machine.Pin.OUT)
        self.motor_pin2 = machine.Pin(pin2, machine.Pin.OUT)

    def forward(self, speed):
        self.motor_pin1.on()
        self.motor_pin2.off()
        self.motor_pwm.duty(speed)

    def backward(self, speed):
        self.motor_pin1.off()
        self.motor_pin2.on()
        self.motor_pwm.duty(speed)

    def stop(self):
        self.motor_pin1.off()
        self.motor_pin2.off()
        self.motor_pwm.duty(0)

    def close(self):
        self.motor_pwm.deinit()
        self.motor_pin1.deinit()
        self.motor_pin2.deinit()

# # 创建一个TB6612电机对象
# motor = TB6612Motor(pwm_pin=5, pin1=4, pin2=0)
# 
# # 控制电机前进
# motor.forward(speed=512)  # 设置速度为512
# 
# # 等待一段时间
# machine.delay(2000)  # 延时2秒
# 
# # 控制电机后退
# motor.backward(speed=512)  # 设置速度为512
# 
# # 等待一段时间
# machine.delay(2000)  # 延时2秒
# 
# # 停止电机
# motor.stop()
# 
# # 关闭电机对象
# motor.close()
