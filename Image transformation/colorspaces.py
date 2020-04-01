import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow('Original', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 색조(색의 종류), 채도(0이면 무채색, 255이면 가장 선명한 색), 명도(작을수록 어둡고 클수록 밝은 색)
cv2.imshow("HSV", hsv)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# 밝기, a 빨강~초록 색영역(음수이면 초록에 치우침, 양수면 빨강/보라 쪽으로 치우침), 노랑,파랑 색영역(음수이면 파랑 양수이면 노랑)
cv2.imshow("L*a*b", lab)
cv2.waitKey(0)