import numpy as np
import argparse
import imutils
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
flipped = cv2.flip(image, 1)# 좌우 반전
cv2.imshow("Flipped Horizontally", flipped)
flipped = cv2.flip(image, 0)# 상하 반전
cv2.imshow("Flipped Vertically", flipped)
flipped = cv2.flip(image, -1)# 상하좌우 반전
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)