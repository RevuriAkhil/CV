import cv2
import face_recognition
import os
from datetime import datetime

known_faces_path = "/home/tach/Desktop/known_faces/vakhil"
unknown_faces_path = "/home/tach/Desktop/known_faces/unknown/"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
image_count = 5

def save_unknown_face(image):
    # Create a unique folder for the unknown face
    folder_name = str(len(os.listdir(unknown_faces_path)) + 1)
    folder_path = os.path.join(unknown_faces_path, folder_name)
    os.makedirs(folder_path)

    # Save multiple images of the unknown face
    for i in range(1, image_count + 1):
        img_name = f"{folder_name}_{i}.jpg"
        img_path = os.path.join(folder_path, img_name)
        cv2.imwrite(img_path, image)

def recognize_faces():
    # Load known faces and encodings
    known_faces = []
    known_encodings = []

    for name in os.listdir(known_faces_path):
        image_path = os.path.join(known_faces_path, name)
        img = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(img)[0]
        known_faces.append(img)
        known_encodings.append(encoding)

    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()  # Read the video capture

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Detect faces and recognize
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            face_encoding = face_recognition.face_encodings(face_img)

            if len(face_encoding) > 0:
                face_encoding = face_encoding[0]

                # Compare face encoding with known encodings
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    matched_index = matches.index(True)
                    name = os.listdir(known_faces_path)[matched_index].split(".")[0]

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # Save unknown faces
                if name == "Unknown":
                    save_unknown_face(face_img)

        cv2.imshow("Video Feed", frame)

        if cv2.waitKey(1) == ord("q"):  # Break the loop on 'q' key press
            break

    cap.release()
    cv2.destroyAllWindows()

recognize_faces()
