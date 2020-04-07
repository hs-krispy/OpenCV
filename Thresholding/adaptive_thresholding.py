import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image",image)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
# 이미지(single channel), 임계값, 계산 방법, threshold type, thresholding을 적용할 영역 사이즈, C(평균이나 가중평균에서 차감할 값)
# 영역의 크기와 C가 가장 중요한 인자
# cv2.ADAPTIVE_THRESH_MEAN_C은 주변영역의 평균값으로 결정
cv2.imshow("Mean Thresh", thresh)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)