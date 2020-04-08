import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)
canny = cv2.Canny(image, 30, 150) # blur 이미지(single channel), 임계값1, 임계값2
# 변화값이 임계값1보다 작은 것은 edge X, 변화값이 임계값2보다 큰 값은 edge, 임계값 사이의 값들은
cv2.imshow("Canny", canny)
cv2.waitKey(0)