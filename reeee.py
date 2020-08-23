import numpy as np
from time import sleep
import cv2 as cv2
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

#la O mayuscula ponla para que los servo no hagan nada
toArduino = 'O'

arriba = False
abajo = False
izquierda = False
derecha = False


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    cv2.circle(frame, (320, 240), 5, (0, 0, 255))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 3)

    for (x, y, w, h) in faces:

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

        if centro_x > 340 :
            print('mover a la derecha')
            derecha = True
        else: 
            derecha = False
            
        if centro_x < 300 :
            print('mover a la izquierda')
            izquierda = True
        else: 
            izquierda = False

        if centro_y < 220 :
            print('mover para abajo')
            abajo = True
        else: 
            abajo = False
            
        if centro_y > 260 :
            print('mover para arriba')
            arriba = True
        else: 
            arriba = False

        #convinados
        if (arriba & izquierda):
            print('sending A')
            toArduino = 'A'
            toArduinoEncode = toArduino.encode()
            ser.write(toArduinoEncode)
            

        if (arriba & derecha):
            print('sending B')
            toArduino = 'B'
            toArduinoEncode = toArduino.encode()
            ser.write(toArduinoEncode)
        
        if (abajo & izquierda):
            print('sending C')
            toArduino = 'C'
            toArduinoEncode = toArduino.encode()
            ser.write(toArduinoEncode)

        if (abajo & derecha):
            print('sending D')
            toArduino = 'D'
            toArduinoEncode = toArduino.encode()
            ser.write(toArduinoEncode)

        #solo direcciones solas
        if (arriba == True & izquierda == False & derecha == False & abajo == False):
            print('sending W')
            toArduino = 'W'
            toArduinoEncode = toArduino.encode()
            ser.write(toArduinoEncode)

        if (derecha == True & arriba == False & abajo == False & izquierda == False):
            print('sending X')
            toArduino = 'X'
            toArduinoEncode = toArduino.encode()
            ser.write(toArduinoEncode)
        
        if (izquierda == True & arriba == False & derecha == False & abajo == False):
            print('sending Y')
            toArduino = 'Y'
            toArduinoEncode = toArduino.encode()
            ser.write(toArduinoEncode)

        if (abajo == True & arriba == False & izquierda == False & derecha == False):
            print('sending Z')
            toArduino = 'Z'
            toArduinoEncode = toArduino.encode()
            ser.write(toArduinoEncode)



        cv2.rectangle(frame, (x, y), (width, height), color, stroke)
        cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 255))


    cv2.imshow('REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', frame)

    if cv2.waitKey(20) & 0xFF == ord('f'):
        break

cap.release()
cv2.destroyAllWindows()