# # # This file is executed on every boot (including wake-boot from deepsleep)
# # #import esp
# # #esp.osdebug(None)
# # #import webrepl
# # #webrepl.start()
# import led
# import psmain
# import machine
# watchdog = machine.WDT(timeout=300000)  # 设置超时时间为5000毫秒（5秒
# led.ledoff()