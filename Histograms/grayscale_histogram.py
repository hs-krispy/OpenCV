from matplotlib import pyplot as plt
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# 입력 이미지의 배열, 히스토그램을 얻을 채널 인덱스, mask값, x축 요소의 개수(bins), y축 요소값의 범위(대부분 [0,256])
# 반환값은 256개의 요소를 갖는 배열
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])# x축의 범위 지정
plt.show()
cv2.waitKey(0)
