import machine
import time
import oled
# “1”为红色，“2”为绿色，“3”为蓝色
# 配置串口
uart = machine.UART(1, tx=21, rx=37, baudrate=115200)

# 循环发送和接收数据
def send(num):
    uart.write('$DGS:%d!'%num)
    time.sleep(2.3)
send(17)
# send(3 ,1)
# print("ok")
def receive():
    if uart.any():
        data = uart.read()
        print("Received:", data)
#      
# def houzhongfang():
#     send(1)
#     send(3)
#     send(4)
#     send(6)
#     send(5)
# 
# def guiwei():
#     send(14)
#     send(1)
# 
# def houzuofang():
#     send(1)
#     send(10)
#     send(11)
#     send(6)
#     send(5)
#     
# def houyoufang():
#     send(1)
#     send(8)
#     send(9)
#     send(6)
#     send(5)
def panyubei():
    send(1)
def panfang():
    send(2)
    
    
def qianfang():
    send(14)
def zuozhua():
    send(2)
#     time.sleep(0.1)
    send(3)
    
    send(4)
    
    send(5)
    
    send(1)
    
    



def zhongzhua():
    send(2)

    send(3)
    
    send(12)
    
    send(13)
    
    send(1)
    
def youzhua():
    send(2)

    send(3)
    
    send(7)
    
    send(8)
    
    send(1)
    
    
def qianzuozhua():
    send(14)

    send(15)
    
    send(4)
    
    send(5)
    
    send(14)
    
def qianzhongzhua():
    send(14)

    send(15)
    
    send(12)
    
    send(13)
    
    send(14)
def qianyouzhua():
    send(14)

    send(15)
    
    send(7)
    
    send(8)
    
    send(14)

def qianzuofang():
    send(5)
    
    send(4)
    
    send(15)
    
    send(14)
def qianzhongfang():
    
    send(13)
    
    send(12)
    
    send(15)
    
    send(14)
def qianyoufang():
    send(8)
    
    send(7)
    
    send(15)
    
    send(14)
    
def qianyubei():
    send(14)
def chushi():
    send(17)
oled.ol('duoji OK')
