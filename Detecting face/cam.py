from pyimagesearch.facedetector import FaceDetector
import imutils
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="path to where the face cascade resides")
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())
fd = FaceDetector(args["face"])
if not args.get("video", False): # 비디오 경로, 디폴트 (비디오 인자에 아무것도 입력하지않으면 False)
    camera = cv2.VideoCapture(0) # 입력 디바이스에 따라 실시간 촬영 frame을 받아옴(0 - webcam)
else:
    camera = cv2.VideoCapture(args["video"]) # 동영상 파일명이나 이미지 파일명을 넣으면 저장된 비디오를 불러옴
while True:
    (grabbed, frame) = camera.read() # 프레임을 읽어오는 것이 성공적인지에대한 boolean값, 프레임 자체
    if args.get("video") and not grabbed:
        break
    frame = imutils.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    frameClone = frame.copy()
    for (fX, fY, fW, fH) in faceRects:
        cv2.rectangle(frameClone, (fX, fY), (fX+fW, fY+fH), (0, 255, 0), 2)
    cv2.imshow("Face", frameClone)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()# 비디오 파일이나 영상 장치를 닫음
cv2.destroyAllWindows()
