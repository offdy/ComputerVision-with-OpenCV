import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch01/cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off') # 가로, 세로의 눈금 삭제
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch01/cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB) # plt.subplot(121) -> 1: 한 개의 행, 2: 두 개의 열, 1: 그 중에 첫번째 열에 그림을 그려라
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray') # plt.subplot(123) -> 1: 한 개의 행, 2: 두 개의 열, 1: 그 중에 두번째 열에 그림을 그려라
plt.show()
