import numpy as np
import cv2 as cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    cv2.circle(frame, (320, 240), 5, (0, 0, 255))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 4)

    for (x, y, w, h)in faces:

        coordenates = [x, y, w, h]

        #print("las coordenadas son: " + str(coordenates))

        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]

        img_item = "dumb_bitch.png"
        cv2.imwrite(img_item, roi_gray)

        color = (0, 255, 0) #BGR
        stroke = 2

        width = x + w 
        height = y + h   

        centro_x = int(round(width - w/2))
        centro_y = int(round(height - h/2))

        min_x = 300
        max_x = 340

        min_y = 220
        max_y = 260

        if(min_x <= centro_x <= max_x) & (min_y <= centro_y <= max_y):
            color = (0, 0, 255)

        while centro_x > 340 :
            print('mover a la derecha')

        while centro_x < 300 :
            print('mover a la izquiera')

        while centro_y < 220 :
            print('mover para abajo')

        while centro_y > 260 :
            print('mover para arriba')

        cv2.rectangle(frame, (x, y), (width, height), color, stroke)
        cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 255))


    cv2.imshow('REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', frame)

    if cv2.waitKey(20) & 0xFF == ord('f'):
        break

cap.release()
cv2.destroyAllWindows()