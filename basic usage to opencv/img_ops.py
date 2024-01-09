import numpy as np
import cv2


# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)       # grayscale image, 픽셀값은 랜덤으로 채워짐
img2 = np.zeros((240, 320, 3), dtype=np.uint8)    # color image, 모든 픽셀값은 0으로 채워짐
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # dark gray, 모든 픽셀값은 1로 채워짐
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow -> green + blue

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch02/HappyFish.jpg')

img2 = img1
img3 = img1.copy()

#img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch02/HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱, 40번째 행부터 120번째 행까지, 30번째 열부터 150번째 열까지
img3 = img1[40:120, 30:150].copy()

img2.fill(0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
