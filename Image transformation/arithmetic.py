import numpy as np
import argparse
import imutils
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
print("max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: " + str(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around: " + str(np.uint8([200])+np.uint8([100])))# 255보다 커지면 0부터 카운트
print("wrap around: " + str(np.uint8([50])-np.uint8([100])))# 0보다 작아지면 255부터 역으로 카운트
M = np.ones(image.shape, dtype="uint8")*100#이미지 픽셀만큼 공간에 값을 100으로
added = cv2.add(image, M)# 이미지의 모든 픽셀에 100을 더해서 255에 가까워지도록(밝아지게)
cv2.imshow("Added", added)
M = np.ones(image.shape, dtype="uint8")*50
subtracted = cv2.subtract(image, M)# 이미지의 모든 픽셀에 50을 빼서 0에 가까워지도록(어두워지게)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)