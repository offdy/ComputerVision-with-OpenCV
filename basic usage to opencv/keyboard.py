import sys
import numpy as np
import cv2


img = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch02/cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    keycode = cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'): # i or I key를 눌렀을 때 영상 반전
        img = ~img
        cv2.imshow('image', img)
    elif keycode == 27:
        break

cv2.destroyAllWindows()
