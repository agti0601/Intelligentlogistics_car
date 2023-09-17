import cv2
import numpy as np

# 初始化全局变量
prev_radius = None
prev_center = None


def detect_circles():
    global prev_radius, prev_center

    # 初始化电脑摄像头
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)  # 设置摄像头宽度
    camera.set(4, 480)  # 设置摄像头高度

    while True:
        # 读取图像帧
        ret, frame = camera.read()
        if not ret:
            break

        # 图像预处理
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.Canny(gray, 50, 150)

        # 圆形检测
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=10,
                                   maxRadius=100)

        # 绘制检测到的圆形和圆心
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")

            # 计算移动平均半径和圆心位置
            if prev_radius is None and prev_center is None:
                prev_radius = circles[0][2]
                prev_center = (circles[0][0], circles[0][1])

            else:
                current_radius = circles[0][2]
                current_center = (circles[0][0], circles[0][1])
                alpha = 0.8  # 移动平均系数

                smoothed_radius = alpha * current_radius + (1 - alpha) * prev_radius
                smoothed_center = (
                    int(alpha * current_center[0] + (1 - alpha) * prev_center[0]),
                    int(alpha * current_center[1] + (1 - alpha) * prev_center[1])
                )

                prev_radius = smoothed_radius
                prev_center = smoothed_center
                print(prev_radius)
                # 绘制圆形
                cv2.circle(frame, smoothed_center, int(smoothed_radius), (0, 255, 0), 4)
                cv2.circle(frame, smoothed_center, 2, (0, 0, 255), 3)
                # print(smoothed_center)
        cv2.circle(frame, (320, 240), 15, (0, 0, 255), -1)
        # 显示图像
        cv2.imshow("Circles Detection", frame)
        key = cv2.waitKey(1) & 0xFF

        # 按下 'q' 键退出循环
        if key == ord("q"):
            break

    # 释放资源
    camera.release()
    cv2.destroyAllWindows()


# 执行圆形检测
detect_circles()