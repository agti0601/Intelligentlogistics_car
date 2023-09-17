import machine
import time

# 配置串口
uart = machine.UART(1, tx=17, rx=16, baudrate=9600)

# 循环发送数据
while True:
    uart.write('1')
    time.sleep(1)
