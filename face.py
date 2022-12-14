import glob
import os
import cv2
import face_recognition
import numpy as np
import matplotlib.pyplot as plt

known_face_encodings = []
known_face_names = []
frame_resizing = 1

class faceRecognize:

    def __init__(self):
        images_path = glob.glob(os.path.join("./images/", "*.*"))
        for img_path in images_path:
            img = cv2.imread(img_path)
            # rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(img)[0]

            # Store file name and file encoding
            known_face_encodings.append(img_encoding)
            known_face_names.append(filename)

        print("Encoding images loaded")

    def detect_known_faces(self,frame):
        small_frame = cv2.resize(frame, (0, 0), fx=frame_resizing, fy=frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)

        face_locations = np.array(face_locations)
        face_locations = face_locations / frame_resizing
        return face_locations.astype(int), face_names

    def recognize(self):
        cap = cv2.VideoCapture(0)
        times = 10
        person = {}

        while times>0:
            times -= 1
            ret, frame = cap.read()
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            face_locations, face_names = self.detect_known_faces(gray_img)
            for face_loc, name in zip(face_locations, face_names):
                y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.putText(frame, name, (x1+5, y1-5), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                
                if name in person:
                    person[name] += 1
                else:
                    person[name] = 1

            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

        Keymax = max(zip(person.values(), person.keys()))[1]
        return Keymax