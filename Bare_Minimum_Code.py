import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)  #Use 0 for laptops inbuit webcam

mpHands = mp.solutions.hands
hands = mpHands.Hands() #using defaults
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #if not work chnage top COLOR_BGR2RGB
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id == 0:
                    cv2.circle(img,(cx,cy),15,(225,0,225),cv2.FILLED)
                    
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
            
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3, (255,0,225), 3)   
  
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
