import numpy as np
import cv2


def on_level_change(pos):
    value = pos * 16
    if value >= 255:
        value = 255
    # np.clip(level, 0, 255)로 해도 동일한 결과

    img[:] = value
    cv2.imshow('image', img)


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)
# 창이 생성되고 난 이후에 createTrackbar 함수 호출해야 함

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
