import cv2
import numpy as np
#import snap7  # For PLC Connection
import serial
import time

# Connection with Arduino
ser = serial.Serial('COM12', 9600, timeout=1)
time.sleep(2)


# To grab webcam feed:
webcam = cv2.VideoCapture(0)   # If we have another camera conected to the PC, you can read it putting number 1
#webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
#webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#webcam.set(10, 100)    # Brightness   (id for brigtness, brightness)
# To read and display the camera/video:
while True:
    read_successful, img = webcam.read()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Let's take the width and the height of the camera displayed
    height, width, read_successful = img.shape
    
    # Let's define the point's coordinates [x, y]:
    cx = int(width / 2)
    cy = int(height / 2)
    
    # Pick pixel value
    pixel_center = hsv_img[cy, cx]
    # We only take the hue value because is the one that define the color:
    hue_value = pixel_center[0]
    

    #~ WE DEFINE THE COLOR:
    color = "Undifined"
    number = 0
    #^ RED:
    if hue_value < 5:
        color = 'Red'
        number = 2
        ser.write(b'R')
    elif hue_value < 21:
        color = "Orange"
        ser.write(b'D')
    elif hue_value < 33:
        color = "Yellow"
        ser.write(b'D')
    #^ GREEN:
    elif hue_value < 89:
        color = "Green"
        number = 3
        ser.write(b'G')
    #^ BLUE:     
    elif hue_value < 131:
        color = "Blue"
        number = 4
        ser.write(b'B')
    elif hue_value < 172:
        color = "Violet"
        ser.write(b'D')
    else:
        color = 'Red'
        
    pixel_center_bgr = img[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    #print(pixel_center)
    cv2.circle(img, (cx, cy), 5, (b, g, r), cv2.FILLED)
    cv2.circle(img, (cx, cy), 5, (b, g, r), 1)
    cv2.putText(img, color, (cx+10, cy+10), 0, 1, (0, 0, 0), 2)
    print(number)

    cv2.imshow('Camera', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
ser.close()
