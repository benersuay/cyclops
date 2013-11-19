import serial
import numpy
import cv2
import time

ser = serial.Serial("/dev/ttyUSB0",9600,timeout=1)
cap = cv2.VideoCapture(1)

for i in range(100):
    ret, frame = cap.read()
    cv2.imshow('3D Scanner',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ser.write("P0,0"+str(i)+"\r")
    time.sleep(0.5)
    if i == 99:
        ser.write("P0,0000\r")
    
cap.release()
del cap
cv2.destroyAllWindows()
    
