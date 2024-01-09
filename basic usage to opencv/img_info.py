import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch02/cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch02/cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

# 영상의 속성 참조
print('type(img1):', type(img1))
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img1.dtype:', img1.dtype)

# 영상의 크기 참조
h, w = img2.shape[:2] # h, w = img2.shape 이렇게만 실행하면 컬러 이미지는 채널 수 까지 shape이 (h,w,3)이므로 h,w 두개로 받을 수 없음
print('img2 size: {} x {}'.format(w, h))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

'''
# 영상의 픽셀 값 참조
for y in range(h):
    for x in range(w):
        img1[y, x] = 255 # img1의 모든 픽셀 값을 참조해서 하얀색으로 변경
        img2[y, x] = (0, 0, 255) # img2의 모든 픽셀 값을 참조해서 파란색으로 변경

''' # 위 처럼 for 문을 활용한 방식은 시간이 오래 걸리므로 사용 지양

# img1[:,:] = 255
# img2[:,:] = (0, 0, 255) -> 이렇게 전체 범위 지정해서 모든 픽셀 값을 한꺼번에 세팅하는 것이 훨씬 빠르게 동작

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
