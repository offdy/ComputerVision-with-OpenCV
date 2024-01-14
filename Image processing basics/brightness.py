import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
src = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, 100)
#dst = np.clip(src + 100., 0, 255).astype(np.uint8) # 0보다 작으면 0으로 만들고, 255보다 크면 255로 만듦

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상 불러오기
src = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch03/lenna256.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0))
# 스칼라는 실수값 네 개로 구성된 튜플, 즉, 100을 입력하면 (100,0,0,0)의 형태로 입력이 된다고 생각하면 됨
# 그레이스케일 영상에서 src2에 100을 입력하면 픽셀값이 100만큼 커져서 영상이 밝아짐
# 컬러 영상에서 src2에 100을 입력하면 (100,0,0,0) ->(b,g,r,알파) 즉, blue 성분만 100만큼 증가하게 됨

#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
