import numpy as np
from time import sleep
import time
import cv2 as cv2
import RPi.GPIO as GPIO

arriba = False
abajo = False
izquierda = False
derecha = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

servo0 = GPIO.PWM(12, 50)
servo1 = GPIO.PWM(32, 50)
servo2 = GPIO.PWM(33, 50)

servo0.start(0)
servo1.start(0)
servo2.start(0)

pos0 = 0
pos1 = 0
pos2 = 0

def setAngle(servo, angle):

    duty = angle / 18 + 2
    
    servo.ChangeDutyCycle(duty)
    
    sleep(0.1)
    
    servo.ChangeDutyCycle(0)

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

        while arriba == True :
            if pos1 >= 0 & pos1 < 200:
                pos1 -= 1
                setAngle(servo2, pos2)
                sleep(0.25)
                
            if pos2 > 0 & pos2 < 200:
                pos2 += 1
                setAngle(servo1, pos1)
                sleep(0.25)

        while abajo == True :
            if pos1 >= 0 & pos1 < 200:
                pos1 += 1
                setAngle(servo2, pos2)
                sleep(0.25)
                
            if pos2 > 0 & pos2 < 200:
                pos2 -= 1
                setAngle(servo1, pos1)
                sleep(0.25)

        while izquierda == True :
            if pos0 <= 360 & pos0 > 0:
                pos0 -= 1
                setAngle(servo0, pos0)
                sleep(0.5)

        while derecha == True :
            if pos0 <= 360 & pos0 >= 0:
                pos0 += 1
                setAngle(servo0, pos0)        
                sleep(0.5)

        cv2.rectangle(frame, (x, y), (width, height), color, stroke)
        cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 255))


    cv2.imshow('REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', frame)

    if cv2.waitKey(20) & 0xFF == ord('f'):
        servo0.stop()
        servo1.stop()
        servo2.stop()
        GPIO.cleanup()
        break

cap.release()
cv2.destroyAllWindows()