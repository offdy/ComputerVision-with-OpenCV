import sys
import numpy as np
import cv2


src = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch07/keyboard.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt): # 배경이 포함되는 것을 막기 위해 1부터 시작
    (x, y, w, h, area) = stats[i]

    if area < 20: # 노이즈들이 검출되는 것을 방지하기 위해서 흰색 객체의 픽셀 개수가 20보다 작으면 무시하도록 설정
        continue

    cv2.rectangle(dst, (x, y, w, h), (0, 0, 255)) # 빨간색 직사각형이 그려지도록

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
