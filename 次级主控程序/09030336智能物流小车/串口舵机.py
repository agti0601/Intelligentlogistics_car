from machine import Pin, UART
import time
#配置串口
# uart = UART(0, 9600, bits=8, parity=None, stop=1, tx=Pin(17), rx=Pin(18))
# uart = UART(1, 9600, bits=8, parity=None, stop=1, tx=Pin(17), rx=Pin(18))
uart = UART(1, tx=38, rx=39, baudrate=9600)
#串口控制舵机函数
def UARTServo(servonum, angle):
    servonum = 64 + servonum
#     date1 = int(angle/100 + 48)
#     date2 = int((angle%100)/10 + 48)
#     date3 = int(angle%10 + 48)
#     a = int(36.4*angle + 1638) 
#     cmd=bytearray([36,servonum,date1,date2,date3,35])

#     cmd=bytearray([36,servonum,a,a,a,35])
    uart.write(cmd)
    time.sleep(0.05)
# for i in range(0,8):
#     UARTServo(1,10)
#     time.sleep(2)
#     UARTServo(1,150)
#     time.sleep(2)
#     print(i)
while 1:
#     a = int(input("pin"))
    a =1
    b = int(input("degrees"))
    time.sleep_ms(1)
    UARTServo(a,b)
    time.sleep_ms(1)