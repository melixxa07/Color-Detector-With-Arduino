import cv2
import numpy as np


#~ Trackbar:
def empty(x):
    pass

cv2.namedWindow('Trackbar')
#cv2.resizeWindow('TrackBars', 640, 250)
cv2.createTrackbar('H', 'Trackbar', 0, 179 , empty)
cv2.createTrackbar('S', 'Trackbar', 255, 255, empty)
cv2.createTrackbar('V', 'Trackbar', 255, 255, empty)

img_hsv = np.zeros((250, 500, 3), np.uint8)

while True:
    h = cv2.getTrackbarPos ('H', 'Trackbar')
    s = cv2.getTrackbarPos ('S', 'Trackbar')
    v = cv2.getTrackbarPos ('V', 'Trackbar')
    
    img_hsv[:] = (h, s, v)
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    
    cv2.imshow('Trackbar', img_bgr)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cv2.destroyAllWindows()

