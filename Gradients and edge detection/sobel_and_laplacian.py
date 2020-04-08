import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
lap = cv2.Laplacian(image, cv2.CV_64F)
# 이미지(single channel), 출력 이미지의 데이터 타입(여기서는 64bit float)
lap = np.uint8(np.abs(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0) # vertical
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1) # horizontal
sobelX = np.uint8(np.abs(sobelX))
sobelY = np.uint8(np.abs(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)