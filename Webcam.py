import mediapipe as mp
import cv2
#import statements

#ONE "pose" = one set of all 33 points in 1 frame captured. 
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.75, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# create VideoCapture object
cap = cv2.VideoCapture(0)

while True:
    # read the frame
    ret, frame = cap.read()

    # Convert the BGR image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Process the image and detect poses
    results = pose.process(image)

    # draw pose landmarks on the page for this frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    cv2.imshow('Webcam', frame) #appears in a camera in a window called "Webcam"

    # wait for 1 ms and check if q is pressed --> quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#clean up
cap.release() #release frame-capture
cv2.destroyAllWindows() #close all windows
pose.close() #close the pose detection


