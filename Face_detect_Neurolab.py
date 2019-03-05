#import openCV library and numpy
import cv2
import numpy as np

#set up and load the image video, resizing the webcam window
cap = cv2.VideoCapture(0)
cap.set(3 ,640)
cap.set(4, 480)

#create boolean value to check the waitKey
flag = True
isRecording =True

#load the pre-trained cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#run face detection and create the rectangle
while True:
    while isRecording:
        #capture frame-by-frame
        ret, frame= cap.read()

        #run face detection
        #detectMultiScale(img, scale factor, number of minimum neighbors)
        vid_gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(vid_gray, 1.3, 6)

        #count faces
        cv2.putText(frame,'Number of face detected: '+ str(len(faces)), (10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 255, 0),2 )
        cv2.putText(frame,'Press \'p\' to pause, \'c\' to continue, \'q\' to quit ', (10,40),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0),2 )
        #show faces
        for (x,y,w,h) in faces:

            #draw the rectangle on the main image
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),5)

        #display the frame
        cv2.imshow('faces',frame)

        key= cv2.waitKey(1) & 0xFF

        #press p to pause the display
        if key == ord('p'):
            print('p')
            isRecording= False

        #press q to quit the program
        elif key == ord('q'):
            print('q')
            flag= False
            break
    k=cv2.waitKey(1) & 0xFF

    if flag== False:
        break

    else:
        #press c to continue the paused video
        if k == ord('c'):
            print ('c')
            isRecording= True
        #quit the program
        elif k == ord('q'):
            print ('q')
            break

cap.release()
cv2.destroyAllWindows()
