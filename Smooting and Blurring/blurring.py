import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
blurred = np.hstack([cv2.blur(image, (3,3)), cv2.blur(image, (5,5)), cv2.blur(image, (7,7))])
# 3x3, 5x5, 7x7 kernel, 커널의 크기가 커질수록 이미지가 더 blur됨 (커널내의 평균값으로 픽셀들을 대체)
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)
blurred = np.hstack([cv2.GaussianBlur(image, (3,3), 0), cv2.GaussianBlur(image, (5,5), 0), cv2.GaussianBlur(image, (7,7), 0)])
# 마지막인자는 시그마 x값으로 0으로하면 자동적으로 계산됨
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)
blurred = np.hstack([cv2.medianBlur(image, 3), cv2.medianBlur(image, 5), cv2.medianBlur(image, 7)])
# 인자는 이미지와 커널의 크기, 커널내의 중앙값으로 픽셀들을 대체(잡음 제거에 효과적)
cv2.imshow("Median", blurred)
cv2.waitKey(0)
blurred = np.hstack([cv2.bilateralFilter(image, 5, 21, 21), cv2.bilateralFilter(image, 7, 31, 31), cv2.bilateralFilter(image, 9, 41, 41)])
# 다른 blur와 달리 노이즈를 제거하면서 경계도 유지가능
# 3번째인자는 색공간 표준편차로 값이 커지면 블러를 계산하는데 주변의 더 많은 색들이 고려됨
# 4번째인자는 거리공간 표준편차로 값이 커지면 가운데 픽셀로부터 멀리 떨어진 픽셀들의 색이 충분히 유사하다면 블러를 계산하는데 영향을 미친다.
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)