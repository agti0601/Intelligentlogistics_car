import cv2
import numpy as np

wide = 640
high = 480
def video():
    # view = "http://192.168.1.111:8080/?action=stream"
    view = 1
    # cap = cv2.VideoCapture(1)
    vc = cv2.VideoCapture(view)
    vc.set(3, wide)  # 设置宽度为640
    vc.set(4, high)  # 设置高度为480
    while True:
        reg, img = vc.read()
        # img = np.rot90(img, 2)  #旋转图像
        x_center = int(wide/2)
        y_center = int(high/2)
        cv2.waitKey(1)
        cv2.circle(img, (x_center, y_center), 5, (0, 0, 255), -1)
        # cv2.circle(img, (320, 240), 5, (0, 0, 255), -1)
        # cv2.putText(img, qr_data, (x_center, y_center + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow("image", img)

    vc.release()
    cv2.destroyAllWindows()
    return img

if __name__ == '__main__':
    video()

