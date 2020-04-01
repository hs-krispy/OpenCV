import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
# split으로 분리해서 채널이 하나만 존재하기 때문에 흑백으로 보임(해당 채널의 색과 가까운 색이 밝게보임)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))# zero, zero, R을 병합, 해당 채널의 색만 강조되어서 보임
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)