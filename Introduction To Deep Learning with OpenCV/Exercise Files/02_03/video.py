import numpy as np
import cv2

cap = cv2.VideoCapture('../images/shore.mov')

if cap.isOpened() == False:
    print( 'Cannot open file or video stream')
else:
    print(cap)

while True:
    ret, frame = cap.read()

    if ret == True:
        print (ret, frame)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == 27:
            break
    else:
        break

for c in [0, 1, 2]:
    while True:
        ret, frame = cap.read()

        if ret == True:
            print (ret, frame)
            cv2.imshow('Frame', frame[:,:,c])

            if cv2.waitKey(25) & 0xFF == 27:
                break
        else:
            break

cap.release()
cv2.destroyAllWindows()
