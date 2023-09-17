import serial #导入模块

try:
    # 端口号，根据自己实际情况输入，可以在设备管理器查看
    port = "COM6"
    # 串口波特率，根据自己实际情况输入
    bps = 9600
    # 超时时间,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    time = 5
    # 打开串口，并返回串口对象
    uart = serial.Serial(port, bps, timeout = time)

    # 串口发送一个字符串
    len = uart.write("hello world".encode('utf-8'))
    print("send len: ", len)

    # 串口接收一个字符串
    str = ''
    for i in range(len):
        str += uart.read().decode("utf-8")
    print("receive data: ", str)

    # 关闭串口
    uart.close()

except Exception as result:
    print("******error******：", result)
