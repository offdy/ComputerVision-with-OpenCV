import cv2
import sys

print('Hello, OpenCv', cv2.__version__)

img = cv2.imread('/Users/ehddud/Desktop/Computer Vision/ch01/cat.bmp',cv2.IMREAD_GRAYSCALE )
if img is None:
    print('Image load failed!')
    sys.exit()
    
cv2.imwrite('cat_gray.png', img)
cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey() # waitKey() 함수를 실행해야 imshow가 작동함

cv2.destroyAllWindows()
