import cv2
import os

from ultralytics import YOLO

def play_local_video(video_path):
    # Create a VideoCapture object to open the video
    cap = cv2.VideoCapture(0)
    
    ret, frame = cap.read()
    H,W, _ = frame.shape
    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    model_path = os.path.join('.', 'train15', 'weights', 'last.pt')

    model = YOLO(model_path)

    threshold = 0.5
    
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        results = model(frame)[0]   
         
        for result in results.boxes.data.tolist():
            print(result)
            x1, y1, x2, y2, score, class_id = result
            print(x1)
            print(y1)
            print(x2)
            print(y2)
            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            # cv2.imshow('detection', frame)

        # Check if the frame was read successfully
        if not ret:
            break

        
        
        # Display the frame
        cv2.imshow('detection', frame)
        
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Path to the video file on your local machine
video_path = '/home/tachyon/projects/videos/alley_-_39837 (1080p).mp4'

# Call the function to play the video
play_local_video(video_path)
