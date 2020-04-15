from pyimagesearch.facedetector import FaceDetector
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="path to where the face cascade resides")
ap.add_argument("-i", "--image", required=True, help="path to where the image file resides")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fd = FaceDetector(args["face"])
faceRects = fd.detect(gray, scaleFactor=1.3, minNeighbors=3, minSize=(10, 10))
# 이미지, 스캐일팩터(이미지의 크기가 스캐일에 의해 얼마나 줄어드는가), 이미지에서 얼굴로 분류되기 위한 직사각형의 수, 최소 픽셀 수
# scaleFactor와 이미지의 크기는 반비례
# minNeighbors가 커지면 얼굴을 덜 찾지만 퀄리티는 올라감
# (30, 30)부터 시작해서 조율하는 것이 좋음
print("I found %d face(s)" %len(faceRects))
for (x, y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Faces", image)
cv2.waitKey(0)