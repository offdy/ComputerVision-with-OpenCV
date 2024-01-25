import sys
import numpy as np
import cv2

src = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch04/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5) # 10보다 작은것은 비슷한 색깔로 간주하고 10보다 큰 것은 edge로 판단

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
