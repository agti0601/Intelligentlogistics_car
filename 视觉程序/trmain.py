import cv2
from pyzbar.pyzbar import decode
import numpy as np
wide = 640
high = 480

def decode_qr_code(frame):
    decoded_objects = decode(frame)

    # 提取二维码信息
    qr_code_data = None
    if decoded_objects:
        qr_code_data = decoded_objects[0].data.decode('utf-8')

    return qr_code_data

def detect_circle(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用Hough变换检测圆
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=20,
        param1=50,
        param2=30,
        minRadius=0,
        maxRadius=0
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        return circles[0]
    return None
def detect_largest_circle(frame):
    cwide = wide / 2
    chigh = high / 2
    # 将图像从BGR颜色空间转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用Hough圆变换检测圆
    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=5, maxRadius=50
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))

        # 找到最大半径的圆
        largest_circle = max(circles[0, :], key=lambda x: x[2])

        # 提取最大圆的圆心坐标
        center = (largest_circle[0], largest_circle[1])



        # 在图像上绘制最大圆
        cv2.circle(frame, center, largest_circle[2], (0, 255, 0), 2)
        # 在图像上绘制最大圆的中心点
        cv2.circle(frame, center, 2, (0, 0, 255), 3)
        cv2.circle(frame, (340, 240), 12, (255, 0, 0), -1)
        cv2.line(frame, center, (340, 240), (255, 0, 0), 2)
        return center

    return None
def detect_color(frame, circles):
    if circles is not None:
        for circle in circles:
            center_x, center_y, _ = circle
            color = frame[center_y, center_x]

            # 根据颜色值判断颜色
            if color[2] > 200:  # 红色
                print("红色")
            elif color[0] > 200:  # 蓝色
                print("蓝色")
            elif color[1] > 200:  # 绿色
                print("绿色")

def detect_most_common_color(frame):
    # 将图像从BGR颜色空间转换为HSV颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义红色、绿色和蓝色的HSV范围
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    # 创建掩码，根据颜色范围将图像分割为红色、绿色和蓝色部分
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # 计算每种颜色的像素数量
    red_pixel_count = np.sum(mask_red == 255)
    green_pixel_count = np.sum(mask_green == 255)
    blue_pixel_count = np.sum(mask_blue == 255)

    color_counts = {
        'Red': red_pixel_count,
        'Green': green_pixel_count,
        'Blue': blue_pixel_count
    }

    most_common_color = max(color_counts, key=color_counts.get)

    return most_common_color

if __name__ == "__main__":
    cap = cv2.VideoCapture(1)  # 打开默认摄像头

    # 依次执行任务
    step = 2
    while True:
        ret, frame = cap.read()  # 读取视频帧
        if not ret:
            break

        if step == 1:
            # 识别二维码
            qr_code_data = decode_qr_code(frame)
            if qr_code_data:
                print("识别的二维码信息:", qr_code_data)
                ndata = qr_code_data.split('+')
                print(ndata[0][1], ndata[1][1])
                step = 2  # 转到下一步
        elif step == 2:
            # 检测圆
            # circles = detect_circle(frame)
            circles = detect_largest_circle(frame)
            if circles is not None:
                print("检测到圆心:", circles)




                # step =   # 转到下一步
        elif step == 3:
            # 识别颜色
            # detect_color(frame, circles)
            print(detect_most_common_color(frame))

        # 显示帧
        cv2.imshow("QR Code, Circle, and Color Detection", frame)

        # 按下 'q' 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头和关闭窗口
    cap.release()
    cv2.destroyAllWindows()
