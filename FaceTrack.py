import cv2
import sys

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

face = False 

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display helping text and boolean attribute 
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)  
    fontScale = 2
    color = (0, 1, 0)  
    thickness = 2
    a = "True"
    b = "False"

    if (x) in faces: 
        cv2.putText(frame, a, org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    else: 
        cv2.putText(frame, b, org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()