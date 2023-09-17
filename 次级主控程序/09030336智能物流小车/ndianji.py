import machine
import time

# 配置引脚
motor1_pwm = machine.PWM(machine.Pin(13))  # 更换为您的引脚号
motor1_a = machine.Pin(12, machine.Pin.OUT)  # 更换为您的引脚号
motor1_b = machine.Pin(11, machine.Pin.OUT)  # 更换为您的引脚号

# 设置PWM频率
motor1_pwm.freq(1000)  # 设置PWM频率为1kHz

# 正转
motor1_a.on()
motor1_b.off()
motor1_pwm.duty(512)  # 设置占空比，控制速度
time.sleep_(2)

# 反转
motor1_a.off()
motor1_b.on()
motor1_pwm.duty(512)  # 设置占空比，控制速度

# 等待一段时间
time.sleep(2)

# 停止
motor1_a.off()
motor1_b.off()
motor1_pwm.duty(0)  # 设置占空比为0，停止电机
# 
# # 关闭PWM
# motor1_pwm.deinit()
