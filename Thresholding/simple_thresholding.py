import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY) # 이미지(single channel), 임계값, 임계값을 넘었을 때 적용할 value, threshloding type
# T에는 임계값이 들어감
cv2.imshow("Threshold Binary", thresh)
(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
