from ps2 import PS2Controller
import time
import math
from mknmmove import *
from a24duoji import *
ps2ctl = PS2Controller(di_pin_no=39, do_pin_no=40, cs_pin_no=41, clk_pin_no=42)
ps2ctl.init()
i = 2
speed = 500
#sck--clk_pin_no  cs--cs_pin_no    do_pin_no--MOSI   di_pin_no--MISO
def zhuanhuan(x):
    y = 90/128*x + 90
    return y
def luntai(x):
    y = 1000/128*x - 150
    return y

    
while i > 1:
    
    key_car= ps2ctl.read_once()   # 收到的字符格式为 keys:UP,RIGHT: pos(lx,ly):0,-1: pos(rx,ry): 0,-1:
    #print("检测到按键：",key_car)    
    key_list= key_car.split(':')  # 用：来将字符串进行分割，写入数组key_list中  key_list[1]输入的按键、key_list[3]左摇杆坐标、key_list[5]右摇杆坐标

    l= key_list[3].split(',')
    r= key_list[5].split(',')
    lx = int(l[0])
    ly = int(l[1])
    rx = int(r[0])
    ry = int(r[1])
    time.sleep(0.2)
#     if abs(lx) > 30 or abs(ly) > 30:
#         car.move(vx=int(luntai(ly)), vy=int(luntai(lx)), omega=0)
#     else:
#         car.stop()
    

    print("测试", key_list[1])
    print("测试(lx)", lx)
    print("测试(ly)", ly)
    print("测试(rx)", rx)
    print("测试(ry)", ry)
#     if key_list[1]=="无":
#         car.stop()
    if key_list[1]=="UP":
        qianzhongzhua()
      
    if key_list[1]=="DOWN":
        qianyubei()
      
    if key_list[1]=="LEFT": 
        qianzuozhua()
    if key_list[1]=="RIGHT": 
        qianyouzhua()
    if key_list[1]=="SQUARE":
        zuozhua()
    if key_list[1]=="CIRCLE":
        youzhua()

    if key_list[1]=="TRIANGLE":
        zhongzhua()
    
    if key_list[1]=="CROSS":
        panyubei()

    if key_list[1]=="L1":
        qianzhongfang()

    if key_list[1]=="L2":
        qianzuofang()
        
    if key_list[1]=="R1":
        chushi()

    if key_list[1]=="R2":
        qianyoufang()
  
    if key_list[1]=="L3":
        car.move(vx=0, vy=-speed, omega=speed)
    if key_list[1]=="R3":
        car.move(vx=0, vy=speed, omega=-speed)

