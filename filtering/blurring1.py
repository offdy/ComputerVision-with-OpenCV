import sys
import numpy as np
import cv2


src = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch04/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

#kernel = np.ones((3, 3), dtype=np.float64) / 9. -> 1로 채워진 3X3 행렬 만들고 9로 나누기
#dst = cv2.filter2D(src, -1, kernel)

dst = cv2.blur(src, (3, 3))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
