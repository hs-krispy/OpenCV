import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)# equalizeHist에는 grayscale이미지가 들어감
eq = cv2.equalizeHist(image)# 히스토그램 평활화(이미지의 대비를 향상시킴)
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))# 배열 image 우측에 eq를 이어 붙힘
cv2.waitKey(0)