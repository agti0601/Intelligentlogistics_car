import cv2
from pyzbar.pyzbar import decode

# 读取图像
image = cv2.imread("qrcode_image.png")  # 替换为你的图像路径

# 将图像转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 解码二维码
qrcodes = decode(gray)

# 遍历解码结果
for qrcode in qrcodes:
    data = qrcode.data.decode("utf-8")
    print("QR Code Data:", data)

    # 提取二维码边界框的顶点坐标
    points = qrcode.polygon
    if len(points) >= 4:
        for j in range(4):
            cv2.line(image, points[j], points[(j + 1) % 4], (0, 255, 0), 3)

cv2.imshow("QR Code Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
