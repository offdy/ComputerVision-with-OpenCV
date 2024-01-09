import sys
import cv2


# 마스크 영상을 이용한 영상 합성
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

# src 영상에서 mask 부분을 이용하여 만든 영상을 dst 영상에 copy. src, mask, dst 사이즈 다 같아야 하며, src와 dst는 타입이 같아야 함
cv2.copyTo(src, mask, dst) 
# dst[mask > 0] = src[mask > 0] # -> dst 영상의 픽셀값 자체를 바꿔서 위의 copyTo 함수와 동일한 영상을 생성

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 알파 채널을 마스크 영상으로 이용

src = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch02/cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch02/opencv-logo-white.png', cv2.IMREAD_UNCHANGED) # 채널 수 4인 영상(R,G,B,알파 네개의 채널)


if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]   # mask 영상의 height와 width 추출
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출(src 영상이 mask 영상과 logo 영상보다 크기 때문)

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
