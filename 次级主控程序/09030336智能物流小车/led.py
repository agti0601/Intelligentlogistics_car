import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(48), 8)
# np[0] = (255, 0, 0) # set to red, full brightness
# np[1] = (0, 128, 0) # set to green, half brightness
# np[2] = (0, 0, 64)  # set to blue, quarter brightness

def red():
    np[0] = (255, 0, 0)
    np.write()
def green():
    np[0] = (0, 128, 0)
    np.write()
       
def blue():
    np[0] = (0, 0, 64)
    np.write() 
def ledoff():
    np[0] = (0, 0, 0)
    np.write()
green()