import sys
import numpy as np
import cv2


src = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch07/rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
# -> OTSU 방법을 쓸 때 파라미터 두번째 인자는 0으로 주고, 마지막 인자에 cv2.THRESH_BINARY와 cv2.THRESH_OTSU를 OR 연산자로 묶어서 줌
print("otsu's threshold:", th)  # 131

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
