import cv2
import mediapipe as mp
import time


class HandTrack():
    def __init__(self, mode=False, max_hand=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hand = max_hand
        self.track_con = track_con
        self.detection_con = detection_con
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.max_hand, self.detection_con, self.track_con)
        self.mpDraw = mp.solutions.drawing_utils

    def FindHand(self, imp, draw=True):
            imgRGB = cv2.cvtColor(imp, cv2.COLOR_BGR2RGB)
            self.results = self.hands.process(imgRGB)
            # print(results.multi_hand_landmarks)
            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    if draw:
                        self.mpDraw.draw_landmarks(imp, handLms, self.mpHands.HAND_CONNECTIONS)
            return imp
    def Position(self, imp, handno=0, draw=True):
        lmList =[]
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = self.imp.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(imp, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList




def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandTrack()
    while True:
        success, imp = cap.read()
        imp = detector.FindHand(imp)
        lmList = detector.Position(imp)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(imp, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow('Image', imp)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()