from machine import Pin, SoftI2C
from time import sleep
import ssd1306


# 创建i2c对象
i2c = SoftI2C(scl=Pin(35), sda=Pin(36))

# 宽度高度
oled_width = 128
oled_height = 64

# 创建oled屏幕对象
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# 在指定位置处显示文字
def ol(str):
    oled.text(str, 20, 30)
    oled.show()
    
ol("oled OK")
