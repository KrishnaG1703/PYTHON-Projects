import time
import cv2
import mediapipe as mp
import HandTrackingMod as htm

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.HandTrack()
while True:
    success, imp = cap.read()
    img = detector.FindHand(imp)
    lmList = detector.Position(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(imp, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow('Image', img)
    cv2.waitKey(1)