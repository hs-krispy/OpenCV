import numpy as np
import argparse
import time
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="Path to the (optional) video file")
args = vars(ap.parse_args())
blueLower = np.array([100, 67, 0], dtype="uint8") # B - 100, G - 67, R - 0
blueUpper = np.array([255, 128, 50], dtype="uint8")
camera = cv2.VideoCapture(args["video"])
while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break
    blue = cv2.inRange(frame, blueLower, blueUpper) # 이미지, lower threshold, upper threshold
    # 범위 사이에 위치하는 픽셀들은 흰색으로 나머지는 검정색으로
    blue = cv2.GaussianBlur(blue, (3, 3), 0)
    (contour, cnts, heirachy) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        # 컨투어 리스트, 컨투어 영역의 크기를 계산, 가장 큰 것이 앞으로 오도록
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        # minAreaRect로 컨투어를 둘러싸는 가장 작은 박스의 크기를 계산(물체의 회전을 고려한 사각형)
        # cv.BoxPoints로 구한 결과에 맞춰서 다시 박스를 구성하는 리스트를 만듬
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", blue)
    time.sleep(0.025)
    if cv2.waitKey(1) &  0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()