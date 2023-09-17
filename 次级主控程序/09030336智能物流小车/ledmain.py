from ps2 import PS2Controller
import pcatext as pca
import dianji as dj
import math
import time
from machine import SoftI2C,Pin,PWM
import led
import _thread
ps2ctl = PS2Controller(di_pin_no=11, do_pin_no=12, cs_pin_no=13, clk_pin_no=14)
ps2ctl.init()
i = 2
a = 90
b = 90
c = 90
d = 90
e = 90
f = 90
g = 90
h = 90
i = 90
j = 90
k = 90
l = 90
ag = 10 #每次变化的角度


speed = 1000
pin1=PWM(Pin(4),freq=1000)  #左前 红1
pin2=PWM(Pin(5),freq=1000)
pin3=PWM(Pin(6),freq=1000)  #左后 红3
pin4=PWM(Pin(7),freq=1000)
pin5=PWM(Pin(15),freq=1000)  #右前 黑5
pin6=PWM(Pin(16),freq=1000)
pin7=PWM(Pin(17),freq=1000)  #左前 红1
pin8=PWM(Pin(18),freq=1000)

led.ledoff()
for a in range(0,2):
    time.sleep_ms(1000)
    led.blue()
    time.sleep_ms(1000)
    led.green()
def zhuanhuan(x):
    y = 90/128*x + 90
    return y

def luntai(x):
    y = 1000/128*x
    return y

pca.biaoding()
dj.stop()
    
while i > 1:
    led.green()
    key_car= ps2ctl.read_once()   # 收到的字符格式为 keys:UP,RIGHT: pos(lx,ly):0,-1: pos(rx,ry): 0,-1:
    #print("检测到按键：",key_car)    
    key_list= key_car.split(':')  # 用：来将字符串进行分割，写入数组key_list中  key_list[1]输入的按键、key_list[3]左摇杆坐标、key_list[5]右摇杆坐标
    l= key_list[3].split(',')
    r= key_list[5].split(',')
    lx = int(l[0])
    ly = -int(l[1])-1
    rx = int(r[0])
    ry = -int(r[1])-1
    time.sleep(0.2)

    print("测试", key_list[1])
    print("测试(lx)", lx)
    print("测试(ly)", ly)
    print("测试(rx)", rx)
    print("测试(ry)", ry)
    if key_list[1]=="无":
        
        dj.stop()
        time.sleep(0.1)
       

    if key_list[1]=="UP":
        
#       print(kedky_car," 前进")
        dj.forward()
        time.sleep(0.1)

      
      
    if key_list[1]=="DOWN":
        dj.back()
        time.sleep(0.1)
      
    if key_list[1]=="LEFT": 
        dj.left()
        time.sleep(0.1)
      
    if key_list[1]=="RIGHT": 
        dj.right()
        time.sleep(0.1)
      
    if key_list[1]=="SQUARE": 
        dj.pleft()
        time.sleep(0.1)

    if key_list[1]=="CIRCLE": 
        dj.pright()
        time.sleep(0.1)
    if key_list[1]=="TRIANGLE":
        pca.pchushi()
        time.sleep(0.1)
    if key_list[1]=="CROSS": 
        pca.pfangzhi()
        time.sleep(0.1)
    if key_list[1]=="L1": 
        e += ag
        pca.servo.position(5,e)
        time.sleep(0.1)
    if key_list[1]=="L2": 
        e -= ag
        pca.servo.position(5,e)
        time.sleep(0.1)
    if key_list[1]=="R1": 
        f += ag
        pca.servo.position(4,f)
        time.sleep(0.1)
    if key_list[1]=="R2": 
        led.blue()
        time.sleep(0.1)
    if key_list[1]=="L3":    
        pca.servo.position(1,g)
        time.sleep(0.1)
    if key_list[1]=="R3": 
        g -= ag     
        pca.servo.position(1,g)
        time.sleep(0.1)
        
    if ly > 10 and lx==0: 
        dj.forward()
        time.sleep(0.1)
    if ly < -10 and lx==0: 
        dj.back()
        time.sleep(0.1)
    if ly > 10 and lx>0: 
        dj.youhou()
        time.sleep(0.1)
    if ly > 10 and lx<0: 
        dj.youqian()
        time.sleep(0.1)
    if ly < -10 and lx<0: 
        dj.zuoqian()
        time.sleep(0.1)
    if ly < -10 and lx>0: 
        dj.zuohou()
        time.sleep(0.1)
