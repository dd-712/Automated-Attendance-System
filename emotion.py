import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from deepface import DeepFace

class emotionIdentify:
    
    def __init__(self) -> None:
        pass

    def identifyEmotion(self):
        faceCascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")
        video = cv2.VideoCapture(0)
        emot={}
        emot['not'] = 0
        emot['yes'] = 0

        while True:
            _, frame = video.read()
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray_img, 1.3, 5)

            try:
                res = DeepFace.analyze(img_path = frame, actions = ["emotion"])['emotion']
            
                emotion = max(zip(res.values(), res.keys()))[1]
                for (x,y,w,h) in faces:
                    cv2.putText(frame, emotion, (x+5,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 200), 4)
                
                if emotion in ['happy', 'neutral', 'surprise']:
                    emot['yes'] += 1
                else:
                    emot['not'] += 1
            except Exception:
                print("Face Not Visible")
                emot['not'] += 1

            cv2.imshow("Capturing", frame)
            key=cv2.waitKey(1)
            if key == ord('q'):
                    break
        video.release()
        cv2.destroyAllWindows()

        return emot

 