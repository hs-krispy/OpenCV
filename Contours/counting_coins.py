import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Image", image)
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)
(contour, cnts, heirachy) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 이진화 이미지, 컨투어를 찾는 방법(컨투어 라인 중 가장 바깥쪽 라인만), 근사화 방법(컨투어 라인을 그릴 수 있는 포인트만 반환)
# return값은 컨투어 자체, 컨투어를 구성하는 점들로 이루어진 배열의 리스트, 상하구조
print("I count %d coins in this image" % len(cnts)) # 컨투어의 갯수
coins = image.copy() # 원본 이미지를 또 사용할 수 있으므로 copy()로 사용하는 것이 좋음
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
# 컨투어를 그리고자하는 이미지, 컨투어 리스트, 컨투어 리스트의 인덱스 번호(-1이면 모든 컨투어를 의미)
cv2.imshow("Coins", coins)
cv2.waitKey(0)
for (i, c) in enumerate(cnts): # enumerate 인덱스 번호와 리스트의 원소를 tuple형태로 반환
    (x, y, w, h) = cv2.boundingRect(c) # 컨투어를 인자로 받고 컨투어를 감싸는 직사각형의 시작 x, y 그리고 너비와 높이 반환
    print("Coin #%d" %(i+1))
    coin = image[y:y + h, x:x + w]
    cv2.imshow("Coin", coin)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c) # 컨투어를 인자를 받고 컨투어를 감싸는 원의 중심 x, y 그리고 반지름 반환
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w] # 마스크의 크기도 이미지의 크기와 동일하게 해줌
cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))
cv2.waitKey(0)