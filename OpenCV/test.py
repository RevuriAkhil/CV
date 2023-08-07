import cv2
import dlib
import os
import uuid

detector = dlib.get_frontal_face_detector()
new_path = '/home/tach/Desktop/unknown_extract/'

def MyRec(rgb, x, y, w, h, v=20, color=(200, 0, 0), thickness=2):
    """To draw stylish rectangle around the objects"""
    cv2.line(rgb, (x, y), (x + v, y), color, thickness)
    cv2.line(rgb, (x, y), (x, y + v), color, thickness)

    cv2.line(rgb, (x + w, y), (x + w - v, y), color, thickness)
    cv2.line(rgb, (x + w, y), (x + w, y + v), color, thickness)

    cv2.line(rgb, (x, y + h), (x, y + h - v), color, thickness)
    cv2.line(rgb, (x, y + h), (x + v, y + h), color, thickness)

    cv2.line(rgb, (x + w, y + h), (x + w, y + h - v), color, thickness)
    cv2.line(rgb, (x + w, y + h), (x + w - v, y + h), color, thickness)

def save(img, name, bbox, width=180, height=227):
    x, y, w, h = bbox
    imgCrop = img[y:h, x:w]
    imgCrop = cv2.resize(imgCrop, (width, height))
    cv2.imwrite(name + ".jpg", imgCrop)

def faces():
    cap = cv2.VideoCapture(0)  # Open the default camera (index 0)
    counter = 0

    while True:
        ret, frame = cap.read()  # Read the video capture

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        # Detect the faces
        for face in faces:
            x1, y1 = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            cv2.rectangle(frame, (x1, y1), (x2, y2), (220, 255, 220), 1)
            MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0, 250, 0), 3)
            unique_id = str(uuid.uuid4())  # Generate a unique ID for each photo
            save(gray, os.path.join(new_path, unique_id), (x1, y1, x2, y2))
            counter += 1

        frame = cv2.resize(frame, (800, 800))
        cv2.imshow('Video Feed', frame)

        if cv2.waitKey(1) == ord('q'):  # Break the loop on 'q' key press
            break

    cap.release()
    cv2.destroyAllWindows()

faces()
