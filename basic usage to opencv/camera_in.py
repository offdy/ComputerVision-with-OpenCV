import sys
import cv2


# 카메라 열기
cap = cv2.VideoCapture('/Users/ehddud/Desktop/Computer Vision/ch02/video1.mp4')

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# # 프레임 크기 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame  # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27: # ESC
        break

cap.release()
cv2.destroyAllWindows()
