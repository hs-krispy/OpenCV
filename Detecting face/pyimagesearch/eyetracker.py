import cv2

class EyeTracker:
    def __init__(self, faceCascadePath, eyeCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
        self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)
        # 얼굴인식과 눈을 인식하는 파일의 경로를 받아옴
    def track(self, image):
        faceRects = self.faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        # 시작 x, y와 width, height
        rects = []
        for(fX, fY, fW, fH) in faceRects:
            faceROI = image[fY: fY + fH, fX: fX + fW] # 얼굴부분만 슬라이싱한 이미지
            rects.append((fX, fY, fX + fW, fY + fH))
            eyeRects = self.eyeCascade.detectMultiScale(faceROI, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)

            for(eX, eY, eW, eH) in eyeRects:
                rects.append((fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))
                # 눈을 감싸는 사각형
        return rects