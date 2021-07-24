import cv2
import winsound
cam =cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2) # to let the machine know that we are moving form the initial place to final.
    gray =cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) #to make the frame gray .
    blur =cv2.GaussianBlur(gray,(5,5),0) #To make the frame blur and sharper.
    _, thresh =cv2.threshold(blur,20, 255, cv2.THRESH_BINARY) # To remove the unwanted noise.
    dialted = cv2.dilate(thresh, None , iterations=3) #to make the capture image bigger.
    contours, _= cv2.findContours(dialted, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)# the boundaries are called as contours.
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2) #(the frame, the variable assigned, the color ,the thickness)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(c) # For drawing the rectangle bounding boxes (x+y , w+h , x+w ,y+h)
        cv2.rectangle(frame1,(x,y),(x+w , y+h),(0,255,0),2)
        winsound.Beep(500,200) #to create sound
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Invigilator Cam', frame1)