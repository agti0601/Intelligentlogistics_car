import machine
import time

class bmdj:
    def __init__(self, pwm_pin, pin1, pin2, encoder_a_pin, encoder_b_pin):
        self.motor_pwm = machine.PWM(machine.Pin(pwm_pin, machine.Pin.OUT))
        self.motor_pwm.freq(1000)
        
        self.motor_pin1 = machine.Pin(pin1, machine.Pin.OUT)
        self.motor_pin2 = machine.Pin(pin2, machine.Pin.OUT)
        
        self.encoder_a_pin = machine.Pin(encoder_a_pin, machine.Pin.IN)
        self.encoder_b_pin = machine.Pin(encoder_b_pin, machine.Pin.IN)
        
        self.encoder_count = 0
        self.encoder_a_last_state = self.encoder_a_pin.value()

        self.encoder_a_pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=self.encoder_interrupt)

    def encoder_interrupt(self, pin):
        a_state = self.encoder_a_pin.value()
        if a_state != self.encoder_a_last_state:
            if self.encoder_b_pin.value() != a_state:
                self.encoder_count += 1
            else:
                self.encoder_count -= 1
        self.encoder_a_last_state = a_state

    def rotate(self, target_count, direction, speed):
        self.motor_pin1.value(direction)
        self.motor_pin2.value(not direction)
        self.motor_pwm.duty(speed)

        while abs(self.encoder_count) < target_count:
            pass

        self.motor_pin1.off()
        self.motor_pin2.off()
        self.motor_pwm.duty(0)

    def close(self):
        self.encoder_a_pin.irq(trigger=None)
        self.motor_pwm.deinit()
        self.motor_pin1.deinit()
        self.motor_pin2.deinit()

# 创建一个编码电机对象
motor = bmdj(pwm_pin=13, pin1=12, pin2=11)

# 控制电机旋转
motor.rotate(target_count=1000, direction=1, speed=1000)  # 旋转1000个计数，正转，速度为512

# 关闭电机对象
# motor.close()
